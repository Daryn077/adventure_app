from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class TourCreate(BaseModel):
    title: str
    description: str
    country: str
    city: str
    difficulty: str
    start_date: date
    end_date: date
    price: Decimal
    max_people: int
    image_url: str | None = None


class TourUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    country: str | None = None
    city: str | None = None
    difficulty: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    price: Decimal | None = None
    max_people: int | None = None
    image_url: str | None = None


class TourRead(BaseModel):
    id: int
    title: str
    description: str
    country: str
    city: str
    difficulty: str
    start_date: date
    end_date: date
    price: Decimal
    max_people: int
    image_url: str | None = None

    average_rating: float = 0
    participants_count: int = 0