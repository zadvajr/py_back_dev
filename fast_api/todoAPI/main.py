from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str
    description: str = ""

@app.get("/", description="Welcome: This is a simple todo list app.")
def home():
    return "Welcome: This is a simple todo list app."

@app.post("/tasks/")
def create_task(task: Task):
    tasks.append(task)
    return {
        "Message": "Task added Successfully"
    }

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/task/{task_id}")
