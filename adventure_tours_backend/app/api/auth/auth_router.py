from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.auth_schema import RegisterSchema, LoginSchema
from app.business_logic.auth.auth_service import AuthService
from app.data_access.auth.auth_repository import AuthRepository
from app.data_access.db.session import get_db
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/auth", tags=["Auth"])


def get_auth_service(db: AsyncSession = Depends(get_db)):
    return AuthService(AuthRepository(db))


@router.post("/register")
async def register(
    data: RegisterSchema,
    service: AuthService = Depends(get_auth_service)
):
    return await service.register(
        data.full_name,
        data.email,
        data.password
    )


@router.post("/login")
async def login(
    data: LoginSchema,
    service: AuthService = Depends(get_auth_service)
):
    return await service.login(data.email, data.password)


@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return {
        "user_id": current_user["user_id"],
        "email": current_user["email"],
        "role": current_user["role"],
    }