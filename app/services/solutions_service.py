from typing import List, Dict, Optional
from app.models.domain import SolutionSpecification

class SolutionsService:
    SOLUTIONS: Dict[str, SolutionSpecification] = {
        "sovereign-ai": SolutionSpecification(
            id="sovereign-ai",
            title="Private Enterprise AI & Automation",
            category="ai-data",
            category_label="SOVEREIGN AI SUITE",
            headline="Air-gapped domain reasoning models operating entirely inside your corporate boundary.",
            summary="On-premises and private-VPC Small Language Models (SLMs), fine-tuned domain reasoning, and governed multi-agent execution engines.",
            deliverables=[
                "Air-Gapped RAG Pipelines with dense/sparse hybrid search",
                "Deterministic Enterprise Workflows via SAP BTP Event Mesh",
                "Model Risk, Bias, and SOX/HIPAA Compliance Auditing",
                "Domain-specific LoRA parameter-efficient fine-tuning",
                "Private GPU cluster orchestration (NVIDIA Triton & vLLM)"
            ],
            compliance_frameworks=["ISO 27001", "SOC 2 Type II", "HIPAA", "EU AI Act Sovereign Article 10"],
            architecture_overview="Deploying local 8B to 70B parameter models within an isolated VPC or bare-metal GPU clusters. Data never traverses external internet gateways. Ingestion pipelines execute real-time PII scrubbing and format data into knowledge graphs linked to ERP master ledgers.",
            sla_guarantee="99.99% availability, sub-100ms p95 token generation latency, zero data egress guarantee."
        ),
        "sap-modernization": SolutionSpecification(
            id="sap-modernization",
            title="SAP S/4HANA Modernization",
            category="sap",
            category_label="SAP EXCELLENCE",
            headline="Future-proofing core enterprise ERP with pristine Clean Core architecture.",
            summary="Clean Core paradigm transitions, RISE with SAP roadmaps, and SAP BTP cloud-native side-by-side extension engineering.",
            deliverables=[
                "Zero-Modification Core Migration with ABAP Cloud decoupling",
                "SAP Cloud ALM Operations & Automated Regression Testing",
                "SAP Joule Generative Copilot Integration across FICO and MM",
                "Brownfield, Greenfield, and Selective Data Transition Playbooks",
                "Automated Technical Debt Remediation and Z-program elimination"
            ],
            compliance_frameworks=["SAP Clean Core Certified Standard", "IFRS", "SOX 404", "GxP"],
            architecture_overview="Eliminating direct table access and user exits in favor of Tier 1 untouched core, Tier 2 released APIs and event mesh, and Tier 4 side-by-side extensions running on SAP Business Technology Platform (BTP). Ensures biannual upgrades complete in days rather than quarters.",
            sla_guarantee="100% upgradeability guarantee, zero unplanned downtime during brownfield cutover."
        ),
        "hybrid-cloud": SolutionSpecification(
            id="hybrid-cloud",
            title="Hybrid Multi-Cloud Engineering",
            category="infra-sec",
            category_label="CLOUD ARCHITECTURE",
            headline="Sovereign cloud fabrics across AWS, Azure, and Google Cloud with automated failover.",
            summary="AWS, Azure, and Google Cloud cross-platform meshes engineered for regulatory data sovereignty and resilient failover topologies.",
            deliverables=[
                "Terraform / OpenTofu Infrastructure as Code GitOps pipelines",
                "Multi-Region Active-Active Cloud Nodes with automatic BGP routing",
                "FinOps Cloud Margin Governance saving 30-45% cloud spend",
                "Sovereign data residency boundary containment",
                "Unified Kubernetes (EKS/AKS/GKE) cluster federations"
            ],
            compliance_frameworks=["FedRAMP High", "GDPR Data Sovereignty", "DoD IL5/IL6", "PCI-DSS 4.0"],
            architecture_overview="Zero single points of failure multi-cloud fabric. Mesh networking configured with mutual TLS WireGuard overlays, providing sub-millisecond data replication across geographically dispersed availability zones.",
            sla_guarantee="99.999% cloud fabric uptime, sub-60-second cross-cloud failover RTO."
        ),
        "data-fabric": SolutionSpecification(
            id="data-fabric",
            title="Modern Data Fabric & MDM",
            category="ai-data",
            category_label="DATA GOVERNANCE",
            headline="Single source of enterprise truth with Kalido MDM and Apache Iceberg Lakehouses.",
            summary="Unified Master Data Management (Kalido & Informatica), low-latency Apache Iceberg lakes, and real-time Kafka streaming.",
            deliverables=[
                "Kalido MDM & Informatica Master Data Harmonization",
                "Apache Iceberg & Parquet Open Lakehouse Architectures",
                "Automated Lineage, Data Cataloging, and Regulatory Compliance",
                "Sub-second Kafka / Redpanda event streaming pipelines",
                "Reverse-ETL synchronization into SAP HANA and Salesforce"
            ],
            compliance_frameworks=["BCBS 239", "GDPR Right to Be Forgotten", "CCPA", "HIPAA Data Governance"],
            architecture_overview="Decoupling analytical compute from storage. Master data schemas are harmonized in Kalido MDM and streamed in real time to multi-engine query systems (Trino, Snowflake, BigQuery) preserving ACID guarantees.",
            sla_guarantee="100% transactional consistency, zero duplicate master records across subsidiaries."
        ),
        "enterprise-security": SolutionSpecification(
            id="enterprise-security",
            title="Enterprise Security & Defense",
            category="infra-sec",
            category_label="DEFENSIVE RESILIENCE",
            headline="Cryptographic Zero-Trust resilience and hardware-backed key protection.",
            summary="Zero-Trust network segmentation, sovereign key management (KMS), and proactive SOC automation for regulated financial and defense nodes.",
            deliverables=[
                "Zero-Trust IAM, Least-Privilege Role & Microsegmentation",
                "Hardware Security Module (HSM) FIPS 140-3 Key Enclaves",
                "Continuous Compliance Telemetry with automated SIEM/SOAR",
                "Post-Quantum Cryptography (PQC) readiness migration",
                "Red Team Adversarial Emulation and Chaos Engineering"
            ],
            compliance_frameworks=["NIST SP 800-53 Rev 5", "ISO 27001:2022", "FIPS 140-3", "CIS Top 18"],
            architecture_overview="Every packet, request, and query must be authenticated and authorized. Microsegmentation isolates core databases from application tiers, with automated cryptographic rotation every 24 hours.",
            sla_guarantee="Zero breach history, sub-5-minute mean time to detect (MTTD) on anomalous telemetry."
        ),
        "app-engineering": SolutionSpecification(
            id="app-engineering",
            title="Mission-Critical App Engineering",
            category="infra-sec",
            category_label="ENGINEERING CORE",
            headline="Polyglot high-throughput systems engineered for extreme transaction velocity.",
            summary="Polyglot microservices, distributed transaction managers, and reactive web applications engineered for millions of concurrent interactions.",
            deliverables=[
                "High-Throughput Go / Rust low-latency trading and logistics engines",
                "gRPC / Protobuf Internal Communication Fabrics",
                "Formal Invariant Verification & Fault-tolerant state machines",
                "Event-driven CQRS architectures with Kafka and NATS",
                "Observability stacks with OpenTelemetry and distributed tracing"
            ],
            compliance_frameworks=["OpenID Connect", "OAuth 2.1", "Twelve-Factor App Methodology", "W3C Accessible"],
            architecture_overview="Designed from ground-up for extreme reliability under peak loads. Distributed transaction handling with Saga patterns and 2-phase commits, preventing state divergence across heterogeneous enterprise backends.",
            sla_guarantee="Sub-10ms transaction processing p99, zero unhandled invariant panics."
        )
    }

    def list_solutions(self, category: Optional[str] = None) -> List[SolutionSpecification]:
        if not category or category == "all":
            return list(self.SOLUTIONS.values())
        return [s for s in self.SOLUTIONS.values() if s.category == category]

    def get_solution(self, solution_id: str) -> Optional[SolutionSpecification]:
        return self.SOLUTIONS.get(solution_id)

solutions_service = SolutionsService()
