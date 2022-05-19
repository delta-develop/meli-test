from random import randint
import pytest
from app.utils.queue import MongoQueue


@pytest.fixture
def mongo_queue():
    return MongoQueue(5)


@pytest.fixture
def not_mutant_data():
    return {
        "dna": ["CAGTTC", "CAGTTC", "TTATGC", "AGAAGG", "CCCTTA", "TCCCGG"],
        "is_mutant": False,
    }


@pytest.fixture
def is_mutant_data():
    return {
        "dna": ["AAAAAA", "CCCCCC", "GGGGGG", "TTTTTT", "AAAAAA", "CCCCCC"],
        "is_mutant": True,
    }


@pytest.mark.asyncio
async def test_mongo_queue(mongo_queue, is_mutant_data, not_mutant_data):

    assert mongo_queue.queue_size == 0

    await mongo_queue.add_job(is_mutant_data)
    await mongo_queue.add_job(not_mutant_data)

    assert mongo_queue.queue_size == 2


@pytest.mark.asyncio
async def test_queue_ready_to_send(mongo_queue, is_mutant_data, not_mutant_data):

    assert mongo_queue.ready_to_send == False

    for _ in range(3):
        await mongo_queue.add_job(not_mutant_data)

    for _ in range(2):
        await mongo_queue.add_job(is_mutant_data)

    assert mongo_queue.ready_to_send == True


@pytest.mark.asyncio
async def test_convert_queue_to_list(mongo_queue, is_mutant_data, not_mutant_data):

    for _ in range(3):
        await mongo_queue.add_job(not_mutant_data)

    for _ in range(2):
        await mongo_queue.add_job(is_mutant_data)

    queue_list = [
        not_mutant_data,
        not_mutant_data,
        not_mutant_data,
        is_mutant_data,
        is_mutant_data,
    ]

    assert await mongo_queue.convert_queue_to_list() == queue_list
