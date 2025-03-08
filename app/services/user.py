from app.database.db import collection_users
from app.models.User import User
from .auth import hash_password, verify_password, create_access_token
from bson import ObjectId 

def serialize_user(user):
    user["_id"] = str(user["_id"])
    return user

def serialize_user_without_pass(user):
    user["_id"] = str(user["_id"])
    user.pop("password", None)
    return user

async def find_user(username: str):

    user = await collection_users.find_one({"username": username})
    if user:
        user = serialize_user(user)
        return user
    return None

async def create_user(user):
    try:
        
        hash_pass = hash_password(user.password)
        new_user = {**user.model_dump(), "password": hash_pass}
        result = await collection_users.insert_one(new_user)
        if result.inserted_id:
            new_user = await collection_users.find_one({"_id": result.inserted_id})
            new_user = serialize_user_without_pass(new_user)
            return new_user
    except:
        return None

async def verify_password_user(user: User, password: str):
    if verify_password(password, user["password"]):
        return True 
    return False

async def create_token_user(user: User):
    encoded_token = create_access_token(data={"sub": user["username"]})
    return encoded_token