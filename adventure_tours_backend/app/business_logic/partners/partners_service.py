from fastapi import HTTPException

from app.api.partners.partners_schema import PartnerCreate, PartnerUpdate
from app.data_access.db.models.partner import Partner
from app.data_access.partners.partners_repository import PartnersRepository


class PartnersService:
    def __init__(self, repo: PartnersRepository):
        self.repo = repo

    async def get_all_partners(self):
        return await self.repo.get_all()

    async def get_partner_by_id(self, partner_id: int):
        partner = await self.repo.get_by_id(partner_id)

        if not partner:
            raise HTTPException(status_code=404, detail="Partner not found")

        return partner

    async def create_partner(self, data: PartnerCreate):
        partner = Partner(**data.model_dump())
        return await self.repo.create(partner)

    async def update_partner(self, partner_id: int, data: PartnerUpdate):
        partner = await self.get_partner_by_id(partner_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(partner, key, value)

        return await self.repo.update(partner)

    async def delete_partner(self, partner_id: int):
        partner = await self.get_partner_by_id(partner_id)
        await self.repo.delete(partner)

        return {"message": "Partner deleted successfully"}

    async def attach_partner_to_tour(self, tour_id: int, partner_id: int):
        tour = await self.repo.get_tour_by_id(tour_id)
        if not tour:
            raise HTTPException(status_code=404, detail="Tour not found")

        partner = await self.get_partner_by_id(partner_id)

        if partner in tour.partners:
            raise HTTPException(status_code=400, detail="Partner already attached to this tour")

        await self.repo.attach_to_tour(tour, partner)

        return {"message": "Partner attached to tour successfully"}