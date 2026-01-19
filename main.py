from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 仮のデータ保存場所
tasks = []
next_id = 1


class TaskCreate(BaseModel):
    title: str


class Task(BaseModel):
    id: int
    title: str


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(task: TaskCreate):
    global next_id
    new_task = {
        "id": next_id,
        "title": task.title
    }
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
