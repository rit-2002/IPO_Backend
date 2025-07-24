from config.db import db

async def check_db_connection() -> bool:
    try:
        await db.command("ping")
        return True
    except Exception:
        return False
