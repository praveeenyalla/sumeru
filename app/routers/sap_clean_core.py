from fastapi import APIRouter
from typing import List, Dict, Any
from app.services.clean_core_service import clean_core_service
from app.models.domain import CleanCoreAuditRequest, CleanCoreAuditResponse

router = APIRouter(prefix="/sap", tags=["SAP Clean Core Center of Excellence"])

@router.get("/tiers", response_model=List[Dict[str, Any]])
async def get_clean_core_tiers():
    """Retrieve the 5-tier SAP Clean Core architectural hierarchy."""
    return clean_core_service.get_tiers()

@router.post("/audit", response_model=CleanCoreAuditResponse)
async def perform_clean_core_audit(payload: CleanCoreAuditRequest):
    """Calculate Clean Core index, technical debt level, and migration pathway recommendations."""
    return clean_core_service.evaluate_clean_core(payload)
