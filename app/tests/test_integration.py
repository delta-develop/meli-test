from app.app import app
import pytest
from app.settings.settings import drop_testing_db
from httpx import AsyncClient

from app.tests.fixtures import (
    bad_matrix,
    single_matrix,
    diagonal_matrix,
    diagonal_matrix_lower,
    angled_matrix,
    empty_matrix,
    horizontal_matrix,
    almost_mutant_horizontal_matrix,
    almost_mutant_vertical_matrix,
    is_mutant,
    not_mutant,
)


@pytest.mark.asyncio
async def test_horizontal_matrix(horizontal_matrix, is_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": horizontal_matrix.dna_sequences}
        )

    assert response.status_code == 200
    assert response.json() == is_mutant


@pytest.mark.asyncio
async def test_single_matrix(single_matrix, is_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": single_matrix.dna_sequences}
        )

    assert response.status_code == 200
    assert response.json() == is_mutant


@pytest.mark.asyncio
async def test_diagonal_matrix(diagonal_matrix, is_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": diagonal_matrix.dna_sequences}
        )

    assert response.status_code == 200
    assert response.json() == is_mutant


@pytest.mark.asyncio
async def test_lower_diagonal_matrix(diagonal_matrix_lower, is_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": diagonal_matrix_lower.dna_sequences}
        )

    assert response.status_code == 200
    assert response.json() == is_mutant


@pytest.mark.asyncio
async def test_angled_matrix(angled_matrix, is_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": angled_matrix.dna_sequences}
        )

    assert response.status_code == 200
    assert response.json() == is_mutant


@pytest.mark.asyncio
async def test_bad_matrix(bad_matrix, not_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post("/mutant/", json={"dna": bad_matrix.dna_sequences})

    assert response.status_code == 403
    assert response.json() == not_mutant


@pytest.mark.asyncio
async def test_empty_matrix(empty_matrix, not_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": empty_matrix.dna_sequences}
        )
    assert response.status_code == 403
    assert response.json() == not_mutant


@pytest.mark.asyncio
async def test_almost_mutant_horizontal(almost_mutant_horizontal_matrix, not_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": almost_mutant_horizontal_matrix.dna_sequences}
        )
    assert response.status_code == 403
    assert response.json() == not_mutant


@pytest.mark.asyncio
async def test_almost_mutant_vertical(almost_mutant_vertical_matrix, not_mutant):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.post(
            "/mutant/", json={"dna": almost_mutant_vertical_matrix.dna_sequences}
        )
    assert response.status_code == 403
    assert response.json() == not_mutant


@pytest.mark.asyncio
async def test_stats():
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        response = await client.get("/stats/")
    assert response.status_code == 200
    assert response.json() == {
        "mutants": 5,
        "non-mutants": 4,
        "ratio_mutants-non_mutants": 1.25,
    }
    drop_testing_db()
