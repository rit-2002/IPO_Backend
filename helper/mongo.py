from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.ipo_db

async def connect_to_mongo():
    await db.command("ping")
    print("✅ Connected to MongoDB")
