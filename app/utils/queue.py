from queue import Queue
from typing import List

from app.db.operations import insert_bulk_data


class MongoQueue:
    def __init__(self, max_queue_size: int) -> None:
        self.job_queue = Queue(maxsize=max_queue_size + 2)
        self.max_queue_size = max_queue_size

    async def add_job(self, analysis_result: dict) -> None:
        self.job_queue.put(analysis_result)

    async def convert_queue_to_list(self) -> List:
        data_to_insert = []
        while self.job_queue.empty() == False:
            data_to_insert.append(self.job_queue.get())

        return data_to_insert

    @property
    def ready_to_send(self) -> bool:
        if self.queue_size >= self.max_queue_size:
            return True
        return False

    @property
    def queue_size(self) -> int:
        return self.job_queue.qsize()

    async def empty_the_queue(self) -> None:
        data_to_insert = await self.convert_queue_to_list()
        if data_to_insert:
            await insert_bulk_data(data_to_insert)
