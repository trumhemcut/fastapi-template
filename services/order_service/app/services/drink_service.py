from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from ..models.drink import DrinkCreate, DrinkUpdate
from ..models.drink import Drink


async def create_drink(session: AsyncSession, drink: DrinkCreate) -> Drink:
    """Create a new drink"""
    db_drink = Drink(**drink.dict())
    session.add(db_drink)
    await session.commit()
    await session.refresh(db_drink)
    return db_drink


async def get_drink(session: AsyncSession, drink_id: str) -> Drink:
    """Get a drink by ID"""
    return await session.get(Drink, drink_id)


async def list_drinks(session: AsyncSession) -> List[Drink]:
    """List all drinks"""
    return await session.execute(select(Drink)).scalars().all()


async def update_drink(session: AsyncSession, drink_id: str, drink: DrinkUpdate) -> Drink:
    """Update a drink"""
    db_drink = await session.get(Drink, drink_id)
    for field, value in drink:
        setattr(db_drink, field, value)
    await session.commit()
    await session.refresh(db_drink)
    return db_drink


async def delete_drink(session: AsyncSession, drink_id: str) -> None:
    """Delete a drink"""
    db_drink = await session.get(Drink, drink_id)
    session.delete(db_drink)
    await session.commit()