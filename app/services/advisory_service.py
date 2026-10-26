import hashlib
import uuid
import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.db_models import AdvisoryRequest
from app.models.domain import AdvisoryDispatchCreate, AdvisoryDispatchResponse

class AdvisoryService:
    PRACTICE_PARTNERS = {
        "sap": "S/4HANA Enterprise Architecture Lead",
        "ai": "Sovereign Intelligence & Private SLM Partner",
        "cloud": "Multi-Cloud Resiliency & GitOps Director",
        "data": "Data Fabric & Kalido MDM Practice Head",
        "audit": "Enterprise ALM & Compliance Fellow"
    }

    def create_advisory_dispatch(self, data: AdvisoryDispatchCreate, db: Session) -> AdvisoryDispatchResponse:
        # Generate clean ticket ID
        random_suffix = uuid.uuid4().hex[:5].upper()
        ticket_id = f"SUM-ADV-{datetime.datetime.now().strftime('%y%m')}-{random_suffix}"

        # Assign senior partner
        partner = self.PRACTICE_PARTNERS.get(data.focus_practice, "Senior Enterprise Architect")

        # SLA: 4 hours
        sla_hours = 4
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        target_callback = now_utc + datetime.timedelta(hours=sla_hours)

        # Cryptographic hash for mutual tamper evidence
        raw_token = f"{ticket_id}:{data.corporate_email}:{data.organization}:{now_utc.isoformat()}"
        sec_hash = hashlib.sha256(raw_token.encode()).hexdigest()[:16].upper()

        db_item = AdvisoryRequest(
            ticket_id=ticket_id,
            executive_name=data.executive_name,
            corporate_email=str(data.corporate_email),
            organization=data.organization,
            focus_practice=data.focus_practice,
            mandate_scope=data.mandate_scope or "",
            nda_requested=data.nda_requested,
            status="DISPATCHED_PENDING_REVIEW",
            assigned_partner=partner,
            response_sla_hours=sla_hours,
            security_hash=sec_hash
        )

        db.add(db_item)
        db.commit()
        db.refresh(db_item)

        return AdvisoryDispatchResponse(
            success=True,
            ticket_id=ticket_id,
            message="Mandate dispatched successfully into Sumeru Sovereign Queue.",
            assigned_partner=partner,
            response_sla_hours=sla_hours,
            target_callback_time_utc=target_callback.strftime("%Y-%m-%d %H:%M UTC"),
            security_hash=f"SHA256-{sec_hash}",
            received_at=now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
        )

    def get_ticket_status(self, ticket_id: str, db: Session):
        stmt = select(AdvisoryRequest).where(AdvisoryRequest.ticket_id == ticket_id)
        result = db.execute(stmt)
        record = result.scalars().first()
        if not record:
            return None
        return {
            "ticket_id": record.ticket_id,
            "executive_name": record.executive_name,
            "organization": record.organization,
            "focus_practice": record.focus_practice,
            "status": record.status,
            "assigned_partner": record.assigned_partner,
            "nda_requested": record.nda_requested,
            "security_hash": f"SHA256-{record.security_hash}",
            "created_at": record.created_at.strftime("%Y-%m-%d %H:%M UTC") if record.created_at else "Recent"
        }

advisory_service = AdvisoryService()
