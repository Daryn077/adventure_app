from pydantic import BaseModel


class TourMetadataCreate(BaseModel):
    tour_id: int
    key: str
    value: str


class TourMetadataUpdate(BaseModel):
    key: str | None = None
    value: str | None = None


class TourMetadataRead(BaseModel):
    id: int
    tour_id: int
    key: str
    value: str

    model_config = {
        "from_attributes": True
    }