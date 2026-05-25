class UsersService:
    def __init__(self, repository):
        self.repository = repository

    async def get_all_users(self):
        return await self.repository.get_all_users()

    async def get_user_by_id(self, user_id: int):
        return await self.repository.get_user_by_id(user_id)