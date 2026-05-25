from fastapi import HTTPException, UploadFile

from app.data_access.db.models.photo import Photo
from app.data_access.photos.photos_repository import PhotosRepository
from app.utils.file_uploader import save_upload_file


class PhotosService:
    def __init__(self, repo: PhotosRepository):
        self.repo = repo

    async def get_all_photos(self):
        return await self.repo.get_all()

    async def get_photo_by_id(self, photo_id: int):
        photo = await self.repo.get_by_id(photo_id)

        if not photo:
            raise HTTPException(status_code=404, detail="Photo not found")

        return photo

    async def upload_photo(self, tour_id: int, file: UploadFile, caption: str | None):
        tour = await self.repo.get_tour_by_id(tour_id)

        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        image_path = await save_upload_file(file)

        photo = Photo(
            tour_id=tour_id,
            image_path=image_path,
            caption=caption,
        )

        return await self.repo.create(photo)

    async def delete_photo(self, photo_id: int):
        photo = await self.get_photo_by_id(photo_id)
        await self.repo.delete(photo)

        return {"message": "Photo deleted successfully"}