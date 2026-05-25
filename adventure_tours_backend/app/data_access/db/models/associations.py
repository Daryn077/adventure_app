from sqlalchemy import Table, Column, ForeignKey

from app.data_access.db.base import Base


tour_routes = Table(
    "tour_routes",
    Base.metadata,
    Column("tour_id", ForeignKey("tours.id"), primary_key=True),
    Column("route_id", ForeignKey("routes.id"), primary_key=True),
)

tour_equipment = Table(
    "tour_equipment",
    Base.metadata,
    Column("tour_id", ForeignKey("tours.id"), primary_key=True),
    Column("equipment_id", ForeignKey("equipment.id"), primary_key=True),
)

partner_tours = Table(
    "partner_tours",
    Base.metadata,
    Column("partner_id", ForeignKey("partners.id"), primary_key=True),
    Column("tour_id", ForeignKey("tours.id"), primary_key=True),
)