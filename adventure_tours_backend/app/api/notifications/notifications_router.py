from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.infrastructure.redis_client import redis_client
from app.api.notifications.connection_manager import notification_manager


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get("/")
async def get_notifications():
    notifications = redis_client.lrange("notifications", 0, 20)
    return notifications


@router.websocket("/ws")
async def notifications_websocket(websocket: WebSocket):
    await notification_manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        notification_manager.disconnect(websocket)