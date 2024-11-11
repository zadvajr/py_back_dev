"""FastAPI Intro"""
#my first fastapi app

from fastapi import FastAPI

app = FastAPI()



@app.get("/", description="This is the home route", tags=["Home Route"], summary="Home Route", response_description="Success! Home Route")
def home():
    return "Welcome to my First FastAPI App"

#end
