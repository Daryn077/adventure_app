from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.route import Route


async def seed_routes(db: AsyncSession):
    result = await db.execute(select(Route))
    if result.scalars().first():
        return

    routes = [
        Route(
            name="Mountain Trail",
            description="Rocky mountain path",
            distance_km=12.5,
            duration_hours=6,
            start_point="Base Camp",
            end_point="Peak"
        ),
        Route(
            name="Desert Route",
            description="Sandy desert trail",
            distance_km=20,
            duration_hours=8,
            start_point="Oasis",
            end_point="Dunes"
        )
    ]

    db.add_all(routes)
    await db.commit()