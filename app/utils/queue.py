import asyncio
from queue import Queue
from app.db.operations import insert_bulk_data, insert_one


class MongoQueue:
    def __init__(self):
        self.job_queue = Queue(maxsize=502)

    async def add_job(self, data):

        self.job_queue.put(data)

        if self.job_queue.qsize() >= 500:
            # print(f"Enviando jobs: {self.job_queue.qsize()}")
            await self.send_jobs()

            # await self.send_jobs()
            # print(f"jobs enviados: {self.job_queue.qsize()}")
            # await self.clear_queue()
            # print(f"limpiando cola: {self.job_queue.qsize()}")

    async def clear_queue(self):
        with self.job_queue.mutex:
            self.job_queue.queue.clear()

    async def send_jobs(self):
        # await insert_bulk_data(self.job_queue.queue)
        # print(f"jobs enviados: {self.job_queue.qsize()}")
        await insert_bulk_data(self.job_queue)
        # print(f"jobs enviados: {self.job_queue.qsize()}")

    @property
    def queue_size(self):
        return self.job_queue.qsize()
