from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.tour import Tour
from app.data_access.db.models.tour_metadata import TourMetadata


class TourMetadataRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(TourMetadata))
        return result.scalars().all()

    async def get_by_id(self, metadata_id: int):
        result = await self.db.execute(
            select(TourMetadata).where(TourMetadata.id == metadata_id)
        )
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def create(self, metadata: TourMetadata):
        self.db.add(metadata)
        await self.db.commit()
        await self.db.refresh(metadata)
        return metadata

    async def update(self, metadata: TourMetadata):
        await self.db.commit()
        await self.db.refresh(metadata)
        return metadata

    async def delete(self, metadata: TourMetadata):
        await self.db.delete(metadata)
        await self.db.commit()