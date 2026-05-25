from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.risks.risks_schema import RiskCreate, RiskRead, RiskUpdate
from app.business_logic.risks.risks_service import RisksService
from app.data_access.db.session import get_db
from app.data_access.risks.risks_repository import RisksRepository
from app.utils.auth_middleware import get_current_user


router = APIRouter(prefix="/risks", tags=["Risks"])


def get_risks_service(db: AsyncSession = Depends(get_db)):
    return RisksService(RisksRepository(db))


@router.get("/", response_model=list[RiskRead])
async def get_risks(service: RisksService = Depends(get_risks_service)):
    return await service.get_all_risks()


@router.get("/{risk_id}", response_model=RiskRead)
async def get_risk(risk_id: int, service: RisksService = Depends(get_risks_service)):
    return await service.get_risk_by_id(risk_id)


@router.post("/", response_model=RiskRead)
async def create_risk(
    data: RiskCreate,
    service: RisksService = Depends(get_risks_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.create_risk(data)


@router.put("/{risk_id}", response_model=RiskRead)
async def update_risk(
    risk_id: int,
    data: RiskUpdate,
    service: RisksService = Depends(get_risks_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.update_risk(risk_id, data)


@router.delete("/{risk_id}")
async def delete_risk(
    risk_id: int,
    service: RisksService = Depends(get_risks_service),
    current_user: dict = Depends(get_current_user),
):
    return await service.delete_risk(risk_id)