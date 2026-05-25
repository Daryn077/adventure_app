from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data_access.db.models.log import Log


class LogsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Log).order_by(Log.id.desc()))
        return result.scalars().all()

    async def create(self, log: Log):
        self.db.add(log)
        await self.db.commit()
        await self.db.refresh(log)
        return log