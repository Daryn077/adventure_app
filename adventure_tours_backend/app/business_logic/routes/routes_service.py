from fastapi import HTTPException

from app.api.routes.routes_schema import RouteCreate, RouteUpdate
from app.data_access.db.models.route import Route
from app.data_access.routes.routes_repository import RoutesRepository


class RoutesService:
    def __init__(self, repo: RoutesRepository):
        self.repo = repo

    async def get_all_routes(self):
        return await self.repo.get_all()

    async def get_route_by_id(self, route_id: int):
        route = await self.repo.get_by_id(route_id)

        if not route:
            raise HTTPException(status_code=404, detail="Route not found")

        return route

    async def create_route(self, data: RouteCreate):
        if data.distance_km <= 0:
            raise HTTPException(status_code=400, detail="Distance must be greater than 0")

        if data.duration_hours <= 0:
            raise HTTPException(status_code=400, detail="Duration must be greater than 0")

        route = Route(**data.model_dump())
        return await self.repo.create(route)

    async def update_route(self, route_id: int, data: RouteUpdate):
        route = await self.get_route_by_id(route_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(route, key, value)

        if route.distance_km <= 0:
            raise HTTPException(status_code=400, detail="Distance must be greater than 0")

        if route.duration_hours <= 0:
            raise HTTPException(status_code=400, detail="Duration must be greater than 0")

        return await self.repo.update(route)

    async def delete_route(self, route_id: int):
        route = await self.get_route_by_id(route_id)
        await self.repo.delete(route)

        return {"message": "Route deleted successfully"}

    async def attach_route_to_tour(self, tour_id: int, route_id: int):
        tour = await self.repo.get_tour_by_id(tour_id)
        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        route = await self.get_route_by_id(route_id)

        if route in tour.routes:
            raise HTTPException(status_code=400, detail="Route already attached to this tour")

        await self.repo.attach_route_to_tour(tour, route)

        return {"message": "Route attached to tour successfully"}