from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.user import User
from app.utils.password_hasher import hash_password


async def seed_users(db: AsyncSession):
    users_data = [
        {
            "full_name": "Zhakiya Tlegen",
            "email": "tlegen@gmail.com",
            "password": "123456",
            "role_id": 2
        },
        {
            "full_name": "Sovet Merey",
            "email": "merey@gmail.com",
            "password": "123456",
            "role_id": 1
        },
    ]

    for u in users_data:
        result = await db.execute(select(User).where(User.email == u["email"]))
        if not result.scalar_one_or_none():
            db.add(User(
                full_name=u["full_name"],
                email=u["email"],
                password_hash=hash_password(u["password"]),
                role_id=u["role_id"]
            ))

    await db.commit()