from fastapi import HTTPException

from app.api.reviews.reviews_schema import ReviewCreate, ReviewUpdate
from app.data_access.db.models.review import Review
from app.data_access.reviews.reviews_repository import ReviewsRepository


class ReviewsService:
    def __init__(self, repo: ReviewsRepository):
        self.repo = repo

    async def get_all_reviews(self):
        return await self.repo.get_all()

    async def get_review_by_id(self, review_id: int):
        review = await self.repo.get_by_id(review_id)

        if not review:
            raise HTTPException(status_code=404, detail="Review not found")

        return review

    async def create_review(self, data: ReviewCreate):
        user = await self.repo.get_user_by_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        tour = await self.repo.get_tour_by_id(data.tour_id)
        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        existing = await self.repo.get_existing_review(data.user_id, data.tour_id)
        if existing:
            raise HTTPException(status_code=400, detail="User already reviewed this tour")

        review = Review(**data.model_dump())
        return await self.repo.create(review)

    async def update_review(self, review_id: int, data: ReviewUpdate):
        review = await self.get_review_by_id(review_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(review, key, value)

        return await self.repo.update(review)

    async def delete_review(self, review_id: int):
        review = await self.get_review_by_id(review_id)
        await self.repo.delete(review)

        return {"message": "Review deleted successfully"}