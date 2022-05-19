from app.db.operations import get_statistics
from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get(
    "/",
    response_description="Statistics of DNA results.",
    status_code=status.HTTP_200_OK,
)
async def stats(response: Response) -> dict:
    """Attend the /stats/ endpoint

    Returns:
        dict: results of the collected data.
    """
    stats = await get_statistics()

    return stats
