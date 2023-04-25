from fastapi import APIRouter, Depends, Request
from fastapi_microsoft_identity import requires_auth, validate_scope
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.models.company import Company

router = APIRouter()

@router.get("/companies", response_model=list[Company])
@requires_auth
async def get_companies(request: Request, session: AsyncSession = Depends(get_session)):
    validate_scope(request=request, required_scope="Data.Read")

    result = await session.execute(select(Company))
    companies = result.scalars().all()
    return companies


@router.post("/companies")
async def add_company(request: Request, company: Company, session: AsyncSession = Depends(get_session)):
    validate_scope(request=request, required_scope="Data.Write")

    company = Company(
        name=company.name,
        description=company.description,
        mode=company.mode,
        rating=company.rating)
    session.add(company)
    await session.commit()
    await session.refresh(company)
    return company
