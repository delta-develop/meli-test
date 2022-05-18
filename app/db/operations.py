from app.settings.settings import collection
import copy


async def insert_bulk_data(data_queue) -> None:
    data_to_insert = []
    while data_queue.empty() == False:
        data_to_insert.append(data_queue.get())
    try:
        await collection.insert_many(data_to_insert)
    except Exception as e:
        print("🛑🛑🛑🛑🛑🛑 duplicated 🛑🛑🛑🛑🛑🛑")


async def insert_one(data):
    await collection.insert_one(data)


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
