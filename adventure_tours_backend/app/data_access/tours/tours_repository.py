from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.participant import Participant
from app.data_access.db.models.review import Review
from app.data_access.db.models.tour import Tour


class ToursRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_with_stats(self):
        result = await self.db.execute(
            select(
                Tour.id,
                Tour.title,
                Tour.description,
                Tour.country,
                Tour.city,
                Tour.difficulty,
                Tour.start_date,
                Tour.end_date,
                Tour.price,
                Tour.max_people,
                Tour.image_url,
                func.coalesce(func.avg(Review.rating), 0).label("average_rating"),
                func.count(func.distinct(Participant.id)).label("participants_count"),
            )
            .outerjoin(Review, Review.tour_id == Tour.id)
            .outerjoin(Participant, Participant.tour_id == Tour.id)
            .group_by(Tour.id)
            .order_by(Tour.id)
        )

        return result.mappings().all()

    async def get_by_id_with_stats(self, tour_id: int):
        result = await self.db.execute(
            select(
                Tour.id,
                Tour.title,
                Tour.description,
                Tour.country,
                Tour.city,
                Tour.difficulty,
                Tour.start_date,
                Tour.end_date,
                Tour.price,
                Tour.max_people,
                Tour.image_url,
                func.coalesce(func.avg(Review.rating), 0).label("average_rating"),
                func.count(func.distinct(Participant.id)).label("participants_count"),
            )
            .outerjoin(Review, Review.tour_id == Tour.id)
            .outerjoin(Participant, Participant.tour_id == Tour.id)
            .where(Tour.id == tour_id)
            .group_by(Tour.id)
        )

        return result.mappings().first()

    async def get_by_id(self, tour_id: int):
        result = await self.db.execute(
            select(Tour).where(Tour.id == tour_id)
        )

        return result.scalar_one_or_none()

    async def create(self, tour: Tour):
        self.db.add(tour)
        await self.db.commit()
        await self.db.refresh(tour)

        return tour

    async def update(self, tour: Tour):
        await self.db.commit()
        await self.db.refresh(tour)

        return tour

    async def delete(self, tour: Tour):
        await self.db.delete(tour)
        await self.db.commit()