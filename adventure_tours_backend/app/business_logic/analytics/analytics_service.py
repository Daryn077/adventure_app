from app.data_access.analytics.analytics_repository import AnalyticsRepository


class AnalyticsService:
    def __init__(self, repo: AnalyticsRepository):
        self.repo = repo

    async def get_tours_analytics(self):
        return await self.repo.get_tours_analytics()