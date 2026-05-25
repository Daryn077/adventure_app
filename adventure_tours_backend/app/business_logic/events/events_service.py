from fastapi import HTTPException

from app.api.events.events_schema import EventCreate, EventUpdate
from app.data_access.db.models.event import Event
from app.data_access.events.events_repository import EventsRepository


class EventsService:
    def __init__(self, repo: EventsRepository):
        self.repo = repo

    async def get_all_events(self):
        return await self.repo.get_all()

    async def get_event_by_id(self, event_id: int):
        event = await self.repo.get_by_id(event_id)

        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        return event

    async def create_event(self, data: EventCreate):
        tour = await self.repo.get_tour_by_id(data.tour_id)

        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        event = Event(**data.model_dump())
        return await self.repo.create(event)

    async def update_event(self, event_id: int, data: EventUpdate):
        event = await self.get_event_by_id(event_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(event, key, value)

        return await self.repo.update(event)

    async def delete_event(self, event_id: int):
        event = await self.get_event_by_id(event_id)
        await self.repo.delete(event)

        return {"message": "Event deleted successfully"}