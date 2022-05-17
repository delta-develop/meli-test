from __future__ import annotations
from app.routes.mutant_router import router as DNAAnalysisRouter
from app.routes.stats_router import router as StatsRouter
from functools import lru_cache
from fastapi import FastAPI
from app.settings.settings import (
    Settings,
    ENVIRONMENT,
    get_database_and_collection_name,
    create_collection,
)

app = FastAPI()
app.include_router(DNAAnalysisRouter, tags=["DNAAnalysis"], prefix="/mutant")
app.include_router(StatsRouter, tags=["Statistics"], prefix="/stats")


@app.on_event("startup")
async def startup_event():
    database, collection_name = get_database_and_collection_name(ENVIRONMENT)
    await create_collection(database, collection_name)


@lru_cache()
def get_settings():
    return Settings()
