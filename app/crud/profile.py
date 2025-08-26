from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate

async def create_profile(db: AsyncSession, profile: ProfileCreate):
    db_profile = Profile(
        name=profile.name,
        description=profile.description,
        state_id=1,
    )
    db.add(db_profile)
    await db.commit()
    await db.refresh(db_profile)
    return db_profile

async def list_profiles(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Profile).offset(skip).limit(limit))
    return result.scalars().all()