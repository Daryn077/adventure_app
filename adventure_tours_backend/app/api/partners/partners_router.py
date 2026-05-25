from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.partners.partners_schema import PartnerCreate, PartnerRead, PartnerUpdate
from app.business_logic.partners.partners_service import PartnersService
from app.data_access.db.session import get_db
from app.data_access.partners.partners_repository import PartnersRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/partners", tags=["Partners"])


def get_partners_service(db: AsyncSession = Depends(get_db)):
    return PartnersService(PartnersRepository(db))


@router.get("/", response_model=list[PartnerRead])
async def get_partners(service: PartnersService = Depends(get_partners_service)):
    return await service.get_all_partners()


@router.get("/{partner_id}", response_model=PartnerRead)
async def get_partner(partner_id: int, service: PartnersService = Depends(get_partners_service)):
    return await service.get_partner_by_id(partner_id)


@router.post("/", response_model=PartnerRead)
async def create_partner(
    data: PartnerCreate,
    service: PartnersService = Depends(get_partners_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.create_partner(data)


@router.put("/{partner_id}", response_model=PartnerRead)
async def update_partner(
    partner_id: int,
    data: PartnerUpdate,
    service: PartnersService = Depends(get_partners_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.update_partner(partner_id, data)


@router.delete("/{partner_id}")
async def delete_partner(
    partner_id: int,
    service: PartnersService = Depends(get_partners_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.delete_partner(partner_id)


@router.post("/{partner_id}/attach-to-tour/{tour_id}")
async def attach_partner_to_tour(
    partner_id: int,
    tour_id: int,
    service: PartnersService = Depends(get_partners_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.attach_partner_to_tour(tour_id, partner_id)