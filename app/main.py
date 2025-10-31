from fastapi import FastAPI
from schemas.task import TaskBase

TaskBase = TaskBase

app = FastAPI()

tasks = []

@app.get("/tasks", response_model=list[TaskBase])
async def get_tasks():
    return tasks

@app.post("/tasks", response_model=TaskBase)
async def create_task(task: TaskBase):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=TaskBase)
async def update_task(task_id: int, task: TaskBase):
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    del tasks[task_id]
    return {"message": "Task deleted"}




@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

