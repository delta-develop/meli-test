import asyncio
from turtle import back
from fastapi import APIRouter, Body, Response, status, BackgroundTasks

from app.models.dna_matrix import DNAMatrixSchema

from app.models.person import PersonSchema
from fastapi.encoders import jsonable_encoder
from app.orchestator.orchestator import analyze_adn, save_data

router = APIRouter()


@router.post(
    "/",
    response_description="DNA analysis data added into database",
    status_code=status.HTTP_200_OK,
)
async def is_mutant(
    response: Response,
    background_tasks: BackgroundTasks,
    request: DNAMatrixSchema = Body(...),
):

    analysis_result = await analyze_adn(request, response)
    background_tasks.add_task(save_data, analysis_result)

    return analysis_result
