from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.audit.audit_schema import AuditLogCreate, AuditLogRead
from app.business_logic.audit.audit_service import AuditService
from app.data_access.audit.audit_repository import AuditRepository
from app.data_access.db.session import get_db
from app.utils.auth_middleware import get_current_user


router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"],
    dependencies=[Depends(get_current_user)]
)


def get_audit_service(db: AsyncSession = Depends(get_db)):
    return AuditService(AuditRepository(db))


@router.get("/", response_model=list[AuditLogRead])
async def get_audit_logs(service: AuditService = Depends(get_audit_service)):
    return await service.get_all_audit_logs()


@router.post("/", response_model=AuditLogRead)
async def create_audit_log(
    data: AuditLogCreate,
    service: AuditService = Depends(get_audit_service)
):
    return await service.create_audit_log(data)