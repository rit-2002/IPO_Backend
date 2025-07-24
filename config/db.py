from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

if not MONGO_URI or not MONGO_DB:
    raise Exception("❌ Environment variables not loaded correctly")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]  # This line should work now

# Optional: create collections
async def create_collections():
    try:
        await db.create_collection("users")
    except Exception:
        pass  # Collection might already exist
