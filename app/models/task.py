from typing import List
from sqlmodel import Relationship, SQLModel, Field

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    summary: str = Field(default=None, max_length=300)
    description: str
    status: int = Field(ge=0, description="Status of the task")
    priority: int = Field(ge=0, description="Priority of the task")
    user_id: int = Field(default=None, foreign_key="user.id")
