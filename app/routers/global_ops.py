from fastapi import APIRouter
from app.services.global_sync_service import global_sync_service

router = APIRouter(prefix="/global", tags=["Global Follow-the-Sun Operations"])

@router.get("/sync-status")
async def get_global_sync_status():
    """Retrieve continuous 24-hour follow-the-sun synchronized hub metrics across US, UK, and India."""
    return global_sync_service.get_sync_status()
