from typing import List, Optional, Dict, Any
from pydantic import BaseModel, EmailStr, Field
import datetime

# --- Telemetry Models ---
class NodeTelemetry(BaseModel):
    node_id: str
    name: str
    category: str
    latency_ms: float
    status: str
    protocol: str
    throughput_ops: int
    memory_usage_pct: float
    cpu_usage_pct: float
    last_heartbeat: str

class ClusterTelemetryResponse(BaseModel):
    cluster_state: str
    active_nodes: int
    total_nodes: int
    global_average_latency_ms: float
    synapse_version: str
    utc_timestamp: str
    nodes: Dict[str, NodeTelemetry]

# --- 7-Stage Pipeline Models ---
class PipelineStage(BaseModel):
    stage_number: int
    code: str
    name: str
    short_desc: str
    full_description: str
    stats: Dict[str, str]
    key_capabilities: List[str]

class PipelineSimulateRequest(BaseModel):
    mandate_or_query: str = Field(..., min_length=3, max_length=1000)
    enable_anti_hallucination: bool = True
    target_environment: str = "SOVEREIGN_ON_PREM_VPC"

class PipelineSimulateResponse(BaseModel):
    execution_id: str
    status: str
    total_latency_ms: int
    stages_executed: List[Dict[str, Any]]
    final_output_preview: str
    provenance_trace: List[str]

# --- Solutions Models ---
class SolutionSpecification(BaseModel):
    id: str
    title: str
    category: str
    category_label: str
    headline: str
    summary: str
    deliverables: List[str]
    compliance_frameworks: List[str]
    architecture_overview: str
    sla_guarantee: str

# --- SAP Clean Core Assessment ---
class CleanCoreAuditRequest(BaseModel):
    sap_version: str # e.g. "ECC 6.0", "S/4HANA 1909", "S/4HANA 2023"
    custom_z_programs_count: int
    direct_db_modifications: bool
    btp_adoption_rate: str # "None", "Pilot", "Enterprise"
    industry: str

class CleanCoreAuditResponse(BaseModel):
    assessment_id: str
    clean_core_index_pct: int
    compliance_grade: str # A+, A, B, C, CRITICAL
    risk_level: str
    estimated_migration_savings: str
    recommended_pathway: str
    tier_recommendations: List[Dict[str, str]]

# --- Advisory Dispatch Models ---
class AdvisoryDispatchCreate(BaseModel):
    executive_name: str = Field(..., min_length=2, max_length=255)
    corporate_email: str = Field(..., min_length=5, max_length=255)
    organization: str = Field(..., min_length=2, max_length=255)
    focus_practice: str
    mandate_scope: Optional[str] = None
    nda_requested: bool = False

class AdvisoryDispatchResponse(BaseModel):
    success: bool
    ticket_id: str
    message: str
    assigned_partner: str
    response_sla_hours: int
    target_callback_time_utc: str
    security_hash: str
    received_at: str

# --- Client Portal Models ---
class ClientLoginRequest(BaseModel):
    email: str
    access_key: str

class ClientPortalDashboard(BaseModel):
    client_name: str
    organization: str
    active_tenants: int
    synapse_nodes_online: int
    sla_uptime: str
    clean_core_score: str
    recent_deployments: List[Dict[str, str]]
    active_advisories: List[Dict[str, Any]]
