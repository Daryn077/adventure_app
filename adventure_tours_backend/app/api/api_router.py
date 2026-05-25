from fastapi import APIRouter
from app.api.auth.auth_router import router as auth_router
from app.api.users.users_router import router as users_router
from app.api.tours.tours_router import router as tours_router
from app.api.routes.routes_router import router as routes_router
from app.api.participants.participants_router import router as participants_router
from app.api.reviews.reviews_router import router as reviews_router
from app.api.photos.photos_router import router as photos_router
from app.api.risks.risks_router import router as risks_router
from app.api.equipment.equipment_router import router as equipment_router
from app.api.partners.partners_router import router as partners_router
from app.api.events.events_router import router as events_router
from app.api.tour_metadata.tour_metadata_router import router as tour_metadata_router
from app.api.logs.logs_router import router as logs_router
from app.api.audit.audit_router import router as audit_router
from app.api.analytics.analytics_router import router as analytics_router
from app.api.weather.weather_router import router as weather_router


api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(tours_router)
api_router.include_router(routes_router)
api_router.include_router(participants_router)
api_router.include_router(reviews_router)
api_router.include_router(photos_router)
api_router.include_router(risks_router)
api_router.include_router(equipment_router)
api_router.include_router(partners_router)
api_router.include_router(events_router)
api_router.include_router(tour_metadata_router)
api_router.include_router(logs_router)
api_router.include_router(audit_router)
api_router.include_router(analytics_router)
api_router.include_router(weather_router)