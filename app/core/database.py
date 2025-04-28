from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

class Database:
    def __init__(self, app: FastAPI):
        self.app = app
        self.client: AsyncIOMotorClient = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient("mongodb://mongo:27017")
        self.db = self.client.routes_db

    async def disconnect(self):
        self.client.close()

db = Database(app)