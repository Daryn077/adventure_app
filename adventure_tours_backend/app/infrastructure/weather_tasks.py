import json
from datetime import datetime

from app.infrastructure.redis_client import redis_client


async def schedule_weather_update(route_id: int, city: str):
    key = f"weather_update:{route_id}"

    data = {
        "route_id": route_id,
        "city": city,
        "status": "scheduled",
        "created_at": datetime.utcnow().isoformat()
    }

    await redis_client.set(key, json.dumps(data), ex=3600)

    return data


async def get_weather_update(route_id: int):
    key = f"weather_update:{route_id}"

    data = await redis_client.get(key)

    if not data:
        return None

    return json.loads(data)


async def complete_weather_update(route_id: int, temperature: float, condition: str):
    key = f"weather_update:{route_id}"

    data = {
        "route_id": route_id,
        "temperature": temperature,
        "condition": condition,
        "status": "completed",
        "updated_at": datetime.utcnow().isoformat()
    }

    await redis_client.set(key, json.dumps(data), ex=3600)

    return data