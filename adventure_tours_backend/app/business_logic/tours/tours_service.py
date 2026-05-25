from fastapi import HTTPException

from app.api.notifications.connection_manager import notification_manager
from app.api.tours.tours_schema import TourCreate, TourUpdate
from app.data_access.db.models.tour import Tour
from app.data_access.tours.tours_repository import ToursRepository
from app.infrastructure.tasks import create_notification_task


class ToursService:
    def __init__(self, repo: ToursRepository):
        self.repo = repo

    async def get_all_tours(self):
        return await self.repo.get_all_with_stats()

    async def get_tour_by_id_with_stats(self, tour_id: int):
        tour = await self.repo.get_by_id_with_stats(tour_id)

        if not tour:
            raise HTTPException(
                status_code=404,
                detail="Tour not found"
            )

        return tour

    async def get_tour_by_id(self, tour_id: int):
        tour = await self.repo.get_by_id(tour_id)

        if not tour:
            raise HTTPException(
                status_code=404,
                detail="Tour not found"
            )

        return tour

    async def create_tour(self, data: TourCreate):
        if data.end_date < data.start_date:
            raise HTTPException(
                status_code=400,
                detail="End date cannot be earlier than start date"
            )

        tour = Tour(**data.model_dump())
        created_tour = await self.repo.create(tour)

        message = f"New tour created: {created_tour.title}"

        create_notification_task.delay(message)
        await notification_manager.broadcast(message)

        return created_tour

    async def update_tour(self, tour_id: int, data: TourUpdate):
        tour = await self.get_tour_by_id(tour_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(tour, key, value)

        if tour.end_date < tour.start_date:
            raise HTTPException(
                status_code=400,
                detail="End date cannot be earlier than start date"
            )

        updated_tour = await self.repo.update(tour)

        message = f"Tour updated: {updated_tour.title}"

        create_notification_task.delay(message)
        await notification_manager.broadcast(message)

        return updated_tour

    async def delete_tour(self, tour_id: int):
        tour = await self.get_tour_by_id(tour_id)
        tour_title = tour.title

        await self.repo.delete(tour)

        message = f"Tour deleted: {tour_title}"

        create_notification_task.delay(message)
        await notification_manager.broadcast(message)

        return {
            "message": "Tour deleted successfully"
        }