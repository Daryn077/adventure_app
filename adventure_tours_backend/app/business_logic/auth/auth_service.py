from fastapi import HTTPException

from app.data_access.auth.auth_repository import AuthRepository
from app.data_access.db.models.user import User
from app.utils.password_hasher import hash_password, verify_password
from app.utils.token_creator import create_access_token


class AuthService:

    def __init__(self, repo: AuthRepository):
        self.repo = repo

    async def register(self, full_name: str, email: str, password: str):
        existing = await self.repo.get_user_by_email(email)

        if existing:
            raise HTTPException(status_code=400, detail="User already exists")

        user = User(
            full_name=full_name,
            email=email,
            password_hash=hash_password(password),
            role_id=1
        )

        return await self.repo.create_user(user)

    async def login(self, email: str, password: str):
        user = await self.repo.get_user_by_email(email)

        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        role_name = user.role.name if user.role else None

        token = create_access_token({
            "user_id": user.id,
            "email": user.email,
            "role": role_name
        })

        return {
            "access_token": token,
            "token_type": "bearer",
            "role": role_name
        }