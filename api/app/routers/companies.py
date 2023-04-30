import logging
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi_microsoft_identity import requires_auth, validate_scope
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.models.company import Company

router = APIRouter()


@router.get("/companies", response_model=list[Company])
@requires_auth
async def get_companies(request: Request, session: AsyncSession = Depends(get_session)):
    logging.info('Validate scope')
    validate_scope(request=request, required_scope="Data.Read")

    logging.info('Getting companies')
    result = await session.execute(select(Company))
    companies = result.scalars().all()
    logging.info('Finished getting companies')
    return companies


@router.get("/companies/{company_id}", response_model=Company)
@requires_auth
async def get_companies(company_id: int, request: Request, session: AsyncSession = Depends(get_session)):
    logging.info('Validate scope')
    validate_scope(request=request, required_scope="Data.Read")

    logging.info(f'Getting a company with id: {company_id}')
    result = await session.execute(select(Company).where(Company.id == company_id))
    company = result.scalars().first()
    
    if company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    
    logging.info('Finished getting company')
    return company

@router.post("/companies", status_code=status.HTTP_201_CREATED, response_model=Company)
@requires_auth
async def add_company(request: Request, company: Company, session: AsyncSession = Depends(get_session)):
    validate_scope(request=request, required_scope="Data.Write")

    logging.info('Adding company')

    company = Company(
        name=company.name,
        description=company.description,
        mode=company.mode,
        rating=company.rating)
    session.add(company)
    await session.commit()
    await session.refresh(company)

    logging.info('Finished adding company')
    return company


@router.delete("/companies/{company_id}")
@requires_auth
async def get_companies(company_id: int, request: Request, session: AsyncSession = Depends(get_session)):
    logging.info('Validate scope')
    validate_scope(request=request, required_scope="Data.Write")

    logging.info(f'Deleting a company with id: {company_id}')
    result = await session.execute(select(Company).where(Company.id == company_id))
    company = result.scalars().first()
    
    if company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    
    await session.delete(company)
    await session.commit()
    
    logging.info('Deleted company')