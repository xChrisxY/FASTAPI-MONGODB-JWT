from motor.motor_asyncio import  AsyncIOMotorClient 
from app.database.config import MONGO_URI, PORT, COLLECTION_NAME, COLLECTION_USERS, DATABASE_NAME

MONGO_URI = f"{MONGO_URI}:{PORT}"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
collection_users = db[COLLECTION_USERS]