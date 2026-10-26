from fastapi import APIRouter, HTTPException
from app.models.domain import ClientLoginRequest, ClientPortalDashboard

router = APIRouter(prefix="/portal", tags=["Client Portal"])

# Authorized demo access credentials
AUTHORIZED_PORTAL_CLIENTS = {
    "executive@enterprise.com": "SUMERU-EXEC-2025",
    "partner@sumeru.com": "SUMERU-PARTNER-CORE",
    "client@sumerutechnologies.com": "SUMERU-DEMO-PORTAL"
}

@router.post("/authenticate", response_model=ClientPortalDashboard)
async def authenticate_client(creds: ClientLoginRequest):
    """Authenticate executive client credentials and retrieve active tenant health."""
    email_clean = creds.email.strip().lower()
    key_clean = creds.access_key.strip()

    expected_key = AUTHORIZED_PORTAL_CLIENTS.get(email_clean)
    if not expected_key or expected_key != key_clean:
        raise HTTPException(status_code=401, detail="Invalid corporate credentials or unauthorized access key")

    return ClientPortalDashboard(
        client_name="Global Enterprise Client",
        organization="Fortune 100 Regulated Institutional Partner",
        active_tenants=3,
        synapse_nodes_online=7,
        sla_uptime="99.994%",
        clean_core_score="94/100 (A+ Clean Core)",
        recent_deployments=[
            {"release": "v4.8.2-PROD", "status": "LIVE", "component": "Synapse SLM Reasoning Mesh", "region": "US-East (Warrenville VPC)"},
            {"release": "v2.4.1", "status": "LIVE", "component": "SAP BTP Event Decoupler", "region": "Frankfurt EMEA Hub"},
            {"release": "v1.9.0", "status": "STAGING", "component": "Kalido MDM Stream Cache", "region": "India Core Dev"}
        ],
        active_advisories=[
            {"id": "SUM-ADV-2501-A91B", "mandate": "SAP Clean Core 2025 S/4HANA Upgrade Strategy", "status": "IN_PROGRESS", "lead": "Senior Architecture Partner"},
            {"id": "SUM-ADV-2412-C83E", "mandate": "Private RAG Air-Gapped Governance Audit", "status": "COMPLETED_DELIVERED", "lead": "Sovereign Intelligence Fellow"}
        ]
    )
