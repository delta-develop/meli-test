from app.models.dna_matrix import DNAMatrixSchema
from app.orchestator.orchestator import analyze_dna
import pytest
from fastapi import Response
from app.tests.fixtures import invalid_matrix, horizontal_matrix, bad_matrix


@pytest.fixture
def response():
    return Response()


@pytest.mark.asyncio
async def test_is_mutant(horizontal_matrix, response):
    request = DNAMatrixSchema(dna=horizontal_matrix.dna_sequences)
    resp = await analyze_dna(request, response)

    assert resp == {"dna": horizontal_matrix.dna_sequences, "is_mutant": True}
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_not_mutant(bad_matrix, response):
    request = DNAMatrixSchema(dna=bad_matrix.dna_sequences)
    resp = await analyze_dna(request, response)

    assert resp == {"dna": bad_matrix.dna_sequences, "is_mutant": False}
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_invalid_request(invalid_matrix, response):
    request = DNAMatrixSchema(dna=invalid_matrix.dna_sequences)
    resp = await analyze_dna(request, response)

    assert resp == {
        "dna": invalid_matrix.dna_sequences,
        "is_mutant": "corrupted input",
    }
    assert response.status_code == 400
