from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.tour import Tour
from app.data_access.db.models.review import Review
from app.data_access.db.models.participant import Participant


class AnalyticsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_tours_analytics(self):
        result = await self.db.execute(
            select(
                Tour.id.label("tour_id"),
                Tour.title.label("tour_title"),
                func.count(func.distinct(Participant.id)).label("bookings_count"),
                func.coalesce(func.avg(Review.rating), 0).label("average_rating"),
                (
                    func.count(func.distinct(Participant.id)) * Tour.price
                ).label("revenue"),
            )
            .outerjoin(Participant, Participant.tour_id == Tour.id)
            .outerjoin(Review, Review.tour_id == Tour.id)
            .group_by(Tour.id)
        )

        rows = result.mappings().all()

        return [
            {
                **row,
                "views_count": 0,
            }
            for row in rows
        ]