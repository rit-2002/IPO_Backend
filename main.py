from fastapi import FastAPI
from controller import auth
from helper.mongo import connect_to_mongo

app = FastAPI(on_startup=[connect_to_mongo])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
