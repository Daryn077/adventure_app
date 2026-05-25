from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.events.events_schema import EventCreate, EventRead, EventUpdate
from app.business_logic.events.events_service import EventsService
from app.data_access.db.session import get_db
from app.data_access.events.events_repository import EventsRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/events", tags=["Events"])


def get_events_service(db: AsyncSession = Depends(get_db)):
    return EventsService(EventsRepository(db))


@router.get("/", response_model=list[EventRead])
async def get_events(service: EventsService = Depends(get_events_service)):
    return await service.get_all_events()


@router.get("/{event_id}", response_model=EventRead)
async def get_event(event_id: int, service: EventsService = Depends(get_events_service)):
    return await service.get_event_by_id(event_id)


@router.post("/", response_model=EventRead)
async def create_event(
    data: EventCreate,
    service: EventsService = Depends(get_events_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.create_event(data)


@router.put("/{event_id}", response_model=EventRead)
async def update_event(
    event_id: int,
    data: EventUpdate,
    service: EventsService = Depends(get_events_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.update_event(event_id, data)


@router.delete("/{event_id}")
async def delete_event(
    event_id: int,
    service: EventsService = Depends(get_events_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.delete_event(event_id)