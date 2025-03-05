from fastapi import FastAPI 
from app.routes.item import item_router

app = FastAPI()

app.include_router(item_router)

@app.get("/")
async def root():
    return {"message":"Welcome to the FastAPI CRUD with MongoDB"}