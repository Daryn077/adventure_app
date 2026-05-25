from fastapi import HTTPException

from app.api.tour_metadata.tour_metadata_schema import TourMetadataCreate, TourMetadataUpdate
from app.data_access.db.models.tour_metadata import TourMetadata
from app.data_access.tour_metadata.tour_metadata_repository import TourMetadataRepository


class TourMetadataService:
    def __init__(self, repo: TourMetadataRepository):
        self.repo = repo

    async def get_all_metadata(self):
        return await self.repo.get_all()

    async def get_metadata_by_id(self, metadata_id: int):
        metadata = await self.repo.get_by_id(metadata_id)

        if not metadata:
            raise HTTPException(status_code=404, detail="Metadata not found")

        return metadata

    async def create_metadata(self, data: TourMetadataCreate):
        tour = await self.repo.get_tour_by_id(data.tour_id)

        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        metadata = TourMetadata(**data.model_dump())
        return await self.repo.create(metadata)

    async def update_metadata(self, metadata_id: int, data: TourMetadataUpdate):
        metadata = await self.get_metadata_by_id(metadata_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(metadata, key, value)

        return await self.repo.update(metadata)

    async def delete_metadata(self, metadata_id: int):
        metadata = await self.get_metadata_by_id(metadata_id)
        await self.repo.delete(metadata)

        return {"message": "Metadata deleted successfully"}