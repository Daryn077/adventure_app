from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data_access.db.base import Base
from app.data_access.db.models.associations import partner_tours


class Partner(Base):
    __tablename__ = "partners"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False)
    contact_email: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    website: Mapped[str | None] = mapped_column(String(300), nullable=True)

    tours = relationship("Tour", secondary=partner_tours, back_populates="partners")