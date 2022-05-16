from __future__ import annotations
from fastapi import FastAPI
from app.routes.mutant_router import router as DNAAnalysisRouter

app = FastAPI()
app.include_router(DNAAnalysisRouter, tags=["DNAAnalysis"], prefix="/mutant")


@app.post("/")
async def read_root():

    return {"Hello": "World"}
