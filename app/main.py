from fastapi import FastAPI
from app.routes import login, logout, forgot_password

app = FastAPI(title="IPO Backend")

app.include_router(login.router, prefix="/auth", tags=["Login"])
app.include_router(forgot_password.router, prefix="/auth", tags=["Forgot Password"])
app.include_router(logout.router, prefix="/auth", tags=["Logout"])
