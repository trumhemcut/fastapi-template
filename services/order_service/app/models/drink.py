from sqlmodel import SQLModel, Field


class Drink(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None, max_length=30, title="Drink name")
    description: str = Field(default=None, title="Description of the drink")
    price: float = Field(default=None, title="Price of the drink")
