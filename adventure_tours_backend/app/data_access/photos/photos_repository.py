from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.photo import Photo
from app.data_access.db.models.tour import Tour


class PhotosRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Photo))
        return result.scalars().all()

    async def get_by_id(self, photo_id: int):
        result = await self.db.execute(select(Photo).where(Photo.id == photo_id))
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def create(self, photo: Photo):
        self.db.add(photo)
        await self.db.commit()
        await self.db.refresh(photo)
        return photo

    async def delete(self, photo: Photo):
        await self.db.delete(photo)
        await self.db.commit()