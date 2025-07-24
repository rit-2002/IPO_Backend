from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from helper.auth_helper import check_db_connection
from services.user_service import get_user_by_email, create_user, get_user_by_reset_token, update_reset_token, update_user_password_by_token
from models.user_model import ChangePasswordRequest, UserSignup, UserInDB
from utils.hash import hash_password, verify_password
import uuid

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/check-db")
async def check_db():
    if await check_db_connection():
        return {"message": "Database connection successful ✅"}
    raise HTTPException(status_code=500, detail="Database connection failed ❌")

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserSignup):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed = hash_password(user.password)
    new_user = UserInDB(email=user.email, hashed_password=hashed)
    await create_user(new_user)
    return {"message": "Signup successful 🎉"}

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": f"Welcome {user['email']}! Login successful ✅"}

@router.post("/forgot-password", status_code=status.HTTP_200_OK)
async def forgot_password(email: str):
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")
    
    token = str(uuid.uuid4())
    await update_reset_token(email, token)
    return {"message": "Reset token generated", "reset_token": token}

@router.post("/reset-password", status_code=200)
async def reset_password(payload: ChangePasswordRequest):
    user = await get_user_by_reset_token(payload.reset_token)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    
    hashed_pw = hash_password(payload.new_password)
    await update_user_password_by_token(payload.reset_token, hashed_pw)
    return {"message": "Password reset successful ✅"}
