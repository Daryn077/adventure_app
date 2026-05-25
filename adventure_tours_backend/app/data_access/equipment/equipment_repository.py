from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.equipment import Equipment
from app.data_access.db.models.tour import Tour


class EquipmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Equipment))
        return result.scalars().all()

    async def get_by_id(self, equipment_id: int):
        result = await self.db.execute(
            select(Equipment).where(Equipment.id == equipment_id)
        )
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def create(self, equipment: Equipment):
        self.db.add(equipment)
        await self.db.commit()
        await self.db.refresh(equipment)
        return equipment

    async def update(self, equipment: Equipment):
        await self.db.commit()
        await self.db.refresh(equipment)
        return equipment

    async def delete(self, equipment: Equipment):
        await self.db.delete(equipment)
        await self.db.commit()

    async def attach_to_tour(self, tour: Tour, equipment: Equipment):
        tour.equipment.append(equipment)
        await self.db.commit()
        await self.db.refresh(tour)
        return tour