from pydantic import BaseModel


class RouteCreate(BaseModel):
    name: str
    description: str
    distance_km: float
    duration_hours: int
    start_point: str
    end_point: str
    map_url: str | None = None


class RouteUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    distance_km: float | None = None
    duration_hours: int | None = None
    start_point: str | None = None
    end_point: str | None = None
    map_url: str | None = None


class RouteRead(BaseModel):
    id: int
    name: str
    description: str
    distance_km: float
    duration_hours: int
    start_point: str
    end_point: str
    map_url: str | None = None

    model_config = {
        "from_attributes": True
    }