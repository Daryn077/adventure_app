from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.equipment import Equipment


async def seed_equipment(db: AsyncSession):
    result = await db.execute(select(Equipment))
    if result.scalars().first():
        return

    equipment = [
        Equipment(name="Tent", description="Camping tent", quantity=10),
        Equipment(name="Backpack", description="Travel backpack", quantity=15),
    ]

    db.add_all(equipment)
    await db.commit()