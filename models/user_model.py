from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSignup(BaseModel):
    email: EmailStr
    password: str

class UserInDB(BaseModel):
    email: EmailStr
    hashed_password: str
    reset_token: Optional[str] = None

class ChangePasswordRequest(BaseModel):
    reset_token: str
    new_password: str
