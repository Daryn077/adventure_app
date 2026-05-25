from decimal import Decimal
from pydantic import BaseModel


class AnalyticsRead(BaseModel):
    tour_id: int
    tour_title: str
    views_count: int
    bookings_count: int
    average_rating: float
    revenue: Decimal