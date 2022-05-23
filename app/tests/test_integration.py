import pytest
from app.app import app
from app.settings.settings import ENVIRONMENT
from app.tests.fixtures import bad_matrix, horizontal_matrix, invalid_matrix
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_stats():
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.get("/stats/")

    assert response.status_code == 200
    assert "ratio" in response.json()
    assert "count_human_dna" in response.json()
    assert "count_mutant_dna" in response.json()


@pytest.mark.skipif(ENVIRONMENT != "TESTING", reason="This test writes on db")
@pytest.mark.asyncio
async def test_mutant_true(horizontal_matrix):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": horizontal_matrix.dna_sequences}
        )

        assert response.json() == {"is_mutant": True}
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.skipif(ENVIRONMENT != "TESTING", reason="This test writes on db")
@pytest.mark.asyncio
async def test_mutant_false(bad_matrix):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post("/mutant/", json={"dna": bad_matrix.dna_sequences})

        assert response.json() == {"is_mutant": False}
        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.skipif(ENVIRONMENT != "TESTING", reason="This test writes on db")
@pytest.mark.asyncio
async def test_mutant_none(invalid_matrix):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": invalid_matrix.dna_sequences}
        )

        assert response.json() == {"is_mutant": "corrupted input"}
        assert response.status_code == status.HTTP_400_BAD_REQUEST
