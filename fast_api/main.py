"""FastAPI Intro"""
#my first fastapi app

from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is the home route")
def home():
    return "Welcome to my First FastAPI App"

#end
