import asyncio
from queue import Queue
from app.db.operations import insert_bulk_data, insert_one
from app.utils.helpers import configure_handlers


main_handler = configure_handlers()


class MongoQueue:
    def __init__(self):
        self.job_queue = Queue(maxsize=502)

    async def add_job(self, data):

        self.job_queue.put(data)

        if self.job_queue.qsize() >= 500:

            data_to_insert = await self.convert_to_data()
            await insert_bulk_data(data_to_insert)

    async def convert_to_data(self):
        data_to_insert = []
        while self.job_queue.empty() == False:
            data_to_insert.append(self.job_queue.get())

        return data_to_insert
