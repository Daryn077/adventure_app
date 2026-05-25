from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data_access.db.base import Base


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    tour_id: Mapped[int] = mapped_column(ForeignKey("tours.id"), nullable=False)

    status: Mapped[str] = mapped_column(String(50), default="registered")
    payment_status: Mapped[str] = mapped_column(String(50), default="pending")

    user = relationship("User", back_populates="participants")
    tour = relationship("Tour", back_populates="participants")