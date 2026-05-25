from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.photos.photos_schema import PhotoRead
from app.business_logic.photos.photos_service import PhotosService
from app.data_access.db.session import get_db
from app.data_access.photos.photos_repository import PhotosRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/photos", tags=["Photos"])


def get_photos_service(db: AsyncSession = Depends(get_db)):
    return PhotosService(PhotosRepository(db))


@router.get("/", response_model=list[PhotoRead])
async def get_photos(service: PhotosService = Depends(get_photos_service)):
    return await service.get_all_photos()


@router.get("/{photo_id}", response_model=PhotoRead)
async def get_photo(photo_id: int, service: PhotosService = Depends(get_photos_service)):
    return await service.get_photo_by_id(photo_id)


@router.post("/upload", response_model=PhotoRead)
async def upload_photo(
    tour_id: int = Form(...),
    caption: str | None = Form(None),
    file: UploadFile = File(...),
    service: PhotosService = Depends(get_photos_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.upload_photo(tour_id, file, caption)


@router.delete("/{photo_id}")
async def delete_photo(
    photo_id: int,
    service: PhotosService = Depends(get_photos_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.delete_photo(photo_id)