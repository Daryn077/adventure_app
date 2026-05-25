from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.participants.participants_schema import (
    ParticipantCreate,
    ParticipantRead,
    ParticipantUpdate,
)
from app.business_logic.participants.participants_service import ParticipantsService
from app.data_access.db.session import get_db
from app.data_access.participants.participants_repository import ParticipantsRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(
    prefix="/participants",
    tags=["Participants"],
    dependencies=[Depends(get_current_user)]
)


def get_participants_service(db: AsyncSession = Depends(get_db)):
    return ParticipantsService(ParticipantsRepository(db))


@router.get("/", response_model=list[ParticipantRead])
async def get_participants(service: ParticipantsService = Depends(get_participants_service)):
    return await service.get_all_participants()


@router.get("/{participant_id}", response_model=ParticipantRead)
async def get_participant(
    participant_id: int,
    service: ParticipantsService = Depends(get_participants_service)
):
    return await service.get_participant_by_id(participant_id)


@router.post("/", response_model=ParticipantRead)
async def create_participant(
    data: ParticipantCreate,
    service: ParticipantsService = Depends(get_participants_service)
):
    return await service.create_participant(data)


@router.put("/{participant_id}", response_model=ParticipantRead)
async def update_participant(
    participant_id: int,
    data: ParticipantUpdate,
    service: ParticipantsService = Depends(get_participants_service)
):
    return await service.update_participant(participant_id, data)


@router.delete("/{participant_id}")
async def delete_participant(
    participant_id: int,
    service: ParticipantsService = Depends(get_participants_service)
):
    return await service.delete_participant(participant_id)