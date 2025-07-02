from fastapi import APIRouter, HTTPException
from app.models.user import UserLogin, MessageResponse
from app.database import users_collection
from app.utils.password import verify_password

router = APIRouter()

@router.post("/login", response_model=MessageResponse)
def login_user(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful"}
