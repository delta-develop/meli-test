import os

from dotenv import load_dotenv
from motor import motor_asyncio
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Leonardo's MeLi test :)"
    admin_email: str = "leohg.ipn@gmail.com"

    class Config:
        env_file = ".env"


MONGO_DETAILS = os.getenv("MONGO_DETAILS")
USER = os.getenv("DBUSERNAME")
PASSWORD = os.getenv("DBPASSWORD")
ENVIRONMENT = os.getenv("ENVIRONMENT")

client = motor_asyncio.AsyncIOMotorClient(
    MONGO_DETAILS, username=USER, password=PASSWORD
)


async def create_collection(database, collection_name):
    try:
        await database.create_collection(collection_name)
    except Exception as e:
        print("Collection already exists.")


def get_database_and_collection_name(env):
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


def get_collection(database, collection_name):
    collection = database.get_collection(collection_name)
    return collection


database, collection_name = get_database_and_collection_name(ENVIRONMENT)
collection = get_collection(database, collection_name)


def drop_testing_db():
    client.drop_database("testing_dna_analysis")
