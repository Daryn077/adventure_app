from fastapi import HTTPException

from app.api.participants.participants_schema import ParticipantCreate, ParticipantUpdate
from app.data_access.db.models.participant import Participant
from app.data_access.participants.participants_repository import ParticipantsRepository


class ParticipantsService:
    def __init__(self, repo: ParticipantsRepository):
        self.repo = repo

    async def get_all_participants(self):
        return await self.repo.get_all()

    async def get_participant_by_id(self, participant_id: int):
        participant = await self.repo.get_by_id(participant_id)

        if not participant:
            raise HTTPException(status_code=404, detail="Participant not found")

        return participant

    async def create_participant(self, data: ParticipantCreate):
        user = await self.repo.get_user_by_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        tour = await self.repo.get_tour_by_id(data.tour_id)
        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        existing = await self.repo.get_existing_participant(data.user_id, data.tour_id)
        if existing:
            raise HTTPException(status_code=400, detail="User already registered for this tour")

        current_count = len(tour.participants)
        if current_count >= tour.max_people:
            raise HTTPException(status_code=400, detail="Tour is full")

        participant = Participant(
            user_id=data.user_id,
            tour_id=data.tour_id,
            status="registered",
            payment_status="pending",
        )

        return await self.repo.create(participant)

    async def update_participant(self, participant_id: int, data: ParticipantUpdate):
        participant = await self.get_participant_by_id(participant_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(participant, key, value)

        return await self.repo.update(participant)

    async def delete_participant(self, participant_id: int):
        participant = await self.get_participant_by_id(participant_id)
        await self.repo.delete(participant)

        return {"message": "Participant deleted successfully"}