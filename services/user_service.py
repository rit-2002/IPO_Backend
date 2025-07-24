from config.db import db
from models.user_model import UserInDB

users_collection = db["users"]

async def get_user_by_email(email: str):
    return await users_collection.find_one({"email": email})

async def create_user(user: UserInDB):
    return await users_collection.insert_one(user.dict())

async def update_reset_token(email: str, token: str):
    return await users_collection.update_one({"email": email}, {"$set": {"reset_token": token}})

async def get_user_by_reset_token(token: str):
    return await users_collection.find_one({"reset_token": token})

async def update_user_password_by_token(token: str, new_hashed_pw: str):
    await users_collection.update_one(
        {"reset_token": token},
        {"$set": {"hashed_password": new_hashed_pw}, "$unset": {"reset_token": ""}}
    )
