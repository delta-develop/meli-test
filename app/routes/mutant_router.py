import asyncio
from app.scripts.person import Person
from fastapi import APIRouter, Body, Response, status

from app.models.dna_matrix import DNAMatrixSchema

from app.utils.helpers import configure_handlers
from app.utils.queue import MongoQueue
from app.models.person import PersonSchema
from fastapi.encoders import jsonable_encoder
from app.db.operations import insert_one


router = APIRouter()
main_handler = configure_handlers()
mongo_queue = MongoQueue()


@router.post(
    "/",
    response_description="DNA analysis data added into database",
    status_code=status.HTTP_200_OK,
)
async def mutant(response: Response, request: DNAMatrixSchema = Body(...)):
    request_data = jsonable_encoder(request)
    dna_matrix = request_data["dna"]

    p = Person(dna_matrix)
    result = await p.is_mutant(main_handler)
    await mongo_queue.add_job({"dna": dna_matrix, "is_mutant": result})

    return {"is_mutant": result}
