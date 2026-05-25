from pydantic import BaseModel, EmailStr


class PartnerCreate(BaseModel):
    name: str
    contact_email: EmailStr
    phone: str | None = None
    website: str | None = None


class PartnerUpdate(BaseModel):
    name: str | None = None
    contact_email: EmailStr | None = None
    phone: str | None = None
    website: str | None = None


class PartnerRead(BaseModel):
    id: int
    name: str
    contact_email: EmailStr
    phone: str | None = None
    website: str | None = None

    model_config = {
        "from_attributes": True
    }