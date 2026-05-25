from sqlalchemy import String, Text, Integer, Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data_access.db.base import Base
from app.data_access.db.models.associations import tour_routes, tour_equipment, partner_tours


class Tour(Base):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    difficulty: Mapped[str] = mapped_column(String(50), nullable=False)
    start_date: Mapped[Date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Date] = mapped_column(Date, nullable=False)
    price: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    max_people: Mapped[int] = mapped_column(Integer, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    routes = relationship("Route", secondary=tour_routes, back_populates="tours")
    equipment = relationship("Equipment", secondary=tour_equipment, back_populates="tours")
    partners = relationship("Partner", secondary=partner_tours, back_populates="tours")

    participants = relationship("Participant", back_populates="tour")
    risks = relationship("Risk", back_populates="tour")
    reviews = relationship("Review", back_populates="tour")
    photos = relationship("Photo", back_populates="tour")
    events = relationship("Event", back_populates="tour")
    logs = relationship("Log", back_populates="tour")
    metadata_items = relationship("TourMetadata", back_populates="tour")
    analytics = relationship("Analytics", back_populates="tour")