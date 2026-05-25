from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    user_id: int
    tour_id: int
    rating: int = Field(ge=1, le=5)
    comment: str


class ReviewUpdate(BaseModel):
    rating: int | None = Field(default=None, ge=1, le=5)
    comment: str | None = None


class ReviewRead(BaseModel):
    id: int
    user_id: int
    tour_id: int
    rating: int
    comment: str

    model_config = {
        "from_attributes": True
    }