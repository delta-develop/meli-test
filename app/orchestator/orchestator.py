import os

from app.models.dna_matrix import DNAMatrixSchema
from app.scripts.person import Person
from app.utils.helpers import configure_handlers
from app.utils.queue import MongoQueue
from fastapi import Response, status
from fastapi.encoders import jsonable_encoder
from app.settings.settings import MAX_QUEUE_SIZE


main_handler = configure_handlers()
mongo_queue = MongoQueue(MAX_QUEUE_SIZE)


async def analyze_dna(request: DNAMatrixSchema, response: Response) -> dict:
    """Function to make all calculus to check if a given input belongs to a
    mutant.

    Args:
        request (DNAMatrixSchema): Request from the endpoint /mutant/
        response (Response): Result of the dna analysis and correspondent
        http status.

    Returns:
        dict: Result of dna analysis.
    """
    request_data = jsonable_encoder(request)
    dna_matrix = request_data["dna"]

    p = Person(dna_matrix)
    is_mutant = await p.is_mutant(main_handler)
    response_json = {"dna": dna_matrix, "is_mutant": is_mutant}

    if is_mutant == False:
        response.status_code = status.HTTP_403_FORBIDDEN
    elif is_mutant == None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        response_json["is_mutant"] = "corrupted input"

    return response_json


async def enqueue_data(data: dict) -> None:
    """Put the results of the analysis into a queue until queue is full
    or ready to send.

    Args:
        data (dict): dna matrix and analysis result.
    """
    await mongo_queue.add_job(data)

    if mongo_queue.ready_to_send:
        await mongo_queue.empty_the_queue()
