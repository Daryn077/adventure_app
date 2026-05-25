from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.route import Route
from app.data_access.db.models.tour import Tour


class RoutesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Route))
        return result.scalars().all()

    async def get_by_id(self, route_id: int):
        result = await self.db.execute(select(Route).where(Route.id == route_id))
        return result.scalar_one_or_none()

    async def get_tour_by_id(self, tour_id: int):
        result = await self.db.execute(select(Tour).where(Tour.id == tour_id))
        return result.scalar_one_or_none()

    async def create(self, route: Route):
        self.db.add(route)
        await self.db.commit()
        await self.db.refresh(route)
        return route

    async def update(self, route: Route):
        await self.db.commit()
        await self.db.refresh(route)
        return route

    async def delete(self, route: Route):
        await self.db.delete(route)
        await self.db.commit()

    async def attach_route_to_tour(self, tour: Tour, route: Route):
        tour.routes.append(route)
        await self.db.commit()
        await self.db.refresh(tour)
        return tour