import asyncio
from app.scripts.person import Person
from fastapi import APIRouter, Body, Response, status

from app.models.dna_matrix import DNAMatrixSchema

from app.utils.helpers import configure_handlers
from app.utils.queue import MongoQueue
from app.models.person import PersonSchema
from fastapi.encoders import jsonable_encoder
from app.db.operations import insert_bulk_data
import os

MONGO_QUEUE_SIZE = os.getenv("MONGO_QUEUE_SIZE")
router = APIRouter()
main_handler = configure_handlers()
mongo_queue = MongoQueue(500)


@router.post(
    "/",
    response_description="DNA analysis data added into database",
    status_code=status.HTTP_200_OK,
)
async def mutant(response: Response, request: DNAMatrixSchema = Body(...)):
    request_data = jsonable_encoder(request)
    dna_matrix = request_data["dna"]

    p = Person(dna_matrix)
    is_mutant = await p.is_mutant(main_handler)

    ready_to_send = await mongo_queue.add_job(
        {"dna": dna_matrix, "is_mutant": is_mutant}
    )

    if ready_to_send:
        data_to_insert = await mongo_queue.convert_queue_to_list()
        await insert_bulk_data(data_to_insert)

    if not is_mutant:
        response.status_code = status.HTTP_403_FORBIDDEN

    return {"is_mutant": is_mutant}
