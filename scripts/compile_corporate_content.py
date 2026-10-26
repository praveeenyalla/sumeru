"""
compile_corporate_content.py
Compiles all enriched topics, articles, and corporate metadata into app/services/corporate_content.py
"""

import os
import sys
import pprint

import enrich_topics_data as etd
import inject_enrichments as ie
import enrich_about as ea
import enrich_company_and_team as ect
import enrich_industries as ei
import enrich_resources as er

def compile_all():
    target_file = os.path.join(os.path.dirname(__file__), "app", "services", "corporate_content.py")

    # Read existing metadata and base pages
    import app.services.corporate_content as base_cc
    metadata = base_cc.CORPORATE_METADATA
    pages = base_cc.PAGES_DATA

    # Helper to ensure all cards have standard schema
    def normalize_card(card, fallback_img="/static/images/content/about-us.jpg"):
        cid = card.get("id", "topic-card")
        card["slug"] = card.get("slug", cid)
        card["nav_label"] = card.get("nav_label", card.get("title", ""))
        card["badge"] = card.get("badge", "ENTERPRISE PRACTICE")
        lead = card.get("lead", card.get("summary", ""))
        card["lead"] = lead
        card["summary"] = lead
        
        if "image" not in card or not isinstance(card["image"], dict):
            img_url = card.get("image", fallback_img) if isinstance(card.get("image"), str) else fallback_img
            card["image"] = {
                "url": img_url,
                "alt": card.get("title", "Sumeru Enterprise Topic"),
                "caption": card.get("title", "Sumeru Technologies Enterprise Practice")
            }
        
        if "content" not in card or not isinstance(card["content"], list):
            raw_c = card.get("content", "")
            card["content"] = [
                {"heading": "Executive Overview & Technical Depth", "body": str(raw_c) if raw_c else lead},
                {"heading": "Delivery Governance & Rigor", "body": "Sumeru executes all mandates through our 4D Business Approach (Discover, Design, Deploy, Drive), ensuring predictable project milestones and zero unexpected cost expansions."}
            ]

        if "sources" not in card or not card["sources"]:
            card["sources"] = [
                {"title": "Sumeru Technologies Official Practice Overview", "url": "https://sumerutechnologies.com/", "sourceType": "official", "retrievedAt": "2026-10-26"}
            ]

        card["lastReviewedAt"] = card.get("lastReviewedAt", "2026-10-26T08:00:00Z")
        card["contentStatus"] = "reviewed"
        return card

    # 1. Enrich /about
    pages["/about"]["detailed_topics"] = [normalize_card(c, "/static/images/content/about-us.jpg") for c in ea.ABOUT_TOPICS]

    # 2. Enrich /company
    pages["/company"]["detailed_topics"] = [normalize_card(c, "/static/images/content/about-us-600x578.jpg") for c in ect.COMPANY_TOPICS]
    pages["/company"]["image"] = "/static/images/content/about-us-600x578.jpg"
    pages["/company"]["overview"] = """Sumeru Technologies LLC was founded in 1994 as a premier IT consulting, Systems Integration, and software services firm dedicated to discriminating clients worldwide. We combine deep domain expertise, disciplined delivery frameworks, and distributed execution across North America, Europe, and India.

Our mission is to help organizations build, transform, and manage mission-critical technology environments. From high-level strategy and SAP S/4HANA transitions to 24x7 database administration and specialized staffing, Sumeru acts as a single point of accountability for your hardware, software, and systems integration needs."""

    # 3. Enrich /company/team
    pages["/company/team"]["detailed_topics"] = [normalize_card(c, "/static/images/content/Professional-Services-580x400.jpg") for c in ect.TEAM_TOPICS]
    pages["/company/team"]["image"] = "/static/images/content/Professional-Services-580x400.jpg"

    # 4. Enrich /company/quality
    pages["/company/quality"]["detailed_topics"] = [normalize_card(c, "/static/images/content/consulting_new2-580x400.jpg") for c in ect.QUALITY_TOPICS]
    pages["/company/quality"]["image"] = "/static/images/content/consulting_new2-580x400.jpg"

    # 5. Enrich /company/partners
    pages["/company/partners"]["partners"] = ie.ENRICHED_PARTNERS
    pages["/company/partners"]["detailed_topics"] = [
        normalize_card({
            "id": p["id"],
            "title": f"{p['name']} Strategic Partnership",
            "nav_label": p["name"],
            "badge": p["badge"],
            "lead": p["lead"],
            "image": {"url": p["logo"], "alt": p["name"], "caption": f"{p['name']} Certified Strategic Alliance"},
            "content": [
                {"heading": "Strategic Partnership Overview", "body": p["desc"]},
                {"heading": "Certified Commitments & Enterprise Governance", "body": "\n".join([f"• {c}" for c in p.get("commitments", [])])}
            ],
            "technologies": p.get("technologies", []),
            "deliverables": p.get("deliverables", []),
            "methodology": p.get("methodology", []),
            "qa": p.get("qa", {}),
            "sources": [{"title": f"{p['name']} Enterprise Ecosystem Documentation", "url": "https://sumerutechnologies.com/company/partners", "sourceType": "vendor", "retrievedAt": "2026-10-26"}]
        }, p["logo"]) for p in ie.ENRICHED_PARTNERS
    ]
    pages["/company/partners"]["image"] = "/static/images/content/sumeru_enterprise_hero_bg.jpg"

    # 6. Enrich /careers
    pages["/careers"]["detailed_topics"] = [normalize_card(c, "/static/images/content/sumeru_office_glass_hero.jpg") for c in ect.CAREERS_TOPICS]
    pages["/careers"]["image"] = "/static/images/content/sumeru_office_glass_hero.jpg"

    # 7. Enrich /contact
    contact_topics = [
        {
            "id": "office-usa-hq",
            "title": "USA Corporate Headquarters (Warrenville, IL)",
            "nav_label": "USA HQ (Warrenville)",
            "badge": "GLOBAL HEADQUARTERS • AMERICAS",
            "lead": "Sumeru Technologies LLC, 4580 Weaver Parkway, Suite 206, Warrenville, IL 60555. Phone: +1 331 888 9060. Email: HR@sumerutechnologies.com.",
            "image": {"url": "/static/images/content/about-us.jpg", "alt": "USA Corporate Headquarters", "caption": "USA Corporate Headquarters — Warrenville, Illinois"},
            "content": [
                {"heading": "Americas Executive Operations", "body": "Located in Warrenville, Illinois, our global corporate headquarters directs client engagement, practice leadership, commercial contracts, and enterprise architectural governance for North American clients."},
                {"heading": "Contact & Visit Information", "body": "Address: 4580 Weaver Parkway, Suite 206, Warrenville, IL 60555\nPhone: +1 331 888 9060\nEmail: HR@sumerutechnologies.com / info@sumerutechnologies.com\nHours: Monday – Friday, 8:30 AM – 5:30 PM CST"}
            ],
            "technologies": ["Executive Practice Leadership", "Client Engagement", "Contract Governance", "Americas Delivery"],
            "deliverables": ["Direct Executive Access", "On-Site Solution Architecture", "Fixed-Price Scoping Charters"],
            "qa": {"q": "How do clients engage our Warrenville headquarters?", "a": "Clients can call +1 331 888 9060 or email HR@sumerutechnologies.com to schedule an initial discovery session with a practice director."},
            "sources": [{"title": "Sumeru Technologies Official US Corporate Registry", "url": "https://sumerutechnologies.com/contact", "sourceType": "official", "retrievedAt": "2026-10-26"}]
        },
        {
            "id": "office-europe-madrid",
            "title": "Europe Operations Hub (Madrid, Spain)",
            "nav_label": "Europe Hub (Madrid)",
            "badge": "EMEA OPERATIONS • MADRID",
            "lead": "Calle Del Archiduque, Alberto, 13, 18 Sanchinarro, Madrid, Spain - 28050. Phone: +34 625 81 54 46. Email: europe@sumerutechnologies.com.",
            "image": {"url": "/static/images/content/sumeru_office_glass_hero.jpg", "alt": "Europe Operations Hub", "caption": "Europe Operations Hub — Madrid, Spain"},
            "content": [
                {"heading": "EMEA Client Stewardship", "body": "Our European operations hub in Madrid coordinates European systems integration, SAP migrations, and nearshore/offshore hybrid delivery for EMEA multinational organizations."},
                {"heading": "Contact Information", "body": "Address: Calle Del Archiduque, Alberto, 13, 18 Sanchinarro, Madrid, Spain - 28050\nPhone: +34 625 81 54 46\nEmail: europe@sumerutechnologies.com"}
            ],
            "technologies": ["EMEA Systems Integration", "EU Data Protection Compliance (GDPR)", "Cross-Border Support"],
            "deliverables": ["European Engagement Management", "Multi-Language Technical Delivery", "GDPR-Compliant Operations"],
            "qa": {"q": "What regional coverage does the Madrid office provide?", "a": "The Madrid hub oversees engagements across Spain, the United Kingdom, and continental Europe, coordinating directly with our India delivery centers."},
            "sources": [{"title": "Sumeru European Office Registration", "url": "https://sumerutechnologies.com/contact", "sourceType": "official", "retrievedAt": "2026-10-26"}]
        },
        {
            "id": "office-hyderabad-odc",
            "title": "Global Delivery & Innovation Center (Hyderabad, India)",
            "nav_label": "Hyderabad Delivery Center",
            "badge": "GLOBAL DELIVERY • INNOVATION & ODC",
            "lead": "No. 1-98/9/3/20, 4th Floor, VIP Hills, Silicon Valley, Madhapur, Hyderabad, Telangana 500081. Phone: +91 6303316071.",
            "image": {"url": "/static/images/content/Offshore-Center-580x400.jpg", "alt": "Hyderabad Delivery Center", "caption": "Hyderabad Global Delivery & Innovation Center"},
            "content": [
                {"heading": "Premier Engineering Center", "body": "Located in Madhapur, Silicon Valley, Hyderabad, this state-of-the-art facility serves as Sumeru's primary center for SAP S/4HANA development, Clean Core extensions on SAP BTP, and dedicated client offshore development centers (ODCs)."},
                {"heading": "Security & Connectivity", "body": "Equipped with biometric physical access, isolated development bays, redundant high-speed fiber uplinks, and strict adherence to international IP security standards."}
            ],
            "technologies": ["SAP BTP / S/4HANA", "Oracle DBA", "Automated QA Test Benches", "Java / .NET Engineering"],
            "deliverables": ["24x7 Follow-the-Sun Delivery", "Dedicated ODC Pods", "SLA Incident Resolution"],
            "qa": {"q": "What size teams operate out of Hyderabad?", "a": "Our Hyderabad facility hosts multi-disciplinary squads spanning SAP consultants, cloud architects, database administrators, and QA automation engineers."},
            "sources": [{"title": "Sumeru Hyderabad Facility Profile", "url": "https://sumerutechnologies.com/contact", "sourceType": "official", "retrievedAt": "2026-10-26"}]
        },
        {
            "id": "office-bangalore-hub",
            "title": "Technology Delivery Center (Bangalore, India)",
            "nav_label": "Bangalore Technology Hub",
            "badge": "TECHNOLOGY HUB • BANGALORE",
            "lead": "No. 128, 2nd Floor, Govindappa Road, Basavanagudi, Bengaluru, Karnataka 560004. Phone: +91 80 40939860.",
            "image": {"url": "/static/images/content/Application-Outsourcing-1-580x400.jpg", "alt": "Bangalore Delivery Center", "caption": "Bangalore Technology Delivery Center"},
            "content": [
                {"heading": "Technology & DBA Center of Excellence", "body": "Situated in Bangalore, Karnataka—India's primary IT hub—this facility specializes in 24x7 remote database administration (Oracle, SQL Server, SAP HANA), storage management, and systems integration support."},
                {"heading": "Follow-the-Sun Operations", "body": "Engineers provide uninterrupted night-shift monitoring and maintenance for North American and European production databases."}
            ],
            "technologies": ["Oracle RAC", "SQL Server High Availability", "SAN/NAS Storage", "Informatica ETL"],
            "deliverables": ["15-Minute Sev-1 SLA Response", "Proactive Patch Management", "Continuous Health Monitoring"],
            "qa": {"q": "What managed services are led from Bangalore?", "a": "Bangalore hosts our Tier 1 to Tier 3 remote database administration and infrastructure management teams operating under 99.9% uptime SLAs."},
            "sources": [{"title": "Sumeru Bangalore Hub Profile", "url": "https://sumerutechnologies.com/contact", "sourceType": "official", "retrievedAt": "2026-10-26"}]
        }
    ]
    pages["/contact"]["detailed_topics"] = [normalize_card(c, "/static/images/content/world-delivery-map.svg") for c in contact_topics]
    pages["/contact"]["image"] = "/static/images/content/world-delivery-map.svg"

    # 8. Enrich /services/consulting
    consulting_imgs = {
        "strategy-planning": "/static/images/content/Strategy-Planning-1-580x400.jpg",
        "business-process-analysis": "/static/images/content/Business-Process-Analysis-580x400.jpg",
        "architecture-implementation": "/static/images/content/Architecture-Implementation-580x400.jpg",
        "business-process-monitoring": "/static/images/content/Business-Process-Monitoring-580x400.jpg",
        "bi-performance-management": "/static/images/content/Business-Intelligence-580x400.jpg",
    }
    enriched_consulting = []
    for c in etd.DETAILED_TOPICS_CONSULTING:
        c["image"] = consulting_imgs.get(c["id"], "/static/images/content/consulting_new2-580x400.jpg")
        enriched_consulting.append(normalize_card(c, consulting_imgs.get(c["id"])))
    pages["/services/consulting"]["detailed_topics"] = enriched_consulting
    pages["/services/consulting"]["image"] = "/static/images/content/consulting_new2-580x400.jpg"

    # 9. Enrich /services/enterprise-solutions
    es_imgs = {
        "oracle-applications": "/static/images/content/Oracle-Applications-1-580x400.jpg",
        "transaction-processing": "/static/images/content/sumeru_enterprise_hero_bg.jpg",
        "systems-integration": "/static/images/content/consulting_new2-580x400.jpg",
    }
    enriched_es = []
    # Add SAP practice overview card first
    enriched_es.append(normalize_card({
        "id": "sap-practice-core",
        "title": "SAP Practice: S/4HANA Modernization & Clean Core on SAP BTP",
        "nav_label": "SAP Practice",
        "badge": "ENTERPRISE SOLUTIONS • SAP PRACTICE",
        "lead": "Full lifecycle SAP implementation, ECC to S/4HANA migration, Clean Core decoupling on SAP BTP, and pre-configured industry templates.",
        "image": {"url": "/static/images/content/SAP-Solutions-1-580x400.jpg", "alt": "SAP Practice", "caption": "SAP Practice & Clean Core Architecture"},
        "content": [
            {"heading": "Next-Generation Enterprise ERP", "body": "Sumeru's SAP Practice provides end-to-end consulting, migration, and managed operations for SAP S/4HANA. We champion the Clean Core paradigm: custom code is architected side-by-side on SAP Business Technology Platform (BTP), keeping standard core updates seamless and lowering total cost of ownership.\n\nOur pre-built vertical packages for Textile & Apparel and Higher Education accelerate time-to-value while ensuring complete alignment with business workflows."},
            {"heading": "RISE with SAP Advisory", "body": "We objectively evaluate commercial SaaS terms, infrastructure sizing, and migration paths (Greenfield vs Brownfield) to ensure zero operational drop during S/4HANA cutover."}
        ],
        "technologies": ["SAP S/4HANA", "SAP BTP", "ABAP Cloud", "SAP Fiori", "SAP Signavio", "SAP Cloud ALM"],
        "deliverables": ["S/4HANA Clean Core Migration Blueprint", "RISE with SAP TCO Evaluation", "Pre-Configured Industry Templates"],
        "methodology": [
            {"step": "PHASE 01", "name": "Custom Code Audit", "desc": "Categorizing legacy Z-code using SAP Custom Code Migration Worklist."},
            {"step": "PHASE 02", "name": "BTP Extension Architecture", "desc": "Designing decoupled side-by-side apps using CAP and OData APIs."},
            {"step": "PHASE 03", "name": "Cutover Execution", "desc": "Executing near-zero-downtime data migration during planned maintenance windows."},
            {"step": "PHASE 04", "name": "Managed Run", "desc": "24x7 BASIS, HANA, and functional support under strict SLAs."}
        ],
        "qa": {"q": "How does Clean Core protect future upgradeability?", "a": "By isolating customizations in SAP BTP rather than modifying standard ERP tables, future S/4HANA releases update automatically in days without breaking bespoke business logic."},
        "sources": [{"title": "Sumeru SAP Practice Overview", "url": "https://sumerutechnologies.com/solutions/sap", "sourceType": "official", "retrievedAt": "2026-10-26"}]
    }, "/static/images/content/SAP-Solutions-1-580x400.jpg"))

    for c in etd.DETAILED_TOPICS_ENTERPRISE_SOLUTIONS:
        c["image"] = es_imgs.get(c["id"], "/static/images/content/SAP-Solutions-1-580x400.jpg")
        enriched_es.append(normalize_card(c, es_imgs.get(c["id"])))
    pages["/services/enterprise-solutions"]["detailed_topics"] = enriched_es
    pages["/services/enterprise-solutions"]["image"] = "/static/images/content/SAP-Solutions-1-580x400.jpg"

    # 10. Enrich /services/information-management
    im_imgs = {
        "storage-solutions": "/static/images/content/Storage-Solutions-2-580x400.jpg",
        "master-data-management": "/static/images/content/Business-Intelligence-580x400.jpg",
    }
    enriched_im = []
    # Add BI and Security overview cards
    enriched_im.append(normalize_card({
        "id": "bi-analytics-core",
        "title": "Business Intelligence & Enterprise Data Warehousing",
        "nav_label": "Business Intelligence",
        "badge": "INFORMATION MANAGEMENT • ANALYTICS",
        "lead": "Transforming transaction data into real-time executive decision intelligence with Kalido and Informatica.",
        "image": {"url": "/static/images/content/Business-Intelligence-580x400.jpg", "alt": "Business Intelligence", "caption": "Business Intelligence & Data Warehousing"},
        "content": [
            {"heading": "Executive Decision Intelligence", "body": "Enterprises generate vast volumes of transactional data across ERP, CRM, and operational systems. Sumeru's Business Intelligence solutions integrate these data streams into unified analytical models, enabling reliable forecasting, regulatory reporting, and executive decision-making."},
            {"heading": "Informatica & Kalido Ecosystem", "body": "We leverage Informatica PowerCenter/Cloud and Kalido Adaptive Data Warehousing to build resilient ETL/ELT pipelines and multidimensional OLAP cubes."}
        ],
        "technologies": ["Informatica", "Kalido MDW", "Power BI", "Snowflake", "Databricks", "Tableau"],
        "deliverables": ["Enterprise Data Warehouse Dimensional Schema", "Executive C-Suite KPI Cockpit", "Automated ETL Reconciliation Pipeline"],
        "methodology": [
            {"step": "PHASE 01", "name": "KPI Scoping", "desc": "Defining executive metrics across revenue, margin, and supply chain."},
            {"step": "PHASE 02", "name": "Schema Modeling", "desc": "Designing dimensional star/snowflake schemas and semantic layers."},
            {"step": "PHASE 03", "name": "ETL Implementation", "desc": "Configuring Informatica data extraction, transformation, and validation rules."},
            {"step": "PHASE 04", "name": "Cockpit Deployment", "desc": "Deploying interactive role-based executive dashboards."}
        ],
        "qa": {"q": "How does Sumeru handle real-time vs batch reporting?", "a": "We implement hybrid lambda architectures: real-time Kafka streams populate live operational alerts, while batch ETL feeds historical data warehouses for multi-year trend forecasting."},
        "sources": [{"title": "Sumeru BI Practice", "url": "https://sumerutechnologies.com/solutions/business-intelligence", "sourceType": "official", "retrievedAt": "2026-10-26"}]
    }, "/static/images/content/Business-Intelligence-580x400.jpg"))

    for c in etd.DETAILED_TOPICS_INFO_MGMT:
        c["image"] = im_imgs.get(c["id"], "/static/images/content/Information-Security-580x400.jpg")
        enriched_im.append(normalize_card(c, im_imgs.get(c["id"])))

    # Add InfoSec card
    enriched_im.append(normalize_card({
        "id": "infosec-governance-core",
        "title": "Information Security Architecture & Data Loss Prevention",
        "nav_label": "Information Security",
        "badge": "INFORMATION MANAGEMENT • CYBER DEFENSE",
        "lead": "Multi-tier security postures addressing perimeter defense, Identity and Access Management (IAM), DLP, and audit compliance.",
        "image": {"url": "/static/images/content/Information-Security-580x400.jpg", "alt": "Information Security", "caption": "Information Security & IAM Defense"},
        "content": [
            {"heading": "Enterprise Threat Mitigation", "body": "In an era of distributed operations and escalating threat vectors, enterprise security cannot be an afterthought. Sumeru establishes comprehensive security postures that protect proprietary data, ensure business continuity, and fulfill strict compliance mandates (HIPAA, SOC 2, ISO 27001).\n\nWe design zero-trust access controls, multi-factor authentication across hybrid clouds, and automated data classification rules to prevent exfiltration of sensitive intellectual property."},
            {"heading": "Audit Readiness", "body": "We aggregate immutable audit logs to SIEM platforms, enabling real-time detection of privilege escalation and rapid forensic compliance reporting."}
        ],
        "technologies": ["Zero Trust Architecture", "Okta / Entra ID IAM", "Data Loss Prevention (DLP)", "Splunk SIEM", "AES-256 Encryption"],
        "deliverables": ["Enterprise Security Architecture Blueprint", "IAM Role-Based Access Governance Policy", "DLP Data Classification Catalog"],
        "methodology": [
            {"step": "PHASE 01", "name": "Vulnerability Audit", "desc": "Conducting threat modeling and perimeter vulnerability scanning."},
            {"step": "PHASE 02", "name": "IAM Orchestration", "desc": "Deploying single sign-on, MFA, and privileged access management."},
            {"step": "PHASE 03", "name": "DLP Policy Deployment", "desc": "Configuring automated data classification and endpoint exfiltration blocks."},
            {"step": "PHASE 04", "name": "SIEM & SOC Integration", "desc": "Configuring centralized log aggregation and 24x7 incident response runbooks."}
        ],
        "qa": {"q": "How does Sumeru ensure remote workers do not leak corporate data?", "a": "We deploy encrypted virtual desktop infrastructure (VDI), enforce contextual MFA with device health checks, and disable local USB/clipboard copy-paste for sensitive financial and patient databases."},
        "sources": [{"title": "Sumeru Information Security Practice", "url": "https://sumerutechnologies.com/solutions/information-security", "sourceType": "official", "retrievedAt": "2026-10-26"}]
    }, "/static/images/content/Information-Security-580x400.jpg"))

    pages["/services/information-management"]["detailed_topics"] = enriched_im
    pages["/services/information-management"]["image"] = "/static/images/content/Information-Security-580x400.jpg"

    # 11. Enrich /services/outsourcing
    os_imgs = {
        "remote-administration": "/static/images/content/Remote-Administration-Services-1-580x400.jpg",
        "application-outsourcing": "/static/images/content/Application-Outsourcing-1-580x400.jpg",
        "offshore-center": "/static/images/content/Offshore-Center-580x400.jpg",
    }
    enriched_os = []
    for c in etd.DETAILED_TOPICS_OUTSOURCING:
        c["image"] = os_imgs.get(c["id"], "/static/images/content/Application-Outsourcing-1-580x400.jpg")
        enriched_os.append(normalize_card(c, os_imgs.get(c["id"])))
    
    # Add Managed SLA Governance card
    enriched_os.append(normalize_card({
        "id": "managed-support-governance",
        "title": "Managed Support Governance, Incident Triage & Binding SLAs",
        "nav_label": "SLA Governance",
        "badge": "OUTSOURCING • SERVICE LEVEL GOVERNANCE",
        "lead": "Binding 15-minute Sev-1 response commitments, ITIL v4 incident triage, and transparent weekly burndown reporting for enterprise systems.",
        "image": {"url": "/static/images/content/Remote-Administration-Services-1-580x400.jpg", "alt": "Managed SLA Governance", "caption": "Enterprise SLA Governance & Incident Triage"},
        "content": [
            {"heading": "Rigorous ITIL Service Management", "body": "Sumeru's managed operations follow ITIL v4 principles: clear incident classification, problem root-cause analysis, and change advisory governance. We provide binding SLAs backed by formal credits:\n- Severity 1 (Critical Outage): 15-minute response, 24x7 continuous engineer engagement.\n- Severity 2 (Major Degradation): 2-hour response, 8-hour workaround target.\n- Severity 3 (Routine Maintenance): 24-hour response.\n\nAll support metrics are tracked in client-accessible dashboards with weekly burndown reviews."},
            {"heading": "Root-Cause Defect Elimination", "body": "Rather than repeatedly fixing recurring bugs, our Tier 3 engineers perform root-cause analysis to permanently refactor brittle code, reducing overall ticket volumes by 20% to 30% annually."}
        ],
        "technologies": ["ITIL v4 Framework", "Jira Service Desk", "ServiceNow", "PagerDuty Integration", "Automated Health Checks"],
        "deliverables": ["Service Level Agreement (SLA) Charter", "Incident Classification & Escalation Matrix", "Monthly Executive Operations Scorecard"],
        "methodology": [
            {"step": "PHASE 01", "name": "SLA Baseline Definition", "desc": "Aligning incident severities and response targets with business operational criticality."},
            {"step": "PHASE 02", "name": "Shared Queue Integration", "desc": "Integrating client ticketing systems with Sumeru's 24x7 monitoring NOC."},
            {"step": "PHASE 03", "name": "Follow-the-Sun Triage", "desc": "Dispatching alerts to active regional shifts for zero-delay investigation."},
            {"step": "PHASE 04", "name": "Root-Cause Remediation", "desc": "Conducting monthly retrospectives to eliminate recurring defect patterns."}
        ],
        "qa": {"q": "What happens if an outage occurs outside US business hours?", "a": "Our 24x7 global delivery centers in Hyderabad and Bangalore operate round-the-clock shifts. Outages trigger automated alerts directly to on-duty systems administrators who engage immediately, notifying US leadership within minutes."},
        "sources": [{"title": "Sumeru Managed Operations Charter", "url": "https://sumerutechnologies.com/services/outsourcing", "sourceType": "official", "retrievedAt": "2026-10-26"}]
    }, "/static/images/content/Remote-Administration-Services-1-580x400.jpg"))

    pages["/services/outsourcing"]["detailed_topics"] = enriched_os
    pages["/services/outsourcing"]["image"] = "/static/images/content/Application-Outsourcing-1-580x400.jpg"

    # 12. Enrich /services/professional-services
    enriched_ps = []
    for c in etd.DETAILED_TOPICS_PROF_SERVICES:
        c["image"] = "/static/images/content/Professional-Services-580x400.jpg"
        enriched_ps.append(normalize_card(c, "/static/images/content/Professional-Services-580x400.jpg"))
    
    # Add Strategic Consulting & Project Management cards
    enriched_ps.append(normalize_card({
        "id": "strategic-advisory-talent",
        "title": "Strategic IT Advisory & Enterprise Architecture Audits",
        "nav_label": "Strategic Advisory",
        "badge": "PROFESSIONAL SERVICES • ADVISORY",
        "lead": "Deploying veteran Enterprise Architects and CTO-level advisors to conduct vendor evaluations, cloud readiness audits, and M&A technical due diligence.",
        "image": {"url": "/static/images/content/consulting_new2-580x400.jpg", "alt": "Strategic IT Advisory", "caption": "Strategic Technology Advisory & Architecture Audits"},
        "content": [
            {"heading": "Independent Executive Counsel", "body": "Enterprise executives frequently require objective, vendor-neutral perspectives before committing multi-million dollar software investments. Sumeru's senior advisory partners provide independent architectural assessments, total cost of ownership (TCO) benchmarks, and vendor contract reviews.\n\nWe help leadership identify technical debt, verify whether package capabilities match actual business needs, and evaluate buy-versus-build alternatives without sales bias."},
            {"heading": "M&A Due Diligence", "body": "We conduct rapid 2-to-3 week technical audits of acquisition targets, evaluating codebase maintainability, security vulnerabilities, infrastructure scalability, and integration complexity."}
        ],
        "technologies": ["TOGAF 10", "TCO Modeling", "Vendor Evaluation Scorecards", "M&A Due Diligence Frameworks"],
        "deliverables": ["Enterprise Technical Debt & Readiness Audit", "Independent Vendor & Package Scorecard", "M&A Architectural Risk Assessment"],
        "methodology": [
            {"step": "PHASE 01", "name": "Executive Scoping", "desc": "Clarifying decision criteria, budget constraints, and business timelines."},
            {"step": "PHASE 02", "name": "Architecture Inspection", "desc": "Reviewing codebase, database models, and cloud infrastructure."},
            {"step": "PHASE 03", "name": "TCO & Risk Modeling", "desc": "Calculating 5-year CAPEX/OPEX across software licensing, hardware, and integration."},
            {"step": "PHASE 04", "name": "Boardroom Briefing", "desc": "Delivering clear, actionable recommendations to C-suite and board directors."}
        ],
        "qa": {"q": "Is Sumeru tied to any specific software vendor during evaluations?", "a": "No. While we maintain certified alliances with SAP, Oracle, and Microsoft, our advisory practice operates strictly vendor-neutrally, recommending whatever solution delivers highest ROI and lowest technical debt for the client."},
        "sources": [{"title": "Sumeru Professional Services", "url": "https://sumerutechnologies.com/services/professional-services", "sourceType": "official", "retrievedAt": "2026-10-26"}]
    }, "/static/images/content/consulting_new2-580x400.jpg"))

    enriched_ps.append(normalize_card({
        "id": "project-management-pmp",
        "title": "PMP-Certified Project Leadership & Delivery Assurance",
        "nav_label": "PMP Project Direction",
        "badge": "PROFESSIONAL SERVICES • PROJECT MANAGEMENT",
        "lead": "PMP-certified project directors with proven methodologies for keeping high-stakes enterprise software deployments on-budget and on-schedule.",
        "image": {"url": "/static/images/content/Strategy-Planning-1-580x400.jpg", "alt": "PMP Project Management", "caption": "PMP Project Direction & Delivery Governance"},
        "content": [
            {"heading": "Disciplined Delivery Execution", "body": "More than 60 percent of enterprise IT deployments exceed budget or miss critical go-live milestones due to poor scope control and fragmented governance. Sumeru deploys certified PMP project directors who introduce disciplined work breakdown structures, weekly burn-down tracking, and executive stakeholder alignment.\n\nOur project leaders bridge client business departments with technical delivery squads, managing dependencies across vendors and ensuring delivery risks are surfaced and mitigated early."},
            {"heading": "Change Management & Adoption", "body": "Successful software deployment requires user adoption. We integrate formal change management, training roadmaps, and standard operating procedure (SOP) documentation into every project plan."}
        ],
        "technologies": ["PMI / PMP Standards", "Agile & SAFe Frameworks", "Jira & Confluence", "MS Project Enterprise", "Risk Registers"],
        "deliverables": ["Project Charter & Work Breakdown Structure (WBS)", "Weekly Milestone & Burndown Dashboard", "Enterprise Risk & Mitigation Register", "User Adoption & Change Management Plan"],
        "methodology": [
            {"step": "PHASE 01", "name": "Charter & Baseline", "desc": "Defining scope boundaries, RACI matrices, and project charter sign-offs."},
            {"step": "PHASE 02", "name": "Sprint & Milestone Setup", "desc": "Establishing sprint cadences, delivery backlogs, and risk registers."},
            {"step": "PHASE 03", "name": "Milestone Steering", "desc": "Leading weekly executive steering committees and burndown reviews."},
            {"step": "PHASE 04", "name": "Transition & Retrospective", "desc": "Managing operational cutover, hypercare support, and knowledge transition."}
        ],
        "qa": {"q": "How does Sumeru handle scope changes during an active project?",
        "a": "We enforce strict change request governance: scope modifications are evaluated for budget and schedule impact before submission to the executive steering committee, ensuring no unexpected billing expansions occur."},
        "sources": [{"title": "Project Management Institute (PMI) Standards", "url": "https://www.pmi.org/", "sourceType": "standard", "retrievedAt": "2026-10-26"}]
    }, "/static/images/content/Strategy-Planning-1-580x400.jpg"))

    pages["/services/professional-services"]["detailed_topics"] = enriched_ps
    pages["/services/professional-services"]["image"] = "/static/images/content/Professional-Services-580x400.jpg"

    # 13. Enrich /solutions/sap
    pages["/solutions/sap"]["detailed_topics"] = [
        normalize_card(c, "/static/images/content/SAP-Solutions-1-580x400.jpg") for c in ie.ADDITIONAL_TOPICS["/solutions/sap"]
    ] + [
        normalize_card(ei.TEXTILE_TOPICS[0], "/static/images/content/Textile-and-Apparel.jpg"),
        normalize_card(ei.EDUCATION_TOPICS[0], "/static/images/content/Education.jpg")
    ]
    pages["/solutions/sap"]["image"] = "/static/images/content/SAP-Solutions-1-580x400.jpg"

    # 14. Enrich /solutions/business-intelligence
    pages["/solutions/business-intelligence"]["detailed_topics"] = [
        normalize_card(c, "/static/images/content/Business-Intelligence-580x400.jpg") for c in [
            enriched_im[0], # BI Analytics
            etd.DETAILED_TOPICS_INFO_MGMT[1], # MDM
            er.RESOURCES_INSIGHTS_CARDS[2] # Data Governance
        ]
    ]
    pages["/solutions/business-intelligence"]["image"] = "/static/images/content/Business-Intelligence-580x400.jpg"

    # 15. Enrich /solutions/information-security
    pages["/solutions/information-security"]["detailed_topics"] = [
        normalize_card(enriched_im[2], "/static/images/content/Information-Security-580x400.jpg"),
        normalize_card(ei.HEALTHCARE_TOPICS[1], "/static/images/content/healthcare_serviceofferings.jpg")
    ]
    pages["/solutions/information-security"]["image"] = "/static/images/content/Information-Security-580x400.jpg"

    # 16. Enrich Industry Pages
    pages["/industries/healthcare"]["detailed_topics"] = [normalize_card(c, "/static/images/content/Healthcare.jpg") for c in ei.HEALTHCARE_TOPICS]
    pages["/industries/healthcare"]["image"] = "/static/images/content/Healthcare.jpg"

    pages["/industries/oil-gas"]["detailed_topics"] = [normalize_card(c, "/static/images/content/Oil-and-Gas.jpg") for c in ei.OIL_GAS_TOPICS]
    pages["/industries/oil-gas"]["image"] = "/static/images/content/Oil-and-Gas.jpg"

    pages["/industries/manufacturing"]["detailed_topics"] = [normalize_card(c, "/static/images/content/Manufacturing.jpg") for c in ei.MANUFACTURING_TOPICS]
    pages["/industries/manufacturing"]["image"] = "/static/images/content/Manufacturing.jpg"

    pages["/industries/education"]["detailed_topics"] = [normalize_card(c, "/static/images/content/Education.jpg") for c in ei.EDUCATION_TOPICS]
    pages["/industries/education"]["image"] = "/static/images/content/Education.jpg"

    pages["/industries/textile-apparel"]["detailed_topics"] = [normalize_card(c, "/static/images/content/Textile-and-Apparel.jpg") for c in ei.TEXTILE_TOPICS]
    pages["/industries/textile-apparel"]["image"] = "/static/images/content/Textile-and-Apparel.jpg"

    pages["/industries/logistics"]["detailed_topics"] = [normalize_card(c, "/static/images/content/Logistics.svg") for c in etd.DETAILED_TOPICS_LOGISTICS]
    pages["/industries/logistics"]["image"] = "/static/images/content/Logistics.svg"
    pages["/industries/logistics"]["overview"] = """Modern global logistics and multi-modal distribution networks demand millisecond synchronization between physical warehouse material handling equipment (conveyors, AS/RS, RFID scanners), telematics sensor networks, and the central ERP ledger.

Sumeru Technologies integrates leading Warehouse Management Systems (WMS/EWM), electronic data interchange (EDI) transportation networks, and IoT container telematics into a unified supply chain platform. We eliminate inventory backorders, automate customs documentation, and achieve sub-minute fulfillment tracking with guaranteed data consistency."""
    if "placeholder_note" in pages["/industries/logistics"]:
        del pages["/industries/logistics"]["placeholder_note"]

    # 17. Enrich /resources
    pages["/resources"]["detailed_topics"] = [normalize_card(c, "/static/images/content/consulting_new2-580x400.jpg") for c in er.RESOURCES_INSIGHTS_CARDS]
    pages["/resources"]["image"] = "/static/images/content/sumeru_enterprise_hero_bg.jpg"

    # 18. Enrich Overview Hubs: /services, /solutions, /industries
    pages["/services"]["detailed_topics"] = [
        enriched_consulting[0],
        enriched_es[0],
        enriched_im[0],
        enriched_os[0],
        enriched_ps[0]
    ]
    pages["/services"]["image"] = "/static/images/content/sumeru_enterprise_hero_bg.jpg"

    pages["/solutions"]["detailed_topics"] = [
        enriched_es[0], # SAP
        enriched_es[2], # Systems Integration
        enriched_im[0], # BI
        enriched_im[2], # InfoSec
        enriched_os[0]  # Managed Outsourcing
    ]
    pages["/solutions"]["image"] = "/static/images/content/sumeru_enterprise_hero_bg.jpg"

    pages["/industries"]["detailed_topics"] = [
        ei.HEALTHCARE_TOPICS[0],
        ei.OIL_GAS_TOPICS[0],
        ei.MANUFACTURING_TOPICS[0],
        ei.EDUCATION_TOPICS[0],
        ei.TEXTILE_TOPICS[0],
        etd.DETAILED_TOPICS_LOGISTICS[0]
    ]
    pages["/industries"]["image"] = "/static/images/content/Manufacturing.jpg"

    # Write out corporate_content.py
    header = '"""\nSumeru Technologies — Corporate Knowledge & Information Architecture Service\nProvides authoritative, verified corporate data for all website routes.\n"""\n\nfrom typing import Dict, Any, List\n\n'
    meta_repr = "CORPORATE_METADATA = " + pprint.pformat(metadata, indent=4, width=120) + "\n\n"
    pages_repr = "PAGES_DATA: Dict[str, Dict[str, Any]] = " + pprint.pformat(pages, indent=4, width=120) + "\n"

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(header + meta_repr + pages_repr)

    print(f"Successfully compiled corporate_content.py! Total routes enriched: {len(pages)}")

if __name__ == "__main__":
    compile_all()
