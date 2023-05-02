import grpc
import drink_pb2
import drink_pb2_grpc

from services.drink_service import DrinkService


class DrinkServiceGrpcImp(drink_pb2_grpc.DrinkServiceServicer):
    def ListDrinks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    async def GetDrink(self, request, context):
        drink = await DrinkService().GetDrink(1)
        if (drink == None):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Drink not found!')
            raise LookupError('Drink not found!')

        return drink_pb2.Drink(id=str(drink.id), name=drink.name, description=drink.description, price=drink.price)

    def CreateDrink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDrink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDrink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
