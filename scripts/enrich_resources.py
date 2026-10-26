"""
Module: enrich_resources.py
Contains enriched topic cards for Resources, Technical Insights, Operational Perspectives, Whitepapers, and FAQs.
"""

RESOURCES_INSIGHTS_CARDS = [
    {
        "id": "insights-middleware",
        "slug": "insights-middleware",
        "nav_label": "Overcoming Middleware Fragmentation",
        "badge": "TECHNICAL INSIGHT • SYSTEMS INTEGRATION",
        "title": "Overcoming Middleware Fragmentation: Modernizing Enterprise Application Fabrics",
        "summary": "How enterprises running hybrid multi-cloud landscapes can replace brittle point-to-point batch connectors with resilient, event-driven API gateways and Kafka streams.",
        "lead": "How enterprises running hybrid multi-cloud landscapes can replace brittle point-to-point batch connectors with resilient, event-driven API gateways and Kafka streams.",
        "image": {
            "url": "/static/images/content/consulting_new2-580x400.jpg",
            "alt": "Enterprise Systems Integration Insight",
            "caption": "Modernizing Middleware Fabrics and API Gateways"
        },
        "content": [
            {
                "heading": "The Challenge of Brittle Point-to-Point Interfaces",
                "body": "As organizations grow through organic expansion and mergers, their IT landscapes accumulate hundreds of point-to-point batch scripts, legacy flat-file FTP jobs, and unversioned REST calls. When a single schema changes in the core ERP, downstream warehouse and billing systems fail silently.\n\nModernizing this fabric requires adopting a Canonical Data Model and decoupling producers from consumers via event-driven pub/sub brokers (such as Apache Kafka and SAP Event Mesh). By routing all transactional messages through centrally governed API gateways with mutual TLS and rate limiting, enterprises gain end-to-end auditability and eliminate interface failure cascades."
            },
            {
                "heading": "Architectural Recommendations",
                "body": "1. Mandate standard OpenAPI v3 / OData contracts for all new integrations.\n2. Wrap legacy systems in microservice adapters rather than modifying core database tables directly.\n3. Implement dead-letter queues (DLQ) with automated alert triage for unprocessable messages."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Interface Inventory Audit", "desc": "Cataloging point-to-point integrations and identifying failure-prone batch scripts."},
            {"step": "PHASE 02", "name": "Canonical Schema Standard", "desc": "Authoring enterprise-wide data contracts for customer, order, and invoice entities."},
            {"step": "PHASE 03", "name": "Event Mesh Backbone", "desc": "Deploying distributed Kafka/RabbitMQ clusters with guaranteed delivery semantics."},
            {"step": "PHASE 04", "name": "Telemetry Instrumentation", "desc": "Configuring distributed tracing with OpenTelemetry to track transaction lag across microservices."}
        ],
        "technologies": ["Apache Kafka", "MuleSoft Anypoint", "SAP Integration Suite", "OpenAPI v3", "OpenTelemetry", "Docker / Kubernetes"],
        "deliverables": [
            "Canonical Enterprise Integration Blueprint",
            "API Gateway Governance & Rate Limiting Policy",
            "Event-Driven Pub/Sub Queue Specification",
            "Interface Latency & Health Scorecard"
        ],
        "qa": {
            "q": "What is the primary architectural benefit of an event-driven integration mesh?",
            "a": "It completely decouples sender systems from receiver systems. If a receiving billing system is temporarily down for maintenance, incoming orders are safely buffered in the event broker and processed automatically once the system comes back online, ensuring zero transaction loss."
        },
        "sources": [
            {"title": "Enterprise Integration Patterns (Hohpe & Woolf)", "url": "https://www.enterpriseintegrationpatterns.com/", "sourceType": "industry", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    },
    {
        "id": "insights-clean-core",
        "slug": "insights-clean-core",
        "nav_label": "SAP Clean Core Architecture",
        "badge": "ERP STRATEGY • SAP CLEAN CORE",
        "title": "Decoupling Legacy Customizations: The Practical Guide to SAP Clean Core on BTP",
        "summary": "Moving from legacy ABAP modifications to side-by-side BTP microservices, preserving standard S/4HANA upgradeability while accelerating continuous innovation.",
        "lead": "Moving from legacy ABAP modifications to side-by-side BTP microservices, preserving standard S/4HANA upgradeability while accelerating continuous innovation.",
        "image": {
            "url": "/static/images/content/SAP-Solutions-1-580x400.jpg",
            "alt": "SAP Clean Core Guide",
            "caption": "Side-by-Side BTP Decoupling & Clean Core Governance"
        },
        "content": [
            {
                "heading": "The Death of Core Modifications",
                "body": "In traditional SAP ECC systems, organizations wrote thousands of custom Z-programs, user exits, and direct table modifications. While this met immediate departmental requests, it created massive technical debt that turned every support package upgrade into a painful, months-long code remediation project.\n\nSAP's Clean Core strategy mandates that the core ERP remains standard and upgrade-ready. All customizations are built either in-app using released extension points (such as BAdIs with restricted ABAP) or side-by-side on SAP Business Technology Platform (BTP). Side-by-side apps interact with S/4HANA strictly through stable, public OData APIs and business events."
            },
            {
                "heading": "Migration Sequencing",
                "body": "Using the SAP Custom Code Migration Worklist, Sumeru helps clients classify custom code into four buckets: retire (unused code), replace (standard SAP features now available), refactor (in-app BAdIs), and re-platform (side-by-side BTP extensions)."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Custom Code Audit", "desc": "Running automated ABAP test cockpit scans to identify non-compliant modifications."},
            {"step": "PHASE 02", "name": "BTP Extension Architecture", "desc": "Designing decoupled UI5/CAP applications hosted on SAP BTP Cloud Foundry/Kyma."},
            {"step": "PHASE 03", "name": "API & Event Broker Setup", "desc": "Configuring SAP Integration Suite and Event Mesh for asynchronous ledger updates."},
            {"step": "PHASE 04", "name": "Upgrade Simulation", "desc": "Executing simulated release upgrades in sandbox environments to prove 100% upgrade compatibility."}
        ],
        "technologies": ["SAP BTP", "ABAP Cloud", "Cloud Application Programming (CAP)", "SAP Fiori / UI5", "SAP Event Mesh", "OData v4"],
        "deliverables": [
            "Clean Core Migration Assessment & Scorecard",
            "Legacy Z-Code Remediation Roadmap",
            "BTP Side-by-Side Application Runtime Architecture",
            "Automated S/4HANA Upgrade Certification"
        ],
        "qa": {
            "q": "How long does a typical Clean Core custom code audit take?",
            "a": "A typical enterprise audit spans 3 to 4 weeks. Sumeru's automated scanning tools catalog all custom objects, dependencies, and execution logs, delivering an executive roadmap prioritized by business value and upgrade impact."
        },
        "sources": [
            {"title": "SAP Clean Core Strategy & Extensibility Guide", "url": "https://www.sap.com/products/technology-platform/clean-core.html", "sourceType": "vendor", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    },
    {
        "id": "insights-data-governance",
        "slug": "insights-data-governance",
        "nav_label": "Master Data Governance with Kalido",
        "badge": "DATA ARCHITECTURE • MDM",
        "title": "Harmonizing Enterprise Entities: Adaptive Master Data Management in M&A Environments",
        "summary": "How Kalido adaptive modeling and Informatica integration pipelines solve the critical challenge of customer and product duplication across merged corporate entities.",
        "lead": "How Kalido adaptive modeling and Informatica integration pipelines solve the critical challenge of customer and product duplication across merged corporate entities.",
        "image": {
            "url": "/static/images/content/Business-Intelligence-580x400.jpg",
            "alt": "Master Data Governance Insights",
            "caption": "Adaptive MDM Harmonization across Enterprise Systems"
        },
        "content": [
            {
                "heading": "The High Cost of Fragmented Master Data",
                "body": "When enterprises merge or acquire subsidiaries, they inherit conflicting customer databases, incompatible product taxonomies, and divergent charts of accounts. Forcing these systems into a rigid traditional MDM schema takes years and millions of dollars, frequently failing as business structures evolve.\n\nAdaptive Master Data Management—pioneered by Sumeru's partner Kalido—allows business models to adapt dynamically as organizational relationships change. Combined with Informatica Data Quality (IDQ) pipelines, our architecture applies fuzzy matching, address verification, and survivorship rules to create a single source of truth (golden records) without breaking existing subsidiary systems."
            },
            {
                "heading": "Operational Outcomes",
                "body": "Clients eliminate duplicate vendor disbursements, establish unified customer 360-degree views for cross-selling, and produce consolidated financial statements in hours rather than weeks."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Entity Discovery", "desc": "Profiling customer, vendor, and product schemas across all subsidiary databases."},
            {"step": "PHASE 02", "name": "Survivorship Rules", "desc": "Configuring automated rules to select the most reliable attributes into the golden record."},
            {"step": "PHASE 03", "name": "Stewardship Portal", "desc": "Deploying collaborative exception review workflows for business data stewards."},
            {"step": "PHASE 04", "name": "Real-Time Syndication", "desc": "Syndicating verified golden records back to ERP, CRM, and billing systems via message queues."}
        ],
        "technologies": ["Kalido Adaptive MDM", "Informatica MDM Hub", "Informatica Data Quality", "Kafka Syndication", "REST APIs"],
        "deliverables": [
            "Enterprise Master Data Governance Charter",
            "Domain Data Model & Matching Algorithm Blueprint",
            "Data Quality Rules Catalog",
            "Real-Time Golden Record Syndication Engine"
        ],
        "qa": {
            "q": "What happens if two source systems provide conflicting addresses for the same customer?",
            "a": "Our survivorship engine evaluates timestamps, source system authority weights (e.g. billing system over marketing portal), and Postal Service address verification APIs to automatically select and standardize the correct golden address."
        },
        "sources": [
            {"title": "Kalido Adaptive Information Architecture", "url": "https://sumerutechnologies.com/solutions/business-intelligence", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

print("enrich_resources.py defined.")
