from fastapi import APIRouter, Depends, HTTPException

from app.api.weather.weather_schema import WeatherScheduleRequest, WeatherCompleteRequest
from app.infrastructure.weather_tasks import (
    schedule_weather_update,
    get_weather_update,
    complete_weather_update,
)
from app.utils.auth_middleware import get_current_user


router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
    dependencies=[Depends(get_current_user)]
)


@router.post("/schedule")
async def schedule_weather(data: WeatherScheduleRequest):
    return await schedule_weather_update(data.route_id, data.city)


@router.get("/{route_id}")
async def get_weather(route_id: int):
    data = await get_weather_update(route_id)

    if not data:
        raise HTTPException(status_code=404, detail="Weather update not found")

    return data


@router.post("/complete")
async def complete_weather(data: WeatherCompleteRequest):
    return await complete_weather_update(
        data.route_id,
        data.temperature,
        data.condition
    )