from typing import List
from sqlmodel import Relationship, SQLModel, Field

from .company import Company
from .task import Task


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None, max_length=30, title="Email of the user")
    username: str = Field(default=None, max_length=30,
                          title="Username of the user")
    hashed_password: str
    first_name: str = Field(default=None, max_length=30,
                            title="User's first name")
    last_name: str = Field(default=None, max_length=30,
                           title="User's last name")
    is_active: bool
    is_admin: bool
    company_id: int = Field(default=None, foreign_key="company.id")
    company: Company = Relationship(back_populates="users")
    tasks: List["Task"] = Relationship(back_populates="user")
