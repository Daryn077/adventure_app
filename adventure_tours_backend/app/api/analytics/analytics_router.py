from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.analytics.analytics_schema import AnalyticsRead
from app.business_logic.analytics.analytics_service import AnalyticsService
from app.data_access.analytics.analytics_repository import AnalyticsRepository
from app.data_access.db.session import get_db
from app.utils.auth_middleware import get_current_user


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
    dependencies=[Depends(get_current_user)]
)


def get_analytics_service(db: AsyncSession = Depends(get_db)):
    return AnalyticsService(AnalyticsRepository(db))


@router.get("/tours", response_model=list[AnalyticsRead])
async def get_tours_analytics(
    service: AnalyticsService = Depends(get_analytics_service)
):
    return await service.get_tours_analytics()