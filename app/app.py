from __future__ import annotations

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from app.orchestator.orchestator import mongo_queue
from app.routes.mutant_router import router as DNAAnalysisRouter
from app.routes.stats_router import router as StatsRouter
from app.settings.settings import (
    EMPTYING_TIME,
    ENVIRONMENT,
    create_collection,
    get_database_and_collection_name,
)

app = FastAPI()
app.include_router(DNAAnalysisRouter, tags=["DNAAnalysis"], prefix="/mutant")
app.include_router(StatsRouter, tags=["Statistics"], prefix="/stats")


@app.get("/")
async def root():
    return {
        "Author": "Leonardo Daniel Hernández García",
        "Contact": "leohg.ipn@gmail.com",
        "Running_on": "FastAPI",
        "Database": "MongoDB",
        "Hosted_on": "AWS EC2 Instances",
        "Title": "Software Development Engineer test for Mercado Libre",
        "Notes": "I'm resisting the urge to put an easter egg on this project -_-' ",
        "Apologies": "I'm sorry, I don't have more energy to build a decent home page.",
    }


@app.on_event("startup")
async def startup_event() -> None:
    """Configure the database as soon the application start up."""
    database, collection_name = get_database_and_collection_name(ENVIRONMENT)
    await create_collection(database, collection_name)


@app.on_event("startup")
@repeat_every(seconds=EMPTYING_TIME)
async def empty_queues() -> None:
    """In order to increase performance, the data is being sent in packages,
    so when the requests traffic decrease, some results may be stucked into
    queues, for that reason, this function run periodically to empty the
    queues even if it has not reached the perfect size."""

    if mongo_queue.queue_size > 0:
        await mongo_queue.empty_the_queue()
