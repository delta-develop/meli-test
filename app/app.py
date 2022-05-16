from __future__ import annotations
from fastapi import FastAPI, Depends
from app.routes.mutant_router import router as DNAAnalysisRouter
from app.routes.stats_router import router as StatsRouter
from functools import lru_cache
from app.settings.settings import Settings

app = FastAPI()
app.include_router(DNAAnalysisRouter, tags=["DNAAnalysis"], prefix="/mutant")
app.include_router(StatsRouter, tags=["Statistics"], prefix="/stats")


@lru_cache()
def get_settings():
    return Settings()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {"app_name": settings.app_name, "admin_email": settings.admin_email}
