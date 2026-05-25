from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.partner import Partner
from app.data_access.db.models.tour import Tour


class PartnersRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Partner))
        return result.scalars().all()

    async def get_by_id(self, partner_id: int):
        result = await self.db.execute(select(Partner).where(Partner.id == partner_id))
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def create(self, partner: Partner):
        self.db.add(partner)
        await self.db.commit()
        await self.db.refresh(partner)
        return partner

    async def update(self, partner: Partner):
        await self.db.commit()
        await self.db.refresh(partner)
        return partner

    async def delete(self, partner: Partner):
        await self.db.delete(partner)
        await self.db.commit()

    async def attach_to_tour(self, tour: Tour, partner: Partner):
        tour.partners.append(partner)
        await self.db.commit()
        await self.db.refresh(tour)
        return tour