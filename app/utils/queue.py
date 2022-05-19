from queue import Queue
from app.utils.helpers import configure_handlers


main_handler = configure_handlers()


class MongoQueue:
    def __init__(self, max_queue_size):
        self.job_queue = Queue(maxsize=max_queue_size + 2)
        self.max_queue_size = max_queue_size

    async def add_job(self, data):
        self.job_queue.put(data)

        return self.queue_size

    async def convert_queue_to_list(self):
        data_to_insert = []
        while self.job_queue.empty() == False:
            data_to_insert.append(self.job_queue.get())

        return data_to_insert

    @property
    def ready_to_send(self):
        if self.queue_size >= self.max_queue_size:
            return True
        return False

    @property
    def queue_size(self):
        return self.job_queue.qsize()
