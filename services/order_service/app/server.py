import asyncio
import grpc

from protos import drink_pb2_grpc, drink_pb2_grpc_imp
from config import settings
from logger import logger

async def serve() -> None:
    server = grpc.aio.server()

    drink_pb2_grpc.add_DrinkServiceServicer_to_server(drink_pb2_grpc_imp.DrinkServiceGrpcImp(), server)
    
    port = settings.PORT
    server.add_insecure_port(f"[::]:{port}")
    
    logger.info(f"Starting server on port {port}")
    
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())
