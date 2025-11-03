from fastapi import FastAPI, HTTPException
from schemas.task import TaskBase, TaskCreate, Task
from datetime import datetime 

app = FastAPI()

tasks = {}
current_id = 0

@app.get("/tasks", response_model=list[Task])
async def get_tasks():
    return list(tasks.values())

@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    global current_id
    current_id += 1
    new_task = Task(id=current_id,
                    title= task.title,
                    description= task.description,
                    status = task.status or "pending",
                    created_at = datetime.now(),
                    completed_at = None,
                    pomodoro_count=0,
                    completed=False
                    )
    
    tasks[new_task.id] = new_task
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    updated_task = Task(id=task_id, **task.dict())
    tasks[task_id] = updated_task
    return updated_task

# Mark a task as completed
@app.patch("/tasks/{task_id}/complete", response_model=Task)
async def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks[task_id]
    updated = task.copy(update={"completed": True})
    tasks[task_id] = updated
    return updated

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del tasks[task_id]
    return {"message": "Task deleted"}
