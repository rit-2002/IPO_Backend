from fastapi import FastAPI
from controllers.auth_controller import router as auth_router

app = FastAPI(
    title="FastAPI Auth Project",
    version="1.0.0"
)

app.include_router(auth_router)
