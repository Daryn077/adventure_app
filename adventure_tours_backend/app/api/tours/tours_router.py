from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.tours.tours_schema import TourCreate, TourRead, TourUpdate
from app.business_logic.tours.tours_service import ToursService
from app.data_access.db.session import get_db
from app.data_access.tours.tours_repository import ToursRepository
from app.utils.auth_middleware import admin_required


router = APIRouter(prefix="/tours", tags=["Tours"])


def get_tours_service(db: AsyncSession = Depends(get_db)):
    return ToursService(ToursRepository(db))


@router.get("/", response_model=list[TourRead])
async def get_tours(
    service: ToursService = Depends(get_tours_service)
):
    return await service.get_all_tours()


@router.get("/{tour_id}", response_model=TourRead)
async def get_tour(
    tour_id: int,
    service: ToursService = Depends(get_tours_service)
):
    return await service.get_tour_by_id_with_stats(tour_id)


@router.post("/", response_model=TourRead)
async def create_tour(
    data: TourCreate,
    service: ToursService = Depends(get_tours_service),
    current_user: dict = Depends(admin_required)
):
    return await service.create_tour(data)


@router.put("/{tour_id}", response_model=TourRead)
async def update_tour(
    tour_id: int,
    data: TourUpdate,
    service: ToursService = Depends(get_tours_service),
    current_user: dict = Depends(admin_required)
):
    return await service.update_tour(tour_id, data)


@router.delete("/{tour_id}")
async def delete_tour(
    tour_id: int,
    service: ToursService = Depends(get_tours_service),
    current_user: dict = Depends(admin_required)
):
    return await service.delete_tour(tour_id)