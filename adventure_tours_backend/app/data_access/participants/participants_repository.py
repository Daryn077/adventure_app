from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.participant import Participant
from app.data_access.db.models.tour import Tour
from app.data_access.db.models.user import User


class ParticipantsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Participant))
        return result.scalars().all()

    async def get_by_id(self, participant_id: int):
        result = await self.db.execute(
            select(Participant).where(Participant.id == participant_id)
        )
        return result.scalar_one_or_none()

    async def get_user_by_id(self, user_id: int):
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def get_existing_participant(self, user_id: int, tour_id: int):
        result = await self.db.execute(
            select(Participant).where(
                Participant.user_id == user_id,
                Participant.tour_id == tour_id,
            )
        )
        return result.scalar_one_or_none()

    async def create(self, participant: Participant):
        self.db.add(participant)
        await self.db.commit()
        await self.db.refresh(participant)
        return participant

    async def update(self, participant: Participant):
        await self.db.commit()
        await self.db.refresh(participant)
        return participant

    async def delete(self, participant: Participant):
        await self.db.delete(participant)
        await self.db.commit()