import os
from typing import Any, Optional, Tuple

from dotenv import load_dotenv
from motor import motor_asyncio
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Leonardo's MeLi test :)"
    admin_email: str = "leohg.ipn@gmail.com"

    class Config:
        env_file = ".env"


MONGO_HOST = "mongodb://" + os.getenv("MONGO_HOST", "127.0.0.1")
MONGO_PORT = os.getenv("MONGO_PORT")
DBUSER = os.getenv("DBUSERNAME")
DBPWD = os.getenv("DBPASSWORD")
ENVIRONMENT = os.getenv("ENVIRONMENT")
EMPTYING_TIME = int(os.getenv("EMPTYING_TIME", "27017"))
MAX_QUEUE_SIZE = int(os.getenv("MAX_QUEUE_SIZE", "500"))

client = motor_asyncio.AsyncIOMotorClient(
    host=MONGO_HOST, port=int(MONGO_PORT), username=DBUSER, password=DBPWD
)


async def create_collection(database: Any, collection_name: str) -> None:
    """At the start of the application, check if the needed collection exists,
    create it if not.

    Args:
        database (Any): Database to look for the collection
        collection_name (str): Name that our collection will have.
    """
    try:
        await database.create_collection(collection_name)
    except Exception as e:
        print("Collection already exists.")


def get_database_and_collection_name(env: Optional[str]) -> Tuple[Any, str]:
    """Based on .env file, give the name of collection and create a database
    to store the results.

    Args:
        env (Optional[str]): Environment variable value.

    Returns:
        Tuple[Any, str]: Database object and collection name.
    """
    if env == "PROD":
        database = client.prod_dna_analysis
        collection_name = "prod_dna_results"
    elif env == "TESTING":
        database = client.testing_dna_analysis
        collection_name = "testing_dna_results"
    else:
        database = client.dev_dna_analysis
        collection_name = "dev_dna_results"

    return database, collection_name


def get_collection(database: Any, collection_name: str) -> Any:
    """After creating it, we need to match the collection object against
    it counterpart in MongoDB


    Args:
        database (Any): Database object.
        collection_name (str): Name of the recently created collection.

    Returns:
        Any: Collection object to perform operations.
    """
    collection = database.get_collection(collection_name)
    return collection


database, collection_name = get_database_and_collection_name(ENVIRONMENT)
collection = get_collection(database, collection_name)


def drop_testing_db():
    client.drop_database("testing_dna_analysis")
