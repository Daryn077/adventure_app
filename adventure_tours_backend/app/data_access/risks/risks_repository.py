from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.risk import Risk
from app.data_access.db.models.tour import Tour


class RisksRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Risk))
        return result.scalars().all()

    async def get_by_id(self, risk_id: int):
        result = await self.db.execute(select(Risk).where(Risk.id == risk_id))
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def create(self, risk: Risk):
        self.db.add(risk)
        await self.db.commit()
        await self.db.refresh(risk)
        return risk

    async def update(self, risk: Risk):
        await self.db.commit()
        await self.db.refresh(risk)
        return risk

    async def delete(self, risk: Risk):
        await self.db.delete(risk)
        await self.db.commit()