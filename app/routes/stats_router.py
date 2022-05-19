from app.db.operations import get_statistics
from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get(
    "/",
    response_description="Statistics of DNA results.",
    status_code=status.HTTP_200_OK,
)
async def stats(response: Response):
    stats = await get_statistics()

    return stats
