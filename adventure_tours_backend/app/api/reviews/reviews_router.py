from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.reviews.reviews_schema import ReviewCreate, ReviewRead, ReviewUpdate
from app.business_logic.reviews.reviews_service import ReviewsService
from app.data_access.db.session import get_db
from app.data_access.reviews.reviews_repository import ReviewsRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/reviews", tags=["Reviews"])


def get_reviews_service(db: AsyncSession = Depends(get_db)):
    return ReviewsService(ReviewsRepository(db))


@router.get("/", response_model=list[ReviewRead])
async def get_reviews(service: ReviewsService = Depends(get_reviews_service)):
    return await service.get_all_reviews()


@router.get("/{review_id}", response_model=ReviewRead)
async def get_review(review_id: int, service: ReviewsService = Depends(get_reviews_service)):
    return await service.get_review_by_id(review_id)


@router.post("/", response_model=ReviewRead)
async def create_review(
    data: ReviewCreate,
    service: ReviewsService = Depends(get_reviews_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.create_review(data)


@router.put("/{review_id}", response_model=ReviewRead)
async def update_review(
    review_id: int,
    data: ReviewUpdate,
    service: ReviewsService = Depends(get_reviews_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.update_review(review_id, data)


@router.delete("/{review_id}")
async def delete_review(
    review_id: int,
    service: ReviewsService = Depends(get_reviews_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.delete_review(review_id)