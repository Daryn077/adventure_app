from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.logs.logs_schema import LogCreate, LogRead
from app.business_logic.logs.logs_service import LogsService
from app.data_access.db.session import get_db
from app.data_access.logs.logs_repository import LogsRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(
    prefix="/logs",
    tags=["Logs"],
    dependencies=[Depends(get_current_user)]
)


def get_logs_service(db: AsyncSession = Depends(get_db)):
    return LogsService(LogsRepository(db))


@router.get("/", response_model=list[LogRead])
async def get_logs(service: LogsService = Depends(get_logs_service)):
    return await service.get_all_logs()


@router.post("/", response_model=LogRead)
async def create_log(
    data: LogCreate,
    service: LogsService = Depends(get_logs_service)
):
    return await service.create_log(data)