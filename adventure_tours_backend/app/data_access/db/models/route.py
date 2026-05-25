from sqlalchemy import String, Text, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data_access.db.base import Base
from app.data_access.db.models.associations import tour_routes


class Route(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    distance_km: Mapped[float] = mapped_column(Float, nullable=False)
    duration_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    start_point: Mapped[str] = mapped_column(String(200), nullable=False)
    end_point: Mapped[str] = mapped_column(String(200), nullable=False)
    map_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    tours = relationship("Tour", secondary=tour_routes, back_populates="routes")