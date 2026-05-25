from pydantic import BaseModel


class PhotoRead(BaseModel):
    id: int
    tour_id: int
    image_path: str
    caption: str | None = None

    model_config = {
        "from_attributes": True
    }