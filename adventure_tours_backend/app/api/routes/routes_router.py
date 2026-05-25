from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.routes.routes_schema import RouteCreate, RouteRead, RouteUpdate
from app.business_logic.routes.routes_service import RoutesService
from app.data_access.db.session import get_db
from app.data_access.routes.routes_repository import RoutesRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/routes", tags=["Routes"])


def get_routes_service(db: AsyncSession = Depends(get_db)):
    return RoutesService(RoutesRepository(db))


@router.get("/", response_model=list[RouteRead])
async def get_routes(service: RoutesService = Depends(get_routes_service)):
    return await service.get_all_routes()


@router.get("/{route_id}", response_model=RouteRead)
async def get_route(route_id: int, service: RoutesService = Depends(get_routes_service)):
    return await service.get_route_by_id(route_id)


@router.post("/", response_model=RouteRead)
async def create_route(
    data: RouteCreate,
    service: RoutesService = Depends(get_routes_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.create_route(data)


@router.put("/{route_id}", response_model=RouteRead)
async def update_route(
    route_id: int,
    data: RouteUpdate,
    service: RoutesService = Depends(get_routes_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.update_route(route_id, data)


@router.delete("/{route_id}")
async def delete_route(
    route_id: int,
    service: RoutesService = Depends(get_routes_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.delete_route(route_id)


@router.post("/{route_id}/attach-to-tour/{tour_id}")
async def attach_route_to_tour(
    route_id: int,
    tour_id: int,
    service: RoutesService = Depends(get_routes_service),
    current_user: dict = Depends(get_current_user)
):
    return await service.attach_route_to_tour(tour_id, route_id)