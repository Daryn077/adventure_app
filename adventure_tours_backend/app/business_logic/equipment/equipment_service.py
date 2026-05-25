from fastapi import HTTPException

from app.api.equipment.equipment_schema import EquipmentCreate, EquipmentUpdate
from app.data_access.db.models.equipment import Equipment
from app.data_access.equipment.equipment_repository import EquipmentRepository


class EquipmentService:
    def __init__(self, repo: EquipmentRepository):
        self.repo = repo

    async def get_all_equipment(self):
        return await self.repo.get_all()

    async def get_equipment_by_id(self, equipment_id: int):
        equipment = await self.repo.get_by_id(equipment_id)

        if not equipment:
            raise HTTPException(status_code=404, detail="Equipment not found")

        return equipment

    async def create_equipment(self, data: EquipmentCreate):
        if data.quantity < 0:
            raise HTTPException(status_code=400, detail="Quantity cannot be negative")

        equipment = Equipment(**data.model_dump())
        return await self.repo.create(equipment)

    async def update_equipment(self, equipment_id: int, data: EquipmentUpdate):
        equipment = await self.get_equipment_by_id(equipment_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(equipment, key, value)

        if equipment.quantity < 0:
            raise HTTPException(status_code=400, detail="Quantity cannot be negative")

        return await self.repo.update(equipment)

    async def delete_equipment(self, equipment_id: int):
        equipment = await self.get_equipment_by_id(equipment_id)
        await self.repo.delete(equipment)

        return {"message": "Equipment deleted successfully"}

    async def attach_equipment_to_tour(self, tour_id: int, equipment_id: int):
        tour = await self.repo.get_tour_by_id(tour_id)
        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        equipment = await self.get_equipment_by_id(equipment_id)

        if equipment in tour.equipment:
            raise HTTPException(status_code=400, detail="Equipment already attached to this tour")

        await self.repo.attach_to_tour(tour, equipment)

        return {"message": "Equipment attached to tour successfully"}