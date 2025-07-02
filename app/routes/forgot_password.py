from fastapi import APIRouter, HTTPException
from app.models.user import UserForgotPassword, UserResetPassword, MessageResponse
from app.database import users_collection
from app.utils.password import hash_password

router = APIRouter()

@router.post("/forgot-password", response_model=MessageResponse)
def forgot_password(request: UserForgotPassword):
    user = users_collection.find_one({"email": request.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Reset link sent (simulated)"}

@router.post("/reset-password", response_model=MessageResponse)
def reset_password(request: UserResetPassword):
    user = users_collection.find_one({"email": request.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    users_collection.update_one(
        {"email": request.email},
        {"$set": {"password": hash_password(request.new_password)}}
    )
    return {"message": "Password reset successfully"}
