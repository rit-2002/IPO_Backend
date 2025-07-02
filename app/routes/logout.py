from fastapi import APIRouter
from app.models.user import MessageResponse

router = APIRouter()

@router.post("/logout", response_model=MessageResponse)
def logout_user():
    # In a real app, this would handle token invalidation or session cleanup
    return {"message": "Logout successful"}
