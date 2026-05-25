from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.review import Review
from app.data_access.db.models.tour import Tour
from app.data_access.db.models.user import User


class ReviewsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Review))
        return result.scalars().all()

    async def get_by_id(self, review_id: int):
        result = await self.db.execute(select(Review).where(Review.id == review_id))
        return result.scalar_one_or_none()

    async def get_user_by_id(self, user_id: int):
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def get_existing_review(self, user_id: int, tour_id: int):
        result = await self.db.execute(
            select(Review).where(
                Review.user_id == user_id,
                Review.tour_id == tour_id,
            )
        )
        return result.scalar_one_or_none()

    async def create(self, review: Review):
        self.db.add(review)
        await self.db.commit()
        await self.db.refresh(review)
        return review

    async def update(self, review: Review):
        await self.db.commit()
        await self.db.refresh(review)
        return review

    async def delete(self, review: Review):
        await self.db.delete(review)
        await self.db.commit()