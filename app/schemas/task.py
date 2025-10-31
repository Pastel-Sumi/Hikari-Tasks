from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str
    created_at: datetime
    completed_at: datetime | None = None
    pomodoro_count: int = 0


