from fastapi.encoders import jsonable_encoder
from app.scripts.person import Person

from app.utils.helpers import configure_handlers
from app.utils.queue import MongoQueue
import os
from fastapi import status

MONGO_QUEUE_SIZE = os.getenv("MONGO_QUEUE_SIZE")
main_handler = configure_handlers()
mongo_queue = MongoQueue(500)


async def analyze_adn(request, response):
    request_data = jsonable_encoder(request)
    dna_matrix = request_data["dna"]

    p = Person(dna_matrix)
    is_mutant = await p.is_mutant(main_handler)
    response = {"is_mutant": is_mutant}

    if is_mutant == False:
        response.status_code = status.HTTP_403_FORBIDDEN
    elif is_mutant == None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        response = {"error": "Invalid input data"}

    return response


async def save_data(data):

    await mongo_queue.add_job(data)

    if mongo_queue.ready_to_send:
        await mongo_queue.empty_the_queue()
