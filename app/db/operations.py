from typing import List

from app.settings.settings import collection


async def insert_bulk_data(data_to_insert: List) -> None:
    """Insert given data package to MongoDB.

    Args:
        data_to_insert (List): Results of the DNA analysis.
    """
    try:
        await collection.insert_many(data_to_insert)
    except Exception as e:
        print("Duplicated register found")


async def get_statistics() -> dict:
    """Send to MongoDB a request to count mutants, non mutants and calculate
    the ratio between those variables.

    Returns:
        dict: Result of the calculation, may contain or not "mutants" and
        "non-mutants" field, but it will always include
        "ratio_mutants-non_mutants", even if it is null.
    """
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
                "count_mutant_dna": "$Mutants",
                "count_human_dna": "$Non-mutants",
                "ratio": {"$divide": ["$Mutants", "$Non-mutants"]},
            }
        },
    ]
    stats = collection.aggregate(pipeline)

    async for item in stats:
        result = item

    if not "count_human_dna" in result:
        result["count_human_dna"] = 0
        result["ratio"] = 0

    if not "count_mutant_dna" in result:
        result["count_mutant_dna"] = 0
        result["ratio"] = 0

    return result
