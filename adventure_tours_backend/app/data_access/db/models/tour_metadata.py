from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data_access.db.base import Base


class TourMetadata(Base):
    __tablename__ = "tour_metadata"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    tour_id: Mapped[int] = mapped_column(ForeignKey("tours.id"), nullable=False)

    key: Mapped[str] = mapped_column(String(100), nullable=False)
    value: Mapped[str] = mapped_column(Text, nullable=False)

    tour = relationship("Tour", back_populates="metadata_items")