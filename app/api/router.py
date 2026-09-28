from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.tasks import router as tasks_router
from app.api.routes.user import router as users_router

api_router = APIRouter()


api_router.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)


api_router.include_router(
    users_router,
    prefix="/api/v1",
    tags=["Users"],
)


api_router.include_router(
    tasks_router,
    prefix="/api/v1",
    tags=["Tasks"],
)