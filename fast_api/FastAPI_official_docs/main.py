#my first fastapi file

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World FastAPI"}

@app.post("/post")
async def post():
    return {"message": "Hello World FastAPI POST"}