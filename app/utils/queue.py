from queue import Queue
from typing import List

from app.db.operations import insert_bulk_data


class MongoQueue:
    """This class represent the queue of results to be stored at MongoDB"""

    def __init__(self, max_queue_size: int) -> None:
        self.job_queue: Queue = Queue(maxsize=max_queue_size + 2)
        self.max_queue_size: int = max_queue_size

    async def add_job(self, analysis_result: dict) -> None:
        """Enqueue result to the current queue

        Args:
            analysis_result (dict): Result of the analysis.
        """
        self.job_queue.put(analysis_result)

    async def convert_queue_to_list(self) -> List:
        """This get the queue when is full and convert it to a list in order
        to make an bulk insert to mongo. This step may look unnecessary, but
        without this, there will be a lot of errors and repeaed registers in
        mongo, reducing performance.

        Returns:
            List: queue data in list form ready to be send.
        """
        data_to_insert = []
        while self.job_queue.empty() == False:
            data_to_insert.append(self.job_queue.get())

        return data_to_insert

    @property
    def ready_to_send(self) -> bool:
        """This property check if the queue has the size to send it data.

        Returns:
            bool: True if has reached perfect size else false.
        """
        if self.queue_size >= self.max_queue_size:
            return True
        return False

    @property
    def queue_size(self) -> int:
        """Return the size of que queue.

        Returns:
            int: Queue size.
        """
        return self.job_queue.qsize()

    async def empty_the_queue(self) -> None:
        """This method is called when the queue is full, inserting all the
        collected data by once in MongoDB.
        """
        data_to_insert = await self.convert_queue_to_list()
        if data_to_insert:
            await insert_bulk_data(data_to_insert)
