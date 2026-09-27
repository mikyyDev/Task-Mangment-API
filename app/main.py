from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app=FastAPI(
    title=settings.app_name,
    description="Backend API for managing tasks, projects, and notes .",
    version=settings.app_version,
)


app.include_router(api_router)
@app.get("/")
async def root():
    return{
        "message": " Task managment API",
        "environment": settings.environment,
    }