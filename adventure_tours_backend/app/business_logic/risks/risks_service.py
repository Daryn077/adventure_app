from fastapi import HTTPException

from app.api.risks.risks_schema import RiskCreate, RiskUpdate
from app.data_access.db.models.risk import Risk
from app.data_access.risks.risks_repository import RisksRepository


class RisksService:
    def __init__(self, repo: RisksRepository):
        self.repo = repo

    async def get_all_risks(self):
        return await self.repo.get_all()

    async def get_risk_by_id(self, risk_id: int):
        risk = await self.repo.get_by_id(risk_id)

        if not risk:
            raise HTTPException(status_code=404, detail="Risk not found")

        return risk

    async def create_risk(self, data: RiskCreate):
        tour = await self.repo.get_tour_by_id(data.tour_id)

        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        risk = Risk(**data.model_dump())
        return await self.repo.create(risk)

    async def update_risk(self, risk_id: int, data: RiskUpdate):
        risk = await self.get_risk_by_id(risk_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(risk, key, value)

        return await self.repo.update(risk)

    async def delete_risk(self, risk_id: int):
        risk = await self.get_risk_by_id(risk_id)
        await self.repo.delete(risk)

        return {"message": "Risk deleted successfully"}