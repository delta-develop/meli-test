import pytest
from app.app import app
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_stats():
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.get("/stats/")

    assert response.status_code == 200
    assert "mutants" in response.json()
    assert "non-mutants" in response.json()
    assert "ratio_mutants-non_mutants" in response.json()
