from app.models.dna_matrix import DNAMatrixSchema
from app.orchestator.orchestator import analyze_dna, enqueue_data
from fastapi import APIRouter, BackgroundTasks, Body, Response, status

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def is_mutant(
    response: Response,
    background_tasks: BackgroundTasks,
    request: DNAMatrixSchema = Body(...),
) -> dict:
    """Attend the /mutant/ endpoint, first make the dna analysis, put
    the enqueue data process running in background, then return the
    response. After the response has been sent, the background task
    finish their job, putting the result into the queue.


    Returns:
        dict: Result of the analysis.
    """
    analysis_result = await analyze_dna(request, response)
    background_tasks.add_task(enqueue_data, analysis_result)
    return analysis_result
