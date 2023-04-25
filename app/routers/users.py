from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.models.user import User

router = APIRouter()


@router.get("/users", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


@router.post("/users")
async def add_user(user: User, session: AsyncSession = Depends(get_session)):
    user = User(
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_active=user.is_active,
        is_admin=user.is_admin,
        hashed_password=user.hashed_password,
        company_id=user.company_id
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
