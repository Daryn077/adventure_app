from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.role import Role


async def seed_roles(db: AsyncSession):
    roles = ["user", "admin", "guide"]

    for role_name in roles:
        result = await db.execute(select(Role).where(Role.name == role_name))
        existing_role = result.scalar_one_or_none()

        if not existing_role:
            db.add(Role(name=role_name))

    await db.commit()