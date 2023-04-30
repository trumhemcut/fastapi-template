from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=20,
    max_overflow=0
)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_database_session() -> AsyncSession:
    async with async_session() as session:
        yield session