"""
Script to inject comprehensive detailed_topics and enriched partners into app/services/corporate_content.py
"""

import sys
import os

# We can import existing DETAILED_TOPICS from enrich_topics_data.py
import enrich_topics_data as etd

# Additional topics for About, Company Team, Quality, Careers, Solutions
ADDITIONAL_TOPICS = {
    "/about": [
        {
            "id": "heritage-30-years",
            "nav_label": "30+ Years Heritage",
            "badge": "HERITAGE • FOUNDED 1994",
            "title": "Three Decades of Continuous Enterprise Technology Delivery",
            "lead": "Founded in 1994, Sumeru Technologies has built a lasting legacy of excellence, guiding organizations through major waves of digital and ERP transformations.",
            "content": """Sumeru Technologies was founded in 1994 with a simple, enduring vision: to be the 'partner of choice' for discriminating clients who require high-end Systems Integration, Application Lifecycle Management, Custom Application Development, Package Deployment, and Product Development services at sustainable value over the long haul.

Over 30+ years, enterprise technology has transformed from on-premise mainframes and client-server architectures to global ERP suites, cloud-native platforms, and sovereign intelligence networks. Throughout this evolution, Sumeru's founding principles—integrity, technological depth, and uncompromised client commitment—have remained constant.""",
            "methodology": [
                {"step": "STAGE 01", "name": "Long-Term Strategic Stewardship", "desc": "Partnering with enterprise clients for multi-year technology roadmaps rather than one-off transactional projects."},
                {"step": "STAGE 02", "name": "Practitioner-Led Governance", "desc": "Deploying senior practitioners with 15+ years of hands-on architectural experience on every client engagement."},
                {"step": "STAGE 03", "name": "Follow-the-Sun Global Delivery", "desc": "Seamless coordination across US headquarters, European hub, and premier India engineering centers."},
                {"step": "STAGE 04", "name": "Sustainable Value Realization", "desc": "Ensuring measurable ROI, zero vendor lock-in, and full client ownership of implemented architectures."}
            ],
            "technologies": ["Systems Integration", "SAP S/4HANA", "Oracle EBS", "Cloud Infrastructure", "Enterprise Architecture", "Clean Core Standards"],
            "deliverables": [
                "30-Year Proven Delivery Track Record",
                "Executive Architectural Governance Framework",
                "Vendor-Neutral Strategic Advisory",
                "Global SLA Delivery Assurance"
            ],
            "qa": {
                "q": "What makes Sumeru Technologies different from large generic IT consulting conglomerates?",
                "a": "Unlike massive staffing conglomerates where clients get junior resources and bureaucratic overhead, Sumeru provides direct access to veteran architects, senior practitioners, and flexible delivery squads. We prioritize long-term client success, sustainable architecture, and zero technical debt over billable hour expansion."
            }
        },
        {
            "id": "4d-lifecycle",
            "nav_label": "4D Business Approach",
            "badge": "METHODOLOGY • 4D DELIVERY",
            "title": "The 4D Delivery Methodology: Discover, Design, Deploy, Drive",
            "lead": "A disciplined, four-phase delivery paradigm that translates executive vision into scalable software architectures and 24x7 managed operations.",
            "content": """Every successful enterprise technology deployment requires a structured balance between business strategy, architectural rigor, and operational continuity. Sumeru's proprietary 4D Business Approach provides a battle-tested roadmap from initial executive scoping through 24x7 global operational stewardship.

By establishing clear checkpoints and accountability gates at each phase, we eliminate mid-project scope creep, vendor finger-pointing, and unbudgeted implementation overruns.""",
            "methodology": [
                {"step": "PHASE 01", "name": "Discover (Scope & Opportunity)", "desc": "Auditing existing infrastructure, business objectives, and identifying immediate quick wins and strategic roadmaps."},
                {"step": "PHASE 02", "name": "Design (Architecture & Blueprint)", "desc": "Engineering complete, scalable solution blueprints integrating seamlessly with existing ERP and legacy environments."},
                {"step": "PHASE 03", "name": "Deploy (Implementation & Rigor)", "desc": "Applying agile execution, automated test benches, change management, and user training to deliver on time and on budget."},
                {"step": "PHASE 04", "name": "Drive (Managed Operations)", "desc": "Providing 24x7 remote database, ERP, and infrastructure management from our follow-the-sun global centers."}
            ],
            "technologies": ["PMP Framework", "Agile & Scrum", "ITIL v4 Service Management", "TOGAF 10 Architecture", "Automated QA Test Benches"],
            "deliverables": [
                "4D Project Charter & Scope Matrix",
                "End-to-End Architectural Specification Document",
                "Automated Regression Test Suite Certification",
                "24x7 Managed Service Level Agreement (SLA)"
            ],
            "qa": {
                "q": "How does the 4D Approach ensure projects stay on schedule and within budget?",
                "a": "The 4D framework mandates strict sign-off gates between Discovery and Design, locking functional boundaries and interface specifications before coding begins. Weekly burn-down reporting and PMP governance ensure milestones are met predictably."
            }
        }
    ],

    "/company/team": [
        {
            "id": "leadership-philosophy",
            "nav_label": "Practitioner Leadership",
            "badge": "LEADERSHIP • ARCHITECTURAL EXCELLENCE",
            "title": "Practitioner-Led Executive Leadership & Technical Governance",
            "lead": "Guided by hands-on engineering leaders who combine executive business acumen with deep architectural expertise in enterprise systems.",
            "content": """At Sumeru Technologies, leadership is defined by practical engineering mastery, not theoretical management. Our practice heads and senior partners have spent decades in the trenches designing ERP cores, high-throughput message fabrics, and mission-critical databases for Fortune 500 corporations.

Every client engagement is directly sponsored by an executive partner who remains actively engaged throughout Discovery, Design, and Deployment to ensure architectural integrity and milestone predictability.""",
            "methodology": [
                {"step": "PILLAR 01", "name": "Executive Engagement Sponsorship", "desc": "Every project is directly overseen by a senior practice partner with decision-making authority."},
                {"step": "PILLAR 02", "name": "Peer-Reviewed Architecture", "desc": "All system blueprints undergo multi-disciplinary architectural review across security, scale, and compliance."},
                {"step": "PILLAR 03", "name": "Talent Development & Mentorship", "desc": "Continuous technical certification and leadership programs across our USA, European, and Indian engineering hubs."},
                {"step": "PILLAR 04", "name": "Client Advocacy & Transparency", "desc": "Unbiased vendor evaluations and honest architectural counsel prioritizing long-term client benefit."}
            ],
            "technologies": ["Executive Architecture Governance", "TOGAF Standards", "PMP Project Direction", "Clean Core ERP Governance"],
            "deliverables": [
                "Executive Steering Committee Governance Matrix",
                "Architectural Review Board (ARB) Sign-Offs",
                "Quarterly Strategic Technology Briefings"
            ],
            "qa": {
                "q": "Who leads client implementations at Sumeru Technologies?",
                "a": "All client engagements are led by seasoned Principal Architects and PMP-certified Delivery Directors who possess a minimum of 15 years of industry experience across SAP, Oracle, cloud integration, or enterprise databases."
            }
        }
    ],

    "/company/quality": [
        {
            "id": "quality-credo",
            "nav_label": "Quality Credo & Ruskin",
            "badge": "QUALITY • JOHN RUSKIN CREDO",
            "title": "Quality is Never an Accident: It is Always the Result of Intelligent Effort",
            "lead": "Our operational creed, inspired by John Ruskin, governs every line of code, architectural blueprint, and SLA commitment we make.",
            "content": """Sumeru Technologies operates under a foundational principle: 'Quality is never an accident. It is always the result of intelligent effort.' In enterprise computing, software bugs, data loss, or system downtime have catastrophic financial and operational consequences.

We embed quality assurance into every phase of our delivery lifecycle. From static code analysis and automated regression suites to peer-reviewed architecture blueprints and formal SLA governance, quality is an active, continuous discipline.""",
            "methodology": [
                {"step": "STAGE 01", "name": "Requirements Precision & Traceability", "desc": "Ensuring every functional and non-functional requirement maps directly to verifiable acceptance tests."},
                {"step": "STAGE 02", "name": "Static Code & Security Scanning", "desc": "Enforcing SonarQube quality gates, OWASP vulnerability scans, and strict coding standards."},
                {"step": "STAGE 03", "name": "Automated Regression & Load Testing", "desc": "Simulating peak transaction volumes (300%+ nominal capacity) to certify resilience and zero latency spikes."},
                {"step": "STAGE 04", "name": "SLA-Guaranteed Operational Auditing", "desc": "Weekly defect burn-down tracking, root-cause defect elimination, and client transparency scorecards."}
            ],
            "technologies": ["SonarQube Quality Gates", "Selenium & Cypress Automation", "JMeter Load Testing", "ITIL v4 Quality Standards", "ISO 9001 Alignment"],
            "deliverables": [
                "Comprehensive Quality Assurance Charter",
                "Automated Regression Test Certification",
                "Security Vulnerability Audit Scorecard",
                "Binding Operational SLA Commitment"
            ],
            "qa": {
                "q": "What specific metrics does Sumeru use to measure delivery quality?",
                "a": "We track test coverage (>85%), defect density (<0.1 defects per KLOC), automated regression pass rates (100% before cutover), and strict adherence to binding SLA response and resolution times."
            }
        }
    ],

    "/solutions/sap": [
        {
            "id": "sap-clean-core",
            "nav_label": "SAP Clean Core & BTP",
            "badge": "SAP PRACTICE • CLEAN CORE",
            "title": "SAP Clean Core Architecture & Side-by-Side BTP Extensions",
            "lead": "Preserving the standard ERP kernel while delivering rapid custom innovation through decoupled APIs and SAP Business Technology Platform.",
            "content": """For decades, SAP customers customized their ECC systems by directly modifying standard tables and writing custom Z-programs inside the core. While this provided tailored functionality, it turned future upgrades into multi-million-dollar nightmares with massive code breakage.

Sumeru's SAP Practice enforces SAP's Clean Core strategy. We keep the core ERP pristine and standard, building all custom business logic, workflows, and integrations side-by-side on SAP BTP using released OData APIs and event meshes. This ensures future S/4HANA release updates execute seamlessly in days without custom code failure.""",
            "methodology": [
                {"step": "PHASE 01", "name": "Custom Code (Z-Program) Audit", "desc": "Scanning legacy ECC custom code using SAP Custom Code Migration Worklist to categorize obsolete and non-compliant code."},
                {"step": "PHASE 02", "name": "Clean Core Decoupling Blueprint", "desc": "Architecting side-by-side BTP extension models using ABAP Cloud, CAP, and SAP Integration Suite."},
                {"step": "PHASE 03", "name": "API & Event Broker Implementation", "desc": "Deploying standard OData v4 endpoints and SAP Event Mesh to synchronize transactions asynchronously."},
                {"step": "PHASE 04", "name": "Upgrade Validation & Certification", "desc": "Testing simulated S/4HANA release upgrades to prove 100% non-breaking Clean Core compliance."}
            ],
            "technologies": ["SAP BTP", "ABAP Cloud", "SAP Cloud Application Programming Model (CAP)", "SAP Fiori / UI5", "SAP Event Mesh", "OData v4 APIs"],
            "deliverables": [
                "Clean Core Architecture Assessment",
                "Z-Code Remediation & BTP Decoupling Roadmap",
                "Side-by-Side BTP Extension Runtime Setup",
                "Zero-Modification Upgrade Certification"
            ],
            "qa": {
                "q": "How does Sumeru migrate legacy user exits and modifications to SAP Clean Core?",
                "a": "We replace legacy user exits with SAP In-App Extensibility (Business Add-Ins using released interfaces) or Side-by-Side BTP extensions that interact with S/4HANA via standard OData APIs and business events, completely eliminating core modification."
            }
        },
        {
            "id": "rise-with-sap",
            "nav_label": "RISE with SAP Advisory",
            "badge": "SAP PRACTICE • CLOUD ADVISORY",
            "title": "RISE with SAP: Business Transformation as a Service (BTaaS)",
            "lead": "Strategic guidance for transitioning from on-premise ECC to SAP S/4HANA Cloud under unified SLA and cloud infrastructure management.",
            "content": """RISE with SAP offers enterprises a bundled path to cloud ERP, combining S/4HANA Cloud software, cloud infrastructure (AWS/Azure/GCP), SAP Business Network starter packages, and business process intelligence under a single contract.

However, navigating contract licensing, custom code remediation, infrastructure sizing, and migration sequencing requires an experienced implementation partner. Sumeru serves as your objective advisor and delivery partner, formulating a phased migration roadmap that protects existing investments while accelerating cloud benefits.""",
            "methodology": [
                {"step": "PHASE 01", "name": "Readiness Assessment & TCO", "desc": "Evaluating business process complexity, license conversion rights, and calculating 5-year cloud TCO."},
                {"step": "PHASE 02", "name": "Migration Strategy Formulation", "desc": "Determining Greenfield (re-implementation), Brownfield (system conversion), or Selective Data Transition path."},
                {"step": "PHASE 03", "name": "Process Intelligence with Signavio", "desc": "Benchmarking current process execution to identify automation opportunities before cloud deployment."},
                {"step": "PHASE 04", "name": "Cloud Cutover & SLA Stewardship", "desc": "Managing technical cutover, hypercare support, and continuous application management."}
            ],
            "technologies": ["RISE with SAP", "SAP S/4HANA Cloud", "SAP Signavio", "SAP Activate Methodology", "Hyperscaler Cloud Infrastructure"],
            "deliverables": [
                "RISE with SAP Strategic Migration Roadmap",
                "Brownfield vs Greenfield Decision Matrix",
                "Signavio Process Benchmark Report",
                "Single-Contract Cloud Operations Framework"
            ],
            "qa": {
                "q": "Can Sumeru help us choose between S/4HANA Cloud Private Edition and Public Edition?",
                "a": "Yes. We evaluate your industry customization needs, regulatory constraints, and process standardizability. For clients needing deep industry extensions, Private Edition offers greater control, while Public Edition offers rapid innovation cycles."
            }
        }
    ]
}

ENRICHED_PARTNERS = [
    {
        "id": "microsoft",
        "name": "Microsoft Corporation",
        "tag": "Certified Solutions Partner",
        "badge": "CERTIFIED CLOUD & ENTERPRISE DATA ALLIANCE",
        "logo": "/static/images/partners/microsoft.svg",
        "lead": "Official Microsoft Certified Solutions Partner delivering hybrid enterprise infrastructure, Azure Cloud migrations, Microsoft Fabric analytics, and .NET enterprise application modernization.",
        "desc": """Sumeru Technologies has maintained an enduring alliance with Microsoft Corporation, architecting scalable enterprise solutions across Azure Cloud infrastructure, hybrid enterprise directory architectures, Microsoft Fabric, and Power Platform ecosystems.

Our team includes Microsoft-certified Solutions Architects, DevOps Engineers, and Data Platform Specialists who deploy mission-critical architectures aligned with the Microsoft Cloud Adoption Framework (CAF) and Well-Architected principles. We help clients navigate complex migrations from on-premise Windows/SQL Server landscapes to resilient multi-region Azure environments with automated CI/CD and zero downtime.""",
        "commitments": [
            "Microsoft Certified Solutions Partner status with certified architects, data engineers, and DevOps leads",
            "Strict adherence to Microsoft Cloud Adoption Framework (CAF) and Well-Architected Security benchmarks",
            "Binding enterprise SLAs for hybrid cloud migration, Azure SQL high availability, and automated failover",
            "Dedicated Azure Competency Centers in Warrenville, IL and Hyderabad providing 24x7 managed cloud operations",
            "Direct escalation pathways to Microsoft enterprise technical support"
        ],
        "technologies": [
            "Microsoft Azure", "Microsoft Fabric", "Azure Synapse Analytics", "Azure SQL & Cosmos DB",
            "Power BI Enterprise", ".NET Core 8/9", "Azure DevOps & GitHub Enterprise", "Active Directory / Entra ID"
        ],
        "deliverables": [
            "Enterprise Azure Cloud Architecture & CAF Roadmap",
            "Azure Landing Zone & Multi-Subscription Security Blueprint",
            "Power BI Executive Analytics & Governance Workspace",
            "High-Availability SQL Server to Azure SQL Migration Plan",
            "Automated Terraform Infrastructure-as-Code (IaC) Pipelines"
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Cloud Readiness & TCO Assessment", "desc": "Auditing on-premise compute, licensing, database dependencies, and calculating multi-year Azure TCO savings."},
            {"step": "PHASE 02", "name": "Landing Zone Architecture", "desc": "Configuring Hub-Spoke virtual networks, express routes, Entra ID SSO, and automated role-based access control (RBAC)."},
            {"step": "PHASE 03", "name": "Workload Migration & Data Seeding", "desc": "Executing live database replication, containerizing microservices on AKS, and migrating transactional workloads."},
            {"step": "PHASE 04", "name": "24x7 Azure Ops & Cost Optimization", "desc": "Enforcing continuous FinOps cost governance, Azure Monitor alerts, and automated patch compliance runbooks."}
        ],
        "qa": {
            "q": "What specific commitments and SLA guarantees does Sumeru provide for Microsoft Azure migrations?",
            "a": "Sumeru guarantees zero data loss and a 99.99% availability target for migrated enterprise workloads. Our certified engineers execute shadow testing and live data replication before cutover, ensuring production transitions execute within defined weekend maintenance windows with full rollback assurance."
        }
    },
    {
        "id": "sap",
        "name": "SAP Practice & Clean Core Alliance",
        "tag": "Ecosystem & Clean Core Partner",
        "badge": "ENTERPRISE ERP & S/4HANA ADVISORY",
        "logo": "/static/images/partners/sap.svg",
        "lead": "End-to-end SAP ecosystem implementations, S/4HANA cloud transitions, RISE with SAP advisory, and SAP BTP Clean Core decoupled extension architectures.",
        "desc": """Sumeru Technologies has delivered high-impact SAP solutions since 1994, guiding Fortune 500 corporations and mid-market enterprises through ECC 6.0 implementations, S/4HANA transformations, and cloud modernizations.

Our SAP practice champions the 'Clean Core' paradigm: keeping the ERP kernel standard and upgrade-ready by decoupling custom logic and third-party integrations onto SAP Business Technology Platform (BTP). In addition, Sumeru provides specialized, pre-configured industry templates for Manufacturing, Textile & Apparel (Fiber to Fashion), and Education.""",
        "commitments": [
            "Certified SAP implementation methodologies adhering to SAP Activate and Clean Core guidelines",
            "Zero-modification core governance: all custom business logic architected side-by-side on SAP BTP",
            "Binding 15-minute Sev-1 incident response time for production ERP outages under 24x7 SLA contracts",
            "Dedicated SAP Delivery Center of Excellence in Hyderabad and Warrenville with certified functional & technical leads",
            "Guaranteed upgrade compatibility protecting clients against expensive future re-platforming"
        ],
        "technologies": [
            "SAP S/4HANA Cloud & On-Premise", "SAP BTP (Extension & Integration Suite)", "ABAP Cloud",
            "SAP Fiori / UI5", "SAP Signavio Process Mining", "SAP HANA In-Memory DB", "SAP Cloud ALM"
        ],
        "deliverables": [
            "SAP S/4HANA Clean Core Migration Blueprint",
            "RISE with SAP Readiness & TCO Assessment",
            "Side-by-Side BTP Extension Specification",
            "Industry-Specific Pre-configured Best Practice Packages",
            "24x7 Global Remote Basis & Functional SLA Support"
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "ECC Landscape & Custom Code Audit", "desc": "Analyzing existing Z-code, user exits, table modifications, and evaluating Clean Core conversion readiness."},
            {"step": "PHASE 02", "name": "Target Architecture & BTP Blueprint", "desc": "Specifying clean core boundaries, OData APIs, event meshes, and target S/4HANA data models."},
            {"step": "PHASE 03", "name": "Phased Migration & Validation", "desc": "Executing data cleansing, mock cutovers, automated test regression, and dual-run business validation."},
            {"step": "PHASE 04", "name": "Go-Live Hypercare & 24x7 Basis Ops", "desc": "Providing on-site and remote hypercare, SLA monitoring, and continuous process optimization."}
        ],
        "qa": {
            "q": "How does Sumeru's Clean Core approach reduce long-term SAP ownership costs?",
            "a": "By eliminating direct modifications to SAP standard core code and implementing all business extensions on SAP BTP using released APIs, future S/4HANA release upgrades take days rather than months, slashing upgrade costs by over 60% and eliminating version lock-in."
        }
    },
    {
        "id": "informatica",
        "name": "Informatica",
        "tag": "Enterprise Data Integration Partner",
        "badge": "CERTIFIED DATA INTEGRATION ALLIANCE",
        "logo": "/static/images/partners/informatica.svg",
        "lead": "Leading enterprise data integration, Intelligent Data Management Cloud (IDMC), ETL/ELT pipelines, and automated data quality governance.",
        "desc": """Sumeru Technologies partners with Informatica to solve one of the most pressing challenges in enterprise computing: connecting fragmented operational data across on-premise ERPs, cloud CRMs, legacy databases, and analytics lakehouses.

Our Informatica practice builds robust, high-throughput ETL/ELT pipelines, master data hubs, and automated data quality rule engines that process millions of records daily with guaranteed auditability, end-to-end lineage, and zero data leakage.""",
        "commitments": [
            "Certified Informatica PowerCenter and IDMC integration architects and developers",
            "Zero-data-loss extraction, transformation, and load (ETL) guarantees with automatic failure recovery",
            "Automated data quality profiling enforcing >99.8% field accuracy and regulatory compliance",
            "Pre-built connector pipelines for SAP, Oracle, Salesforce, Snowflake, and Microsoft Fabric",
            "Dedicated data governance and master data stewardship frameworks"
        ],
        "technologies": [
            "Informatica PowerCenter", "Informatica IDMC", "Informatica Data Quality (IDQ)",
            "Enterprise Data Catalog (EDC)", "Cloud Application Integration (CAI)", "Cloud B2B Gateway"
        ],
        "deliverables": [
            "Enterprise Data Integration Architecture Blueprint",
            "Automated ETL/ELT Pipeline & Schedule Specification",
            "Data Quality Rules Engine & Cleansing Scorecards",
            "End-to-End Enterprise Data Lineage Dictionary"
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Source Landscape & Schema Profiling", "desc": "Cataloging source tables, APIs, extraction frequencies, volume benchmarks, and data quality defects."},
            {"step": "PHASE 02", "name": "Mapping & Transformation Modeling", "desc": "Building reusable Informatica transformations, lookup caches, and canonical data models."},
            {"step": "PHASE 03", "name": "High-Throughput Pipeline Deployment", "desc": "Configuring pushdown optimization, parallel partitioning, and automated error recovery queues."},
            {"step": "PHASE 04", "name": "Lineage Governance & Telemetry", "desc": "Enabling Enterprise Data Catalog metadata harvesting, audit tracking, and automated SLA alerts."}
        ],
        "qa": {
            "q": "How does Informatica streamline massive cross-system data migrations?",
            "a": "Informatica provides pre-built enterprise connectors with native bulk loaders and pushdown optimization. Sumeru leverages these capabilities to execute multi-terabyte data migrations at database speeds while enforcing live validation checks, ensuring target data is error-free upon arrival."
        }
    },
    {
        "id": "kalido",
        "name": "Kalido",
        "tag": "Enterprise MDM & Data Warehouse Partner",
        "badge": "ADAPTIVE DATA WAREHOUSING & MDM ALLIANCE",
        "logo": "/static/images/partners/kalido.svg",
        "lead": "Adaptive enterprise data warehousing and master data management software delivering timely, accurate single-source-of-truth insight across business restructuring.",
        "desc": """Sumeru Technologies has been a premier partner of Kalido for more than two decades, pioneering the implementation of Kalido Information Engine and Adaptive Master Data Management across major global clients.

Unlike rigid traditional MDM platforms that break whenever corporate structures, product taxonomies, or reporting hierarchies change, Kalido's business-model-driven architecture adapts dynamically. It allows multinational enterprises to harmoniously manage customer, supplier, financial, and organizational data through mergers, acquisitions, and restructuring.""",
        "commitments": [
            "Over 20 years of continuous enterprise implementation expertise with Kalido software",
            "Single-source-of-truth golden record consolidation with automated deduplication across subsidiaries",
            "Adaptive dimensional modeling that evolves without costly physical database redesign",
            "Dedicated Kalido technical support, maintenance, and upgrade engineering squads",
            "Guaranteed historical data traceability and immutable audit reporting"
        ],
        "technologies": [
            "Kalido Information Engine", "Kalido Adaptive MDM", "Kalido Universal Model",
            "Active Data Governance", "Real-Time Golden Record Syndication", "Multi-Domain Data Stewardship"
        ],
        "deliverables": [
            "Adaptive Enterprise Master Data Architecture",
            "Domain Entity Matching & Golden Record Survivorship Rules",
            "Automated Data Syndication Broker Configuration",
            "Data Stewardship Portal & Exception Approval Runbook"
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Enterprise Entity Profiling", "desc": "Profiling conflicting customer, vendor, and chart-of-accounts records across all subsidiary databases."},
            {"step": "PHASE 02", "name": "Adaptive Model Definition", "desc": "Creating flexible business models in Kalido that represent core entities independent of source technical schemas."},
            {"step": "PHASE 03", "name": "Matching & Survivorship Rules", "desc": "Deploying automated matching, probabilistic duplicate identification, and survivorship algorithms."},
            {"step": "PHASE 04", "name": "Bidirectional Syndication", "desc": "Syndicating verified golden records back to operational ERP, CRM, and transactional ledgers."}
        ],
        "qa": {
            "q": "Why is Kalido Adaptive MDM superior for enterprises experiencing frequent acquisitions or restructuring?",
            "a": "Traditional MDM systems hardcode organizational relationships into rigid database schemas, making restructuring costly and slow. Kalido decouples the business model from physical tables, allowing new business units or product lines to be onboarded in days without disrupting existing operational systems."
        }
    },
    {
        "id": "oracle",
        "name": "Oracle PartnerNetwork (OPN)",
        "tag": "Enterprise Database & Applications Partner",
        "badge": "ORACLE EBS & DATABASE EXCELLENCE",
        "logo": "/static/images/partners/oracle.svg",
        "lead": "End-to-end lifecycle implementation, database administration, high-availability RAC clustering, and enterprise performance tuning for Oracle E-Business Suite and Cloud.",
        "desc": """Sumeru Technologies delivers comprehensive architectural, functional, and DBA lifecycle support for Oracle E-Business Suite (EBS 12.2) and Oracle Cloud Applications. Our certified Oracle architects specialize in stabilizing mission-critical financial, procurement, and manufacturing systems.

From high-concurrency database deadlocks and RAC clustering to non-disruptive Application DBA Online Patching (ADOP) and RMAN backup automation, Sumeru ensures your core Oracle investments run at peak performance with zero data loss.""",
        "commitments": [
            "30-year track record of certified Oracle DBAs and Applications specialists",
            "24x7 Remote DBA administration with proactive performance tuning and index optimization",
            "Non-disruptive ADOP patch deployment and major version upgrades with minimal cutover windows",
            "Binding 15-minute Sev-1 response time for critical database outages",
            "Zero-data-loss RMAN backup automation and cross-region Data Guard failover testing"
        ],
        "technologies": [
            "Oracle E-Business Suite 12.2", "Oracle Database 19c/21c", "Oracle Real Application Clusters (RAC)",
            "Oracle Data Guard", "Oracle Fusion Cloud ERP", "Oracle RMAN & ASM", "PL/SQL & CEMLI"
        ],
        "deliverables": [
            "Oracle High-Availability & Disaster Recovery Architecture",
            "CEMLI Customization Catalog & Technical Health Audit",
            "Database Performance & Concurrency Tuning Report",
            "24x7 Remote DBA Incident Response & Maintenance Runbook"
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Database & Customization Audit", "desc": "Cataloging all custom CEMLIs, database wait events, SGA/PGA memory allocations, and storage bottlenecks."},
            {"step": "PHASE 02", "name": "Tuning & High-Availability Design", "desc": "Optimizing SQL execution plans, configuring RAC cache fusion, and setting up automated Data Guard replication."},
            {"step": "PHASE 03", "name": "Patching & Online Upgrade (ADOP)", "desc": "Executing dual-filesystem online patching with minimal business downtime and full rollback verification."},
            {"step": "PHASE 04", "name": "24x7 Managed DBA Support", "desc": "Providing continuous monitoring, automated backups, tablespace management, and SLA enforcement."}
        ],
        "qa": {
            "q": "How does Sumeru eliminate downtime during Oracle EBS maintenance and patching?",
            "a": "In Oracle EBS 12.2, we leverage Application DBA Online Patching (ADOP) with dual file systems (run and patch). All patching is applied and compiled while the system remains fully operational for business users, reducing production downtime to a brief 15-minute cutover window."
        }
    },
    {
        "id": "aws",
        "name": "Amazon Web Services (AWS)",
        "tag": "Consulting & Cloud Infrastructure Partner",
        "badge": "SECURE CLOUD ARCHITECTURE & MIGRATION",
        "logo": "/static/images/partners/aws.svg",
        "lead": "Enterprise cloud migration, hybrid infrastructure deployment, secure VPC networks, and high-resilience disaster recovery on AWS.",
        "desc": """Sumeru Technologies partners with Amazon Web Services to help enterprise organizations build scalable, resilient, and compliant cloud infrastructures. We design hybrid architectures that bridge on-premise data centers with elastic AWS cloud capabilities.

Our AWS practice adheres strictly to the AWS Well-Architected Framework, implementing multi-account landing zones, zero-trust network segregation, automated CI/CD deployment pipelines, and high-availability database architectures across multiple Availability Zones.""",
        "commitments": [
            "AWS Certified Solutions Architects and Cloud Security Specialists",
            "Strict compliance with AWS Well-Architected Framework (Security, Reliability, Performance, Cost)",
            "Guaranteed multi-AZ high availability with automated failover and sub-15 minute RTO",
            "Continuous FinOps cloud cost optimization eliminating idle resource spending",
            "SOC 2, ISO 27001, and HIPAA compliance mapping for regulated client workloads"
        ],
        "technologies": [
            "AWS EC2 & Auto Scaling", "Amazon RDS Multi-AZ & Aurora", "Amazon Elastic Kubernetes Service (EKS)",
            "AWS Transit Gateway & Direct Connect", "Amazon S3 & Glacier Archival", "AWS CloudWatch & CloudTrail", "Terraform & AWS CDK"
        ],
        "deliverables": [
            "AWS Enterprise Landing Zone & Multi-Account Architecture",
            "Hybrid Direct Connect & VPC Network Blueprint",
            "Containerized Microservices on EKS Specification",
            "Automated Multi-Region Disaster Recovery Runbook"
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Infrastructure Discovery & Migration Sizing", "desc": "Inventorying physical/virtual servers, storage requirements, network latency, and mapping AWS target instance types."},
            {"step": "PHASE 02", "name": "Landing Zone & Security Foundation", "desc": "Deploying AWS Control Tower, IAM Identity Center, transit routing, and encrypted KMS storage."},
            {"step": "PHASE 03", "name": "Workload Migration & Cloud Cutover", "desc": "Migrating databases using AWS DMS, deploying application containers, and validating traffic switching."},
            {"step": "PHASE 04", "name": "Continuous Managed Ops & Cost Governance", "desc": "Managing 24x7 monitoring, automated backups, security patching, and monthly FinOps cost reviews."}
        ],
        "qa": {
            "q": "How does Sumeru ensure cost efficiency and avoid unexpected cloud bills on AWS?",
            "a": "We implement continuous FinOps governance, auto-scaling policies, compute savings plans, and automated tiering to Amazon S3 Glacier for historical data. We conduct monthly cost optimization reviews that consistently reduce client cloud expenditures by 20% to 35%."
        }
    }
]

def main():
    target_file = os.path.join(os.path.dirname(__file__), "app", "services", "corporate_content.py")
    
    # Read the file
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()

    # We will import PAGES_DATA and update it
    import app.services.corporate_content as cc
    pages = cc.PAGES_DATA

    # Inject detailed_topics
    pages["/services/consulting"]["detailed_topics"] = etd.DETAILED_TOPICS_CONSULTING
    pages["/services/enterprise-solutions"]["detailed_topics"] = etd.DETAILED_TOPICS_ENTERPRISE_SOLUTIONS
    pages["/services/information-management"]["detailed_topics"] = etd.DETAILED_TOPICS_INFO_MGMT
    pages["/services/outsourcing"]["detailed_topics"] = etd.DETAILED_TOPICS_OUTSOURCING
    pages["/services/professional-services"]["detailed_topics"] = etd.DETAILED_TOPICS_PROF_SERVICES
    pages["/industries/logistics"]["detailed_topics"] = etd.DETAILED_TOPICS_LOGISTICS
    
    for route, topics in ADDITIONAL_TOPICS.items():
        if route in pages:
            pages[route]["detailed_topics"] = topics

    # Enrich /company/partners
    pages["/company/partners"]["partners"] = ENRICHED_PARTNERS
    pages["/company/partners"]["headline"] = "Strategic Technology & Certified Partner Ecosystem"
    pages["/company/partners"]["subhead"] = "Verified alliances with global enterprise leaders: certified competencies, binding commitments, and tested solution architectures."
    pages["/company/partners"]["overview"] = "True enterprise transformation is built on trusted alliances. Sumeru Technologies collaborates with the world's leading technology providers—Microsoft, SAP, Informatica, Kalido, Oracle, and AWS—to deliver certified, SLA-backed solutions. For each partnership, we maintain dedicated Centers of Excellence, certified practitioners, and binding commitments that protect client investments."

    # Now write the clean updated module
    import pprint
    
    header = '"""\nSumeru Technologies \u2014 Corporate Knowledge & Information Architecture Service\nProvides authoritative, verified corporate data for all website routes.\n"""\n\nfrom typing import Dict, Any, List\n\n'
    
    meta_repr = "CORPORATE_METADATA = " + pprint.pformat(cc.CORPORATE_METADATA, indent=4, width=120) + "\n\n"
    pages_repr = "PAGES_DATA: Dict[str, Dict[str, Any]] = " + pprint.pformat(pages, indent=4, width=120) + "\n"
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(header + meta_repr + pages_repr)

    print(f"Successfully enriched corporate_content.py! Total pages: {len(pages)}")

if __name__ == "__main__":
    main()
