from fastapi import APIRouter
from sqlalchemy import text

from app.db.session import engine

router=APIRouter()

@router.get("/health")
async def health_check():
    async with engine.connect() as conncetion:
        await conncetion.execute(text("SELECT 1"))
    return{
        "status": "health"
    }