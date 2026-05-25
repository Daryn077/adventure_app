from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.users.users_schema import UserRead, UserUpdate
from app.business_logic.users.users_service import UsersService
from app.data_access.db.session import get_db
from app.data_access.users.users_repository import UsersRepository
from app.utils.auth_middleware import admin_required


router = APIRouter(prefix="/users", tags=["Users"])


def get_users_service(db: AsyncSession = Depends(get_db)):
    return UsersService(UsersRepository(db))


@router.get("/")
async def get_users(
    service: UsersService = Depends(get_users_service),
    current_user: dict = Depends(admin_required)
):
    users = await service.get_all_users()

    return [
        {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role.name if user.role else "user"
        }
        for user in users
    ]


@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: int,
    service: UsersService = Depends(get_users_service),
    current_user: dict = Depends(admin_required)
):
    return await service.get_user_by_id(user_id)


@router.put("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    data: UserUpdate,
    service: UsersService = Depends(get_users_service),
    current_user: dict = Depends(admin_required)
):
    return await service.update_user(user_id, data)


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    service: UsersService = Depends(get_users_service),
    current_user: dict = Depends(admin_required)
):
    return await service.delete_user(user_id)