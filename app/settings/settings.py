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

client = motor_asyncio.AsyncIOMotorClient(
    MONGO_DETAILS, username=USER, password=PASSWORD
)

database = client.dna_analysis

dna_results_collection = database.get_collection("dna_analysis_results")
