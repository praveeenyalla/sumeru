from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.advisory_service import advisory_service
from app.models.domain import AdvisoryDispatchCreate, AdvisoryDispatchResponse

router = APIRouter(prefix="/advisory", tags=["Executive Advisory Dispatch"])

@router.post("/dispatch", response_model=AdvisoryDispatchResponse)
def dispatch_advisory_request(payload: AdvisoryDispatchCreate, db: Session = Depends(get_db)):
    """Dispatch strategic architectural consultation request directly into senior partner advisory queue."""
    return advisory_service.create_advisory_dispatch(payload, db)

@router.get("/status/{ticket_id}")
def get_advisory_ticket_status(ticket_id: str, db: Session = Depends(get_db)):
    """Track verification status, assigned enterprise partner, and NDA state for an advisory ticket."""
    record = advisory_service.get_ticket_status(ticket_id, db)
    if not record:
        raise HTTPException(status_code=404, detail="Advisory ticket not found")
    return record
