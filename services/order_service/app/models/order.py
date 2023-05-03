from sqlmodel import Relationship, SQLModel, Field

from models import Drink


class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    customer_name: str = Field(
        default=None, max_length=50, title="Customer name")
    customer_phone: str = Field(
        default=None, max_length=50, title="Customer phone")
    customer_email: str = Field(
        default=None, max_length=50, title="Customer email")
    quantity: int = Field(default=None, title="Quantity")
    total_price: float = Field(default=None, title="Total price")
    drink_id: int = Field(default=None, foreign_key="drink.id")
    drink: Drink = Relationship(back_populates="orders")
