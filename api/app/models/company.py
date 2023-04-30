from sqlmodel import SQLModel, Field

class Company(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None, max_length=30, title="Company name")
    description: str
    mode: int = Field(ge=0, description="Mode of the company")
    rating: int = Field(ge=0, description="Rating of the company")
