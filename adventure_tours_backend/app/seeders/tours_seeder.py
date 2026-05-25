from datetime import date
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.tour import Tour


async def seed_tours(db: AsyncSession):
    result = await db.execute(select(Tour))
    if result.scalars().first():
        return

    tours = [
        Tour(
            title="Mountain Adventure",
            description="Explore the mountains",
            country="Kazakhstan",
            city="Almaty",
            difficulty="medium",
            start_date=date(2026, 6, 1),
            end_date=date(2026, 6, 5),
            price=50000,
            max_people=10
        ),
        Tour(
            title="Desert Safari",
            description="Hot desert experience",
            country="Kazakhstan",
            city="Aktau",
            difficulty="hard",
            start_date=date(2026, 7, 10),
            end_date=date(2026, 7, 15),
            price=70000,
            max_people=8
        )
    ]

    db.add_all(tours)
    await db.commit()