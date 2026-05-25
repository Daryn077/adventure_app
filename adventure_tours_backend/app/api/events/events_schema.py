from datetime import datetime

from pydantic import BaseModel


class EventCreate(BaseModel):
    tour_id: int
    title: str
    description: str
    event_time: datetime


class EventUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    event_time: datetime | None = None


class EventRead(BaseModel):
    id: int
    tour_id: int
    title: str
    description: str
    event_time: datetime

    model_config = {
        "from_attributes": True
    }