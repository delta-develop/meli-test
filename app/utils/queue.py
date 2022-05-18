import asyncio
from queue import Queue
from app.db.operations import insert_bulk_data, insert_one
from datetime import datetime
import copy
from app.tasks.celery_worker import test
from celery import group


class MongoQueue:
    def __init__(self):
        self.job_queue = Queue()

    async def add_job(self, data):

        self.job_queue.put(test.s(data))

        if self.job_queue.qsize() >= 500:

            await self.send_jobs()
            await self.clear_queue()

    async def clear_queue(self):
        with self.job_queue.mutex:
            self.job_queue.queue.clear()

    async def send_jobs(self):
        # await insert_bulk_data(self.job_queue.queue)
        x = group(list(self.job_queue.queue))
        # test.delay(list(self.job_queue.queue))
        r = x.delay()

    @property
    def queue_size(self):
        return self.job_queue.qsize()
