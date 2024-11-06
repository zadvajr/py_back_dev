from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is my home route", deprecated=True)
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}