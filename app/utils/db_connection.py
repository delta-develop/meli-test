from motor import motor_asyncio
import os
from app.models.person import PersonSchema
from fastapi.encoders import jsonable_encoder

MONGO_DETAILS = os.getenv("MONGO_DETAILS")


client = motor_asyncio.AsyncIOMotorClient(
    MONGO_DETAILS, username="root", password="root"
)

database = client.dna_analysis

dna_results_collection = database.get_collection("dna_analysis_results")


async def add_result(dna_data: dict, is_mutant) -> None:
    person = PersonSchema(**{"dna": dna_data, "is_mutant": is_mutant})
    person = jsonable_encoder(person)
    dna_result = await dna_results_collection.insert_one(person)


async def get_statistics() -> dict:
    ...
