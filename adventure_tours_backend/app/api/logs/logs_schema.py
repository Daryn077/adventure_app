from datetime import datetime
from pydantic import BaseModel


class LogCreate(BaseModel):
    tour_id: int | None = None
    action: str
    message: str


class LogRead(BaseModel):
    id: int
    tour_id: int | None = None
    action: str
    message: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }