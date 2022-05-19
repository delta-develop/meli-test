from typing import List
from app.settings.settings import collection
from app.utils.queue import MongoQueue


async def insert_bulk_data(data_to_insert: MongoQueue) -> None:
    try:
        await collection.insert_many(data_to_insert)
    except Exception as e:
        print("🛑🛑🛑🛑🛑🛑 duplicated 🛑🛑🛑🛑🛑🛑")


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
    stats = collection.aggregate(pipeline)

    async for item in stats:
        result = item

    return result
