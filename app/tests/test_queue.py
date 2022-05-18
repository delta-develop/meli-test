from random import randint
import pytest
from app.utils.queue import MongoQueue


@pytest.fixture
def mongo_queue():
    return MongoQueue()


@pytest.fixture
def not_mutant_data():
    return {
        "dna": [generate_dna(), "CAGTTC", "TTATGC", "AGAAGG", "CCCTTA", "TCCCGG"],
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
    await mongo_queue.add_job(is_mutant_data)
    await mongo_queue.add_job(not_mutant_data)

    assert mongo_queue.queue_size == 2


@pytest.mark.asyncio
async def test_send_jobs(mongo_queue):
    await mongo_queue.clear_queue()
    for i in range(5):
        print(i)
        await mongo_queue.add_job(
            {
                "dna": ["ATGCGA", "CAGTTC", "TTATGC", "AGAAGG", "CCCTTA", "TCCCGG"],
                "is_mutant": False,
            }
        )
        # await mongo_queue.add_job(
        #     {
        #         "dna": ["AAAAAA", "CCCCCC", "GGGGGG", "TTTTTT", "AAAAAA", "CCCCCC"],
        #         "is_mutant": True,
        #     }
        # )

    assert mongo_queue.queue_size == 5
