from sqlmodel import SQLModel, Field

class Company(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    mode: int
    rating: int
