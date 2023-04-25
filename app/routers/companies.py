from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.models.company import Company

router = APIRouter()


@router.get("/companies", response_model=list[Company])
async def get_companies(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Company))
    companies = result.scalars().all()
    return companies

@router.post("/companies")
async def add_company(company: Company, session: AsyncSession = Depends(get_session)):
    company = Company(
        name=company.name,
        description=company.description,
        mode=company.mode,
        rating=company.rating)
    session.add(company)
    await session.commit()
    await session.refresh(company)
    return company
