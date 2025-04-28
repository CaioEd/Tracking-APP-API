import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.client = MongoClient(
            os.getenv("DATABASE_URL"),
            username=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            authSource='admin'
        )
        self.db = self.client[os.getenv("DATABASE_NAME")]

    def get_db(self):
        return self.db
    
    def close(self):
        self.client.close()

database = Database() 