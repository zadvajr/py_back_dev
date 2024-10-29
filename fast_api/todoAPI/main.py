""" modules import """
from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.TITLE, version=settings.VERSION)

@app.get("/", description="To do API | Home Route")
def home():
    """ home route """
    return {
        "message": "Welcome to Home Route"
    }
