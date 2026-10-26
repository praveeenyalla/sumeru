import uuid
from typing import Dict, List, Any
from app.models.domain import CleanCoreAuditRequest, CleanCoreAuditResponse

class CleanCoreService:
    TIERS = [
        {
            "tier": "T5",
            "title": "SAP Fiori & Modern Experiences",
            "subtitle": "Adaptive UI5, mobile interfaces, and unified portal experiences.",
            "label": "User Experience",
            "color": "tertiary",
            "role": "Modern frontends decoupled from backend ABAP logic via OData v4."
        },
        {
            "tier": "T4",
            "title": "BTP Side-by-Side Extensions",
            "subtitle": "Node.js, Java, and CAP services running decoupled in cloud runtimes.",
            "label": "Decoupled Logic",
            "color": "secondary",
            "role": "Custom application logic deployed in SAP Business Technology Platform."
        },
        {
            "tier": "T3",
            "title": "SAP Cloud ALM & Observability",
            "subtitle": "Real-time health, automated regression suites, and release controls.",
            "label": "Governance",
            "color": "tertiary",
            "role": "Continuous lifecycle observability, test automation, and release synchronization."
        },
        {
            "tier": "T2",
            "title": "Standard Public APIs & Events",
            "subtitle": "OData v4 and SAP Event Mesh eliminating direct database joins.",
            "label": "Strict Gateway",
            "color": "primary",
            "role": "Officially released standard interfaces guaranteeing backward compatibility."
        },
        {
            "tier": "T1",
            "title": "Pristine SAP Kernel (S/4HANA)",
            "subtitle": "100% untouched core logic with perpetual upgrade readiness.",
            "label": "IMMUTABLE CORE",
            "color": "primary-container",
            "role": "Zero modification to standard SAP tables, function modules, or core transactions."
        }
    ]

    def get_tiers(self) -> List[Dict[str, Any]]:
        return self.TIERS

    def evaluate_clean_core(self, req: CleanCoreAuditRequest) -> CleanCoreAuditResponse:
        assessment_id = f"SAP-AUDIT-{uuid.uuid4().hex[:6].upper()}"

        # Calculation logic
        score = 100
        # Penalize for custom Z programs
        if req.custom_z_programs_count > 500:
            score -= 35
        elif req.custom_z_programs_count > 200:
            score -= 22
        elif req.custom_z_programs_count > 50:
            score -= 12
        else:
            score -= 4

        # Penalize for direct database modifications
        if req.direct_db_modifications:
            score -= 30

        # Reward for BTP adoption
        if req.btp_adoption_rate == "Enterprise":
            score += 15
        elif req.btp_adoption_rate == "Pilot":
            score += 5
        else:
            score -= 10

        # Adjust based on current SAP version
        if "ECC" in req.sap_version:
            score -= 15
        elif "1909" in req.sap_version or "2020" in req.sap_version:
            score -= 5

        score = max(24, min(98, score))

        if score >= 85:
            grade = "A+ Sovereign Compliant"
            risk = "MINIMAL"
            savings = "$1.8M - $3.2M across 3-year lifecycle"
            pathway = "S/4HANA Cloud Public / Private Edition with Joule Copilots"
        elif score >= 70:
            grade = "B Tier Upgrade Ready"
            risk = "MODERATE"
            savings = "$950k - $1.6M through selective BTP decoupling"
            pathway = "Selective Data Transition with BTP Side-by-Side refactoring"
        elif score >= 50:
            grade = "C Technical Debt Warning"
            risk = "ELEVATED"
            savings = "$600k - $1.1M post-cleanup"
            pathway = "Brownfield + Sumeru Clean Core Decoupling Sprint"
        else:
            grade = "CRITICAL High Modification Risk"
            risk = "CRITICAL / UPGRADE INHIBITED"
            savings = "Over $2.5M in deferred maintenance avoidance"
            pathway = "Greenfield Re-platforming to Pristine S/4HANA Clean Core"

        recommendations = [
            {"tier": "T1 (Kernel)", "action": "Lock standard SAP tables; disallow direct user exit modifications."},
            {"tier": "T2 (APIs)", "action": "Convert RFC / BAPI calls to modern OData v4 and SAP Event Mesh."},
            {"tier": "T3 (ALM)", "action": "Deploy SAP Cloud ALM automated test automation to eliminate 80% manual UAT."},
            {"tier": "T4 (BTP)", "action": f"Migrate top {min(req.custom_z_programs_count, 45)} custom workflows to SAP BTP Cloud Foundry / Kyma runtimes."},
            {"tier": "T5 (UX)", "action": "Replace classical SAP GUI transactions with responsive SAP Fiori Elements."}
        ]

        return CleanCoreAuditResponse(
            assessment_id=assessment_id,
            clean_core_index_pct=score,
            compliance_grade=grade,
            risk_level=risk,
            estimated_migration_savings=savings,
            recommended_pathway=pathway,
            tier_recommendations=recommendations
        )

clean_core_service = CleanCoreService()
