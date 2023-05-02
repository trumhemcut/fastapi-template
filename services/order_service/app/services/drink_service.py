from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.drink import Drink


async def get_drink(session: AsyncSession, drink_id: str) -> Drink:
    """Get a drink by ID"""
    return await session.get(Drink, drink_id)


async def list_drinks(session: AsyncSession) -> List[Drink]:
    """List all drinks"""
    return await session.execute(select(Drink)).scalars().all()


async def delete_drink(session: AsyncSession, drink_id: str) -> None:
    """Delete a drink"""
    db_drink = await session.get(Drink, drink_id)
    session.delete(db_drink)
    await session.commit()