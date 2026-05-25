from datetime import datetime
from pydantic import BaseModel


class AuditLogCreate(BaseModel):
    user_id: int | None = None
    entity_name: str
    entity_id: int | None = None
    action: str
    old_value: str | None = None
    new_value: str | None = None


class AuditLogRead(BaseModel):
    id: int
    user_id: int | None = None
    entity_name: str
    entity_id: int | None = None
    action: str
    old_value: str | None = None
    new_value: str | None = None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }