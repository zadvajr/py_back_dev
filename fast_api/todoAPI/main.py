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

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if 0 <= task_id < len(tasks):
        return tasks[task_id]
    else:
        raise HTTPException(status_code=404, detail="Task not found!")
    
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = update_task
        return update_task
    
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if 0 <= task_id <= len(tasks):
        deleted_task = tasks.pop(task_id)
    else:
        raise HTTPException(status_code=404, detail="Task not found!")