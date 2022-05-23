import pytest
from app.models.dna_matrix import DNAMatrixSchema
from app.orchestator.orchestator import analyze_dna, enqueue_data, mongo_queue
from app.settings.settings import ENVIRONMENT
from app.tests.fixtures import bad_matrix, horizontal_matrix, invalid_matrix
from fastapi import Response


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


@pytest.mark.skipif(ENVIRONMENT != "TESTING", reason="This test writes on db")
@pytest.mark.asyncio
async def test_auto_empty_queue(horizontal_matrix, bad_matrix, response):
    await mongo_queue.empty_the_queue()
    assert mongo_queue.queue_size == 0

    await enqueue_data({"hello": "world"})
    assert mongo_queue.queue_size == 1

    await enqueue_data({"hello": "world"})

    assert mongo_queue.queue_size == 2
    assert mongo_queue.ready_to_send == False

    await enqueue_data({"hello": "world"})
    assert mongo_queue.queue_size == 0
