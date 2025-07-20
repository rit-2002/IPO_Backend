from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from helper.auth_helper import hash_password, verify_password, create_access_token
from helper.mongo import db

class SignUpRequest(BaseModel):
    email: EmailStr
    password: str
    company_name: str
    contact_name: str
    contact_number: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

router = APIRouter()

@router.post("/signup")
async def signup(data: SignUpRequest):
    user = await db.users.find_one({"email": data.email})
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    await db.users.insert_one({
        "email": data.email,
        "password": hash_password(data.password),
        "company_name": data.company_name,
        "contact_name": data.contact_name,
        "contact_number": data.contact_number
    })
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(data: LoginRequest):
    user = await db.users.find_one({"email": data.email})
    if not user or not verify_password(data.password, user['password']):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token(user['email'])
    return {"access_token": token, "token_type": "bearer"}
