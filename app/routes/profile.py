from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.profile import ProfileCreate, Profile
from app.crud import profile as crud_profile
from app.database import get_db

router = APIRouter()

@router.post("/create/", response_model=Profile)
async def create_event(event: ProfileCreate, db: AsyncSession = Depends(get_db)):
    return await crud_profile.create_profile(db, event)

@router.get("/", response_model=list[Profile])
async def list_events(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud_profile.list_profiles(db, skip, limit)