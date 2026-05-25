from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data_access.db.base import Base


class Analytics(Base):
    __tablename__ = "analytics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    tour_id: Mapped[int] = mapped_column(ForeignKey("tours.id"), nullable=False)

    views_count: Mapped[int] = mapped_column(Integer, default=0)
    bookings_count: Mapped[int] = mapped_column(Integer, default=0)
    average_rating: Mapped[float] = mapped_column(Numeric(3, 2), default=0)
    revenue: Mapped[float] = mapped_column(Numeric(10, 2), default=0)

    tour = relationship("Tour", back_populates="analytics")