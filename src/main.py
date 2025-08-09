from fastapi import *

app = FastAPI()

@app.get("/", status_code=200)
async def root():
    return {"message": "I am alive"}