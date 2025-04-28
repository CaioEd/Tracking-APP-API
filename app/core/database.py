from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

MONGO_URI = f"mongodb://{DB_USER}:{DB_PASSWORD}@localhost:27017"  

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database()  
