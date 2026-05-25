from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.tour_metadata.tour_metadata_schema import (
    TourMetadataCreate,
    TourMetadataRead,
    TourMetadataUpdate,
)
from app.business_logic.tour_metadata.tour_metadata_service import TourMetadataService
from app.data_access.db.session import get_db
from app.data_access.tour_metadata.tour_metadata_repository import TourMetadataRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/tour-metadata", tags=["Tour Metadata"])


def get_metadata_service(db: AsyncSession = Depends(get_db)):
    return TourMetadataService(TourMetadataRepository(db))


@router.get("/", response_model=list[TourMetadataRead])
async def get_metadata(service: TourMetadataService = Depends(get_metadata_service)):
    return await service.get_all_metadata()


@router.get("/{metadata_id}", response_model=TourMetadataRead)
async def get_metadata_item(
    metadata_id: int,
    service: TourMetadataService = Depends(get_metadata_service),
):
    return await service.get_metadata_by_id(metadata_id)


@router.post("/", response_model=TourMetadataRead)
async def create_metadata(
    data: TourMetadataCreate,
    service: TourMetadataService = Depends(get_metadata_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.create_metadata(data)


@router.put("/{metadata_id}", response_model=TourMetadataRead)
async def update_metadata(
    metadata_id: int,
    data: TourMetadataUpdate,
    service: TourMetadataService = Depends(get_metadata_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.update_metadata(metadata_id, data)


@router.delete("/{metadata_id}")
async def delete_metadata(
    metadata_id: int,
    service: TourMetadataService = Depends(get_metadata_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.delete_metadata(metadata_id)