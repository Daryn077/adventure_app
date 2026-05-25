from pydantic import BaseModel


class WeatherScheduleRequest(BaseModel):
    route_id: int
    city: str


class WeatherCompleteRequest(BaseModel):
    route_id: int
    temperature: float
    condition: str