from app.api.audit.audit_schema import AuditLogCreate
from app.data_access.audit.audit_repository import AuditRepository
from app.data_access.db.models.audit_log import AuditLog


class AuditService:
    def __init__(self, repo: AuditRepository):
        self.repo = repo

    async def get_all_audit_logs(self):
        return await self.repo.get_all()

    async def create_audit_log(self, data: AuditLogCreate):
        audit_log = AuditLog(**data.model_dump())
        return await self.repo.create(audit_log)