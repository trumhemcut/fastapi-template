from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.models.task import Task

router = APIRouter()


@router.get("/tasks", response_model=list[Task])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task))
    tasks = result.scalars().all()
    return tasks


@router.post("/tasks")
async def add_user(task: Task, session: AsyncSession = Depends(get_session)):
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
