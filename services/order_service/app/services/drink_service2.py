from sqlalchemy.ext.asyncio import AsyncSession

from app.models.drink import Drink
from app.protos.drink_pb2 import DrinkResponse, DrinksResponse
from app.protos.drink_pb2_grpc import DrinkServiceBase
from app.utils.logger import get_logger
from app.utils.mercator import mercator


logger = get_logger(__name__)


class DrinkService(DrinkServiceBase):
    # async def ListDrinks(self, request, context):
    #     logger.info("Listing all drinks...")
    #     async with pg.transaction():
    #         async with AsyncSession(pg) as session:
    #             result = await session.execute(Drink.select())
    #             drinks = [drink.to_dict() for drink in result.scalars()]
    #             drinks_response = DrinksResponse()
    #             for drink in drinks:
    #                 drinks_response.drinks.append(mercator(drink, DrinkResponse))
    #     return drinks_response

    async def GetDrink(self, request, context):
        logger.info(f"Getting drink with id {request.id}...")
        async with pg.transaction():
            async with AsyncSession(pg) as session:
                result = await session.execute(Drink.select().where(Drink.id == request.id))
                drink = result.scalar()
                if not drink:
                    context.set_code(404)
                    context.set_details("Drink not found")
                    return DrinkResponse()
                return mercator(drink.to_dict(), DrinkResponse)

    # async def CreateDrink(self, request, context):
    #     logger.info("Creating a new drink...")
    #     async with pg.transaction():
    #         async with AsyncSession(pg) as session:
    #             drink = Drink(**request.dict())
    #             session.add(drink)
    #             await session.flush()
    #             return mercator(drink.to_dict(), DrinkResponse)

    # async def UpdateDrink(self, request, context):
    #     logger.info(f"Updating drink with id {request.id}...")
    #     async with pg.transaction():
    #         async with AsyncSession(pg) as session:
    #             result = await session.execute(Drink.select().where(Drink.id == request.id))
    #             drink = result.scalar()
    #             if not drink:
    #                 context.set_code(404)
    #                 context.set_details("Drink not found")
    #                 return DrinkResponse()
    #             for field, value in request.dict(exclude_unset=True).items():
    #                 setattr(drink, field, value)
    #             await session.flush()
    #             return mercator(drink.to_dict(), DrinkResponse)

    # async def DeleteDrink(self, request, context):
    #     logger.info(f"Deleting drink with id {request.id}...")
    #     async with pg.transaction():
    #         async with AsyncSession(pg) as session:
    #             result = await session.execute(Drink.select().where(Drink.id == request.id))
    #             drink = result.scalar()
    #             if not drink:
    #                 context.set_code(404)
    #                 context.set_details("Drink not found")
    #                 return DrinkResponse()
    #             session.delete(drink)
    #             return mercator(drink.to_dict(), DrinkResponse)