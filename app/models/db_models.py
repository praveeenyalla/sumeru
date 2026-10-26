import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.database import Base

def utc_now():
    return datetime.datetime.now(datetime.timezone.utc)

class AdvisoryRequest(Base):
    __tablename__ = "advisory_requests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ticket_id = Column(String(64), unique=True, index=True, nullable=False)
    executive_name = Column(String(255), nullable=False)
    corporate_email = Column(String(255), nullable=False, index=True)
    organization = Column(String(255), nullable=False)
    focus_practice = Column(String(100), nullable=False)
    mandate_scope = Column(Text, nullable=True)
    nda_requested = Column(Boolean, default=False)
    status = Column(String(50), default="DISPATCHED_PENDING_REVIEW")
    assigned_partner = Column(String(100), default="Senior Architecture Partner")
    response_sla_hours = Column(Integer, default=4)
    security_hash = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=utc_now)

class PipelineExecution(Base):
    __tablename__ = "pipeline_executions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    execution_id = Column(String(64), unique=True, index=True, nullable=False)
    query_text = Column(String(500), nullable=False)
    stage_reached = Column(Integer, default=7)
    pii_sanitized = Column(Boolean, default=True)
    knowledge_entities_matched = Column(Integer, default=14)
    rag_confidence_score = Column(String(10), default="99.4%")
    agent_consensus = Column(String(100), default="UNANIMOUS (4/4 AGENTS)")
    execution_time_ms = Column(Integer, default=142)
    created_at = Column(DateTime, default=utc_now)

class ContactInquiry(Base):
    __tablename__ = "contact_inquiries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    business_email = Column(String(255), nullable=False, index=True)
    phone = Column(String(100), nullable=True)
    service_interested_in = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=utc_now)
