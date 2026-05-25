from pydantic import BaseModel


class EquipmentCreate(BaseModel):
    name: str
    description: str
    quantity: int = 0


class EquipmentUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    quantity: int | None = None


class EquipmentRead(BaseModel):
    id: int
    name: str
    description: str
    quantity: int

    model_config = {
        "from_attributes": True
    }