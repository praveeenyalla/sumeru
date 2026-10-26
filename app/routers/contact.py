import datetime
import html
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.db_models import ContactInquiry

router = APIRouter(prefix="/contact", tags=["Contact Inquiries"])

class ContactInquiryRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=200, description="Full name of client")
    company: str = Field(..., min_length=2, max_length=200, description="Company name")
    business_email: EmailStr = Field(..., max_length=255, description="Business email address")
    phone: Optional[str] = Field(None, max_length=50, description="Contact phone number")
    service_interested_in: str = Field(..., min_length=2, max_length=100, description="Practice or service category")
    message: str = Field(..., min_length=5, max_length=5000, description="Scope of mandate or inquiry details")

class ContactInquiryResponse(BaseModel):
    status: str
    reference_id: str
    message: str
    received_at: str

@router.post("/submit", response_model=ContactInquiryResponse)
async def submit_inquiry(req: ContactInquiryRequest, db: Session = Depends(get_db)):
    """Receives corporate client inquiries, sanitizes inputs against XSS, and persists them securely."""
    clean_name = html.escape(req.full_name.strip())
    clean_company = html.escape(req.company.strip())
    clean_message = html.escape(req.message.strip())
    clean_service = html.escape(req.service_interested_in.strip())
    clean_phone = html.escape(req.phone.strip()) if req.phone else None

    if not clean_name or not clean_company or not clean_message:
        raise HTTPException(status_code=400, detail="Please complete all required fields.")

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    inquiry = ContactInquiry(
        full_name=clean_name,
        company=clean_company,
        business_email=str(req.business_email).strip().lower(),
        phone=clean_phone,
        service_interested_in=clean_service,
        message=clean_message,
        created_at=now_utc
    )
    db.add(inquiry)
    db.commit()
    db.refresh(inquiry)

    ref_id = f"SUM-{datetime.date.today().year}-{inquiry.id:04d}"
    
    return ContactInquiryResponse(
        status="SUCCESS",
        reference_id=ref_id,
        message="Thank you for contacting Sumeru Technologies. An enterprise engagement partner will review your inquiry within 1 business day.",
        received_at=now_utc.isoformat()
    )
