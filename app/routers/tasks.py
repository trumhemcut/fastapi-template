from fastapi import APIRouter, Depends, Request
from fastapi_microsoft_identity import requires_auth, validate_scope
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.models.task import Task

router = APIRouter()


@router.get("/tasks", response_model=list[Task])
@requires_auth
async def get_users(request: Request, session: AsyncSession = Depends(get_session)):
    validate_scope(request=request, required_scope="Data.Read")

    result = await session.execute(select(Task))
    tasks = result.scalars().all()
    return tasks


@router.post("/tasks")
@requires_auth
async def add_user(request: Request, task: Task, session: AsyncSession = Depends(get_session)):
    validate_scope(request=request, required_scope="Data.Write")
    task = Task(
        description=task.description,
        priority=task.priority,
        status=task.status,
        summary=task.summary,
        user_id=task.user_id,
    )
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task
