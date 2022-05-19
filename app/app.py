from __future__ import annotations

import os
from functools import lru_cache

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from app.orchestator.orchestator import mongo_queue
from app.routes.mutant_router import router as DNAAnalysisRouter
from app.routes.stats_router import router as StatsRouter
from app.settings.settings import (
    ENVIRONMENT,
    create_collection,
    get_database_and_collection_name,
)

EMPTYING_TIME = os.getenv("EMPTYING_TIME")

app = FastAPI()
app.include_router(DNAAnalysisRouter, tags=["DNAAnalysis"], prefix="/mutant")
app.include_router(StatsRouter, tags=["Statistics"], prefix="/stats")


@app.on_event("startup")
async def startup_event():
    print("Setting up database...")
    database, collection_name = get_database_and_collection_name(ENVIRONMENT)
    await create_collection(database, collection_name)


@app.on_event("startup")
@repeat_every(seconds=int(EMPTYING_TIME))
async def shutdown_event():

    if mongo_queue.queue_size > 0:
        print("Emptying queues...")
        await mongo_queue.empty_the_queue()
