from pydantic import BaseModel


class ParticipantCreate(BaseModel):
    user_id: int
    tour_id: int


class ParticipantUpdate(BaseModel):
    status: str | None = None
    payment_status: str | None = None


class ParticipantRead(BaseModel):
    id: int
    user_id: int
    tour_id: int
    status: str
    payment_status: str

    model_config = {
        "from_attributes": True
    }