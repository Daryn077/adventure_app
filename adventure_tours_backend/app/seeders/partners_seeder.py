from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.partner import Partner


async def seed_partners(db: AsyncSession):
    result = await db.execute(select(Partner))
    if result.scalars().first():
        return

    partners = [
        Partner(name="Nomad Travel", contact_email="nomad@test.com"),
        Partner(name="Adventure Co", contact_email="adventure@test.com"),
    ]

    db.add_all(partners)
    await db.commit()