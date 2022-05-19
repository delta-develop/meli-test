from app.models.dna_matrix import DNAMatrixSchema
from app.orchestator.orchestator import analyze_adn, save_data
from fastapi import APIRouter, BackgroundTasks, Body, Response, status

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
