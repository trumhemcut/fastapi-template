from typing import List
from sqlmodel import Relationship, SQLModel, Field

class Company(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    mode: int
    rating: int
    users: List["User"] = Relationship(back_populates="company")

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    username: str
    hashed_password: str
    first_name: str
    last_name: str
    is_active: bool
    is_admin: bool
    company_id: int = Field(default=None, foreign_key="company.id")
    company: Company = Relationship(back_populates="users")
    tasks: List["Task"] = Relationship(back_populates="user")

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    summary: str
    description: str
    status: int
    priority: int
    user_id: int = Field(default=None, foreign_key="user.id")
    user: User = Relationship(back_populates="tasks")