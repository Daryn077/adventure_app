import asyncio

from app.data_access.db.session import AsyncSessionLocal

from app.seeders.roles_seeder import seed_roles
from app.seeders.users_seeder import seed_users
from app.seeders.tours_seeder import seed_tours
from app.seeders.routes_seeder import seed_routes
from app.seeders.equipment_seeder import seed_equipment
from app.seeders.partners_seeder import seed_partners


async def main():
    async with AsyncSessionLocal() as db:
        await seed_roles(db)
        await seed_users(db)
        await seed_tours(db)
        await seed_routes(db)
        await seed_equipment(db)
        await seed_partners(db)

    print("🔥 Seeders completed successfully")


if __name__ == "__main__":
    asyncio.run(main())