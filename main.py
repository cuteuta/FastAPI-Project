from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []


class Task(BaseModel):
  title: str

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/hello")
def say_hello():
    return {"message": "こんにちは"}
  
@app.get("/tasks")
def get_tasks():
  return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: Task):
  tasks.append(task)
  return {"message": "task added", "task": task}
