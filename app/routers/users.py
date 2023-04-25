from fastapi import APIRouter, Depends, Request
from fastapi_microsoft_identity import requires_auth, validate_scope
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.models.user import User

router = APIRouter()


@router.get("/users", response_model=list[User])
@requires_auth
async def get_users(request:Request, session: AsyncSession = Depends(get_session)):
    validate_scope(request=request, required_scope="Data.Read")

    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


@router.post("/users")
@requires_auth
async def add_user(request: Request, user: User, session: AsyncSession = Depends(get_session)):
    validate_scope(request=request, required_scope="Data.Write")

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
