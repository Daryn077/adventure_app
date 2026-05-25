from app.infrastructure.celery_app import celery_app
from app.infrastructure.redis_client import redis_client


@celery_app.task
def create_notification_task(message: str):
    redis_client.lpush("notifications", message)

    return {
        "status": "success",
        "message": message
    }