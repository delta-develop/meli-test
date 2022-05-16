import os
from app.models.person import PersonSchema
from fastapi.encoders import jsonable_encoder
from app.settings.settings import MONGO_DETAILS, USER, PASSWORD, dna_results_collection


async def add_result(
    dna_data: dict, is_mutant, collection=dna_results_collection
) -> None:
    person = PersonSchema(**{"dna": dna_data, "is_mutant": is_mutant})
    person = jsonable_encoder(person)
    await collection.insert_one(person)


async def get_statistics() -> dict:
    pipeline = [
        {
            "$facet": {
                "mutants": [
                    {"$match": {"is_mutant": {"$eq": True}}},
                    {"$count": "mutants"},
                ],
                "non-mutants": [
                    {"$match": {"is_mutant": {"$eq": False}}},
                    {"$count": "non-mutants"},
                ],
            },
        },
        {
            "$project": {
                "Mutants": {"$arrayElemAt": ["$mutants.mutants", 0]},
                "Non-mutants": {"$arrayElemAt": ["$non-mutants.non-mutants", 0]},
            }
        },
        {
            "$project": {
                "mutants": "$Mutants",
                "non-mutants": "$Non-mutants",
                "ratio_mutants-non_mutants": {"$divide": ["$Mutants", "$Non-mutants"]},
            }
        },
    ]
    stats = dna_results_collection.aggregate(pipeline)

    async for item in stats:
        result = item

    return result
