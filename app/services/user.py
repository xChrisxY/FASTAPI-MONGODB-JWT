from app.database.db import collection_users
from app.models.User import User
from .auth import hash_password, verify_password
from bson import ObjectId 

def serialize_user(user):
    user["_id"] = str(user["_id"])
    return user

async def find_user(username: str):
    try:
        if await collection_users.find_one({"username": username}):
            return True
        return False
    except:
        return None

async def create_user(user):
    try:
        
        hash_pass = hash_password(user.password)
        new_user = {**user.model_dump(), "password": hash_pass}
        result = await collection_users.insert_one(new_user)
        if result.inserted_id:
            new_user = await collection_users.find_one({"_id": result.inserted_id})
            new_user = serialize_user(new_user)
            return new_user
    except:
        return None

async def verify_password_user(user: User, password: str):
    if verify_password(password, user["password"]):
        return True 
    return False

async def create_token_user(user: User):
    pass