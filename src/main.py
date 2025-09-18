from fastapi import *
from src.infrastructure.database import *
from src.entities import todo

app = FastAPI()

todo.Base.metadata.create_all(bind=engine)

@app.get("/", status_code=200)
async def root():
    return {"message": "I am alive"}

@app.get("/get_all_todos", status_code=200)
async def get_all_todos():
    return {"message": "I am alive"}

@app.get("v1/get_all_todos", status_code=200)
async def get_all_todos():
    return {"message": "I am alive"}