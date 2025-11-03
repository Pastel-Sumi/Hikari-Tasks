from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    

#What the client sends
class TaskCreate(TaskBase):
    status: str | None = "pending"

#Or TaskResponse, full DB output model
#What the API returns
class Task(TaskBase):
    id: int
    status: str
    created_at: datetime
    completed_at: datetime | None = None
    pomodoro_count: int = 0
    completed: bool = False


