from app.scripts.person import Person
from fastapi import APIRouter, Body, Response, status
from fastapi.encoders import jsonable_encoder

from app.utils.db_connection import add_result

from app.models.dna_matrix import DNAMatrixSchema
from app.utils.helpers import configure_handlers

router = APIRouter()
main_handler = configure_handlers()


@router.post(
    "/",
    response_description="DNA analysis data added into database",
    status_code=status.HTTP_200_OK,
)
async def mutant(response: Response, request: DNAMatrixSchema = Body(...)):
    request = jsonable_encoder(request)
    dna_matrix = request["dna"]

    p = Person(dna_matrix)
    is_mutant = p.is_mutant(main_handler)

    await add_result(dna_matrix, is_mutant)

    if not is_mutant:
        response.status_code = status.HTTP_403_FORBIDDEN

    return {"is_mutant": is_mutant}
