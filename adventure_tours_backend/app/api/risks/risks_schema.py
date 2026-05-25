from pydantic import BaseModel


class RiskCreate(BaseModel):
    tour_id: int
    title: str
    description: str
    level: str


class RiskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    level: str | None = None


class RiskRead(BaseModel):
    id: int
    tour_id: int
    title: str
    description: str
    level: str

    model_config = {
        "from_attributes": True
    }