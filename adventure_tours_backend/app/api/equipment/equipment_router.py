from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.equipment.equipment_schema import EquipmentCreate, EquipmentRead, EquipmentUpdate
from app.business_logic.equipment.equipment_service import EquipmentService
from app.data_access.db.session import get_db
from app.data_access.equipment.equipment_repository import EquipmentRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/equipment", tags=["Equipment"])


def get_equipment_service(db: AsyncSession = Depends(get_db)):
    return EquipmentService(EquipmentRepository(db))


@router.get("/", response_model=list[EquipmentRead])
async def get_equipment(service: EquipmentService = Depends(get_equipment_service)):
    return await service.get_all_equipment()


@router.get("/{equipment_id}", response_model=EquipmentRead)
async def get_equipment_item(
    equipment_id: int,
    service: EquipmentService = Depends(get_equipment_service)
):
    return await service.get_equipment_by_id(equipment_id)


@router.post("/", response_model=EquipmentRead)
async def create_equipment(
    data: EquipmentCreate,
    service: EquipmentService = Depends(get_equipment_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.create_equipment(data)


@router.put("/{equipment_id}", response_model=EquipmentRead)
async def update_equipment(
    equipment_id: int,
    data: EquipmentUpdate,
    service: EquipmentService = Depends(get_equipment_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.update_equipment(equipment_id, data)


@router.delete("/{equipment_id}")
async def delete_equipment(
    equipment_id: int,
    service: EquipmentService = Depends(get_equipment_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.delete_equipment(equipment_id)


@router.post("/{equipment_id}/attach-to-tour/{tour_id}")
async def attach_equipment_to_tour(
    equipment_id: int,
    tour_id: int,
    service: EquipmentService = Depends(get_equipment_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.attach_equipment_to_tour(tour_id, equipment_id)