from app.api.logs.logs_schema import LogCreate
from app.data_access.db.models.log import Log
from app.data_access.logs.logs_repository import LogsRepository


class LogsService:
    def __init__(self, repo: LogsRepository):
        self.repo = repo

    async def get_all_logs(self):
        return await self.repo.get_all()

    async def create_log(self, data: LogCreate):
        log = Log(**data.model_dump())
        return await self.repo.create(log)