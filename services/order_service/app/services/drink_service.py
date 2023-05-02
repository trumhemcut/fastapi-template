from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

import database
from models.drink import Drink


class DrinkService():
    def __init__(self):
        self.session_factory = sessionmaker(
            database.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def GetDrink(self, drink_id: int):
        async with self.session_factory() as session:
            result = await session.execute(select(Drink).where(Drink.id == drink_id))
            drink = result.scalars().first()
            return drink
