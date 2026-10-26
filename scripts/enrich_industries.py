"""
Module: enrich_industries.py
Contains enriched topic cards for Healthcare, Oil & Gas, Manufacturing, Education, Textile & Apparel, and Logistics.
"""

HEALTHCARE_TOPICS = [
    {
        "id": "his-implementation",
        "slug": "his-implementation",
        "nav_label": "Hospital Information Systems (HIS)",
        "badge": "HEALTHCARE • CLINICAL INTEGRATION",
        "title": "Hospital Information Systems (HIS) & Clinical-Financial Integration",
        "summary": "Configurable, compliant enterprise architectures to manage and integrate clinical, financial, and operational workflows across greenfield and existing hospital networks.",
        "lead": "Configurable, compliant enterprise architectures to manage and integrate clinical, financial, and operational workflows across greenfield and existing hospital networks.",
        "image": {
            "url": "/static/images/content/Healthcare.jpg",
            "alt": "Healthcare Information Systems",
            "caption": "Hospital Information Systems & Clinical-Financial Architecture"
        },
        "content": [
            {
                "heading": "Clinical & Financial Synergy",
                "body": "The global healthcare industry is constantly evolving due to new medical research, shifting reimbursement models, and stringent regulatory oversight. As healthcare providers expand, the importance of configurable systems that integrate clinical, financial, and operational information becomes paramount.\n\nA robust Hospital Information System (HIS) that keeps pace with changing trends is the most effective way to deliver high-quality care while maintaining fiscal sustainability. At Sumeru Technologies, we possess rich experience implementing HIS across existing multi-site health systems and greenfield hospital networks."
            },
            {
                "heading": "End-to-End SDLC & Product Development",
                "body": "Our dedicated Healthcare Practice provides technical design, project management, and complete SDLC execution for healthcare software vendors and hospital networks, ensuring systems meet ARRA/HITECH standards and clinical workflow requirements."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Clinical Workflow Discovery", "desc": "Mapping departmental intake, nursing notes, pharmacy orders, and billing capture."},
            {"step": "PHASE 02", "name": "HIS Architecture & Customization", "desc": "Configuring modular clinical modules and integrating financial ledgers."},
            {"step": "PHASE 03", "name": "HL7 & EHR Interface Integration", "desc": "Connecting lab analyzers, PACS imaging servers, and external EHR systems."},
            {"step": "PHASE 04", "name": "Clinical Go-Live & Hypercare", "desc": "Conducting dual-run verification, nurse training, and 24x7 clinical cutover support."}
        ],
        "technologies": ["HL7 v2 / v3", "FHIR APIs", "DICOM & PACS", "Cerner / Epic Integration", "HIPAA Compliance", "SAP Healthcare"],
        "deliverables": [
            "Hospital Information System Architecture Document",
            "Clinical-Financial Workflow Integration Blueprint",
            "HL7 Interface Engine Specification & Test Log",
            "Clinical User Training & Go-Live Readiness Plan"
        ],
        "qa": {
            "q": "How does Sumeru ensure patient care is not disrupted during an HIS upgrade?",
            "a": "We use phased departmental rollouts and simulated clinical walkthroughs during off-peak shifts. Shadow environments run concurrently with legacy systems to verify prescription verification and patient record sync before final cutover."
        },
        "sources": [
            {"title": "Sumeru Healthcare IT Practice", "url": "https://sumerutechnologies.com/industries/healthcare", "sourceType": "official", "retrievedAt": "2026-10-26"},
            {"title": "HL7 International Healthcare Interoperability Standards", "url": "https://www.hl7.org/", "sourceType": "standard", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    },
    {
        "id": "hipaa-phi-security",
        "slug": "hipaa-phi-security",
        "nav_label": "HIPAA & PHI Security",
        "badge": "HEALTHCARE • DATA PRIVACY & COMPLIANCE",
        "title": "HIPAA Compliance, PHI Encryption & Healthcare Security Architecture",
        "summary": "Multi-tier security postures enforcing end-to-end Protected Health Information (PHI) encryption, role-based clinician access, and immutable audit logging.",
        "lead": "Multi-tier security postures enforcing end-to-end Protected Health Information (PHI) encryption, role-based clinician access, and immutable audit logging.",
        "image": {
            "url": "/static/images/content/healthcare_serviceofferings.jpg",
            "alt": "Healthcare Security and Compliance",
            "caption": "HIPAA Privacy, PHI Encryption & Audit Governance"
        },
        "content": [
            {
                "heading": "Strict Regulatory Protection",
                "body": "Healthcare IT systems involve complex health information exchange across doctors, diagnostic labs, payers, and pharmacies. Designing such systems requires deep subject matter expertise to ensure full compliance with the Health Insurance Portability and Accountability Act (HIPAA) and regional data privacy standards.\n\nSumeru designs zero-trust healthcare environments with AES-256 field-level encryption for electronic Protected Health Information (ePHI), strict role-based access control (RBAC), and automated auditing of every record viewed or modified."
            },
            {
                "heading": "Audit Readiness & Breach Prevention",
                "body": "We implement continuous compliance monitoring and SIEM log aggregation to detect unauthorized access attempts instantly, ensuring healthcare providers maintain flawless audit readiness."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "PHI Data Flow Audit", "desc": "Identifying all databases, APIs, and portable devices storing or transmitting patient data."},
            {"step": "PHASE 02", "name": "Encryption & Key Management", "desc": "Deploying hardware security modules (HSMs) and automated key rotation for data at rest and in transit."},
            {"step": "PHASE 03", "name": "Clinician IAM Governance", "desc": "Configuring biometric and badge-tap single sign-on (SSO) with emergency 'break-glass' protocols."},
            {"step": "PHASE 04", "name": "Compliance Certification", "desc": "Conducting third-party penetration testing and authoring HIPAA compliance validation reports."}
        ],
        "technologies": ["HIPAA Security Rule", "HITECH Compliance", "AES-256 / TLS 1.3", "OAuth2 / SMART on FHIR", "Splunk Healthcare SIEM"],
        "deliverables": [
            "HIPAA Security & Risk Assessment Report",
            "PHI Encryption & Key Management Architecture",
            "Clinician Role-Based Access Governance Policy",
            "Healthcare Incident Response & Breach Notification Plan"
        ],
        "qa": {
            "q": "How does Sumeru balance strict HIPAA security with rapid clinician access in emergency rooms?",
            "a": "We implement fast badge-tap proximity authentication with biometric fallback and smart session handover, combined with auditable 'break-glass' emergency access that grants immediate clinician access while triggering real-time compliance alerting."
        },
        "sources": [
            {"title": "HHS Health Information Privacy & Security Guidelines", "url": "https://www.hhs.gov/hipaa/", "sourceType": "government", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

OIL_GAS_TOPICS = [
    {
        "id": "upstream-downstream-erp",
        "slug": "upstream-downstream-erp",
        "nav_label": "Upstream & Downstream ERP",
        "badge": "OIL & GAS • ENERGY ENTERPRISE SYSTEMS",
        "title": "Upstream & Downstream ERP Architecture & Financial Consolidation",
        "summary": "Integrated enterprise systems supporting exploration, production, pipeline transmission, refining, and retail distribution with continuous uptime and asset tracking.",
        "lead": "Integrated enterprise systems supporting exploration, production, pipeline transmission, refining, and retail distribution with continuous uptime and asset tracking.",
        "image": {
            "url": "/static/images/content/Oil-and-Gas.jpg",
            "alt": "Oil and Gas Enterprise ERP",
            "caption": "Upstream Exploration and Downstream Distribution Systems"
        },
        "content": [
            {
                "heading": "Critical Energy Value Chain",
                "body": "Exploration and production (E&P) of oil and gas is critical for global energy security and economic growth. Energy companies operate in capital-intensive, geographically dispersed, and volatile market environments requiring real-time visibility into production volumes, asset integrity, and supply logistics.\n\nOver the years, the E&P sector has required massive capital investment and flawless operational execution. Sumeru's Oil & Gas practice delivers tailored ERP architectures that bridge upstream field extraction telemetry with downstream refinery accounting and supply chain distribution."
            },
            {
                "heading": "High Availability & Flawless Commissioning",
                "body": "Energy assets operate 24x7x365 in remote environments. We engineer fault-tolerant systems with 100% uptime, ensuring continuous production metering, joint-venture accounting, and regulatory compliance."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Asset & Telemetry Mapping", "desc": "Cataloging field extraction meters, pipeline SCADA interfaces, and refinery ERP nodes."},
            {"step": "PHASE 02", "name": "Joint Venture Accounting", "desc": "Configuring multi-partner production sharing contracts (PSCs) and automated royalty calculations."},
            {"step": "PHASE 03", "name": "High-Availability Integration", "desc": "Deploying redundant database clusters and satellite uplink caching for remote offshore rigs."},
            {"step": "PHASE 04", "name": "Field Deployment & SLA Run", "desc": "Delivering continuous monitoring and maintenance to ensure zero transactional downtime."}
        ],
        "technologies": ["SAP Oil & Gas (IS-Oil)", "SCADA / OPC-UA Telemetry", "Oracle Financials", "Real-Time Production Metering", "Joint Venture Accounting (JVA)"],
        "deliverables": [
            "Oil & Gas Integrated ERP Architecture",
            "SCADA-to-ERP Production Telemetry Interface",
            "Joint Venture Accounting & Revenue Distribution Engine",
            "Offshore High-Availability Disaster Recovery Blueprint"
        ],
        "qa": {
            "q": "How do your solutions handle network connectivity dropouts on remote offshore drilling platforms?",
            "a": "We deploy edge edge-computing nodes that ingest SCADA production telemetry locally during satellite outages. Once satellite connectivity restores, the edge nodes synchronize back to the central ERP ledger using write-ahead transactional queues."
        },
        "sources": [
            {"title": "Sumeru Oil & Gas Solutions", "url": "https://sumerutechnologies.com/industries/oil-gas", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    },
    {
        "id": "asset-lifecycle-management",
        "slug": "asset-lifecycle-management",
        "nav_label": "Asset Lifecycle & Maintenance",
        "badge": "OIL & GAS • ASSET INTEGRITY",
        "title": "Capital Asset Lifecycle Management & Predictive Maintenance Systems",
        "summary": "Maximizing capital asset utilization, preventing pipeline failure, and automating maintenance work orders across high-pressure energy infrastructures.",
        "lead": "Maximizing capital asset utilization, preventing pipeline failure, and automating maintenance work orders across high-pressure energy infrastructures.",
        "image": {
            "url": "/static/images/content/sumeru_enterprise_hero_bg.jpg",
            "alt": "Energy Asset Management",
            "caption": "Predictive Asset Lifecycle & Field Equipment Integrity"
        },
        "content": [
            {
                "heading": "Capital Asset Integrity",
                "body": "In deepwater exploration, refining, and pipeline networks, asset downtime costs millions of dollars per hour, while equipment failure risks catastrophic environmental damage. Maintaining asset integrity requires moving from reactive repairs to sensor-driven predictive maintenance.\n\nSumeru implements Enterprise Asset Management (EAM) solutions that track thousands of pumps, turbines, valves, and pipelines. By integrating vibration, temperature, and pressure sensor feeds into central maintenance schedules, our systems automatically dispatch preventive work orders before component breakdown occurs."
            },
            {
                "heading": "EHS Compliance & Turnaround Management",
                "body": "Our solutions streamline plant shutdown and turnaround scheduling, ensuring maintenance workers adhere strictly to Environmental Health & Safety (EHS) permits and regulatory inspections."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Asset Hierarchy Cataloging", "desc": "Building comprehensive ISO 14224 equipment taxonomies across drilling and refinery facilities."},
            {"step": "PHASE 02", "name": "Sensor & IoT Integration", "desc": "Connecting vibration, heat, and pressure sensor streams into maintenance alerting engines."},
            {"step": "PHASE 03", "name": "Automated Work Order Dispatch", "desc": "Automating preventive maintenance schedules and spare parts reservation in ERP inventory."},
            {"step": "PHASE 04", "name": "Turnaround Optimization", "desc": "Blueprinting plant maintenance shutdowns to minimize outage duration and ensure safety compliance."}
        ],
        "technologies": ["SAP Plant Maintenance (PM)", "IBM Maximo", "ISO 14224 Standards", "Industrial IoT Telemetry", "Predictive Analytics"],
        "deliverables": [
            "Enterprise Asset Hierarchy & Maintenance Taxonomy",
            "Condition-Based Work Order Dispatch Configuration",
            "Plant Turnaround Management Schedule",
            "EHS Environmental Compliance Audit Runbook"
        ],
        "qa": {
            "q": "What cost savings can energy companies achieve with predictive asset maintenance?",
            "a": "Clients typically realize a 20% to 35% reduction in unscheduled asset downtime and a 15% reduction in overall maintenance expenditures through optimized spare parts inventory and timely component refurbishment."
        },
        "sources": [
            {"title": "ISO 14224 Petroleum & Natural Gas Asset Standards", "url": "https://www.iso.org/standard/64076.html", "sourceType": "standard", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

MANUFACTURING_TOPICS = [
    {
        "id": "mes-erp-integration",
        "slug": "mes-erp-integration",
        "nav_label": "Shop Floor & MES Integration",
        "badge": "MANUFACTURING • ISA-95 & SHOP FLOOR",
        "title": "Shop Floor & Manufacturing Execution Systems (MES) Integration (ISA-95)",
        "summary": "Bridging shop-floor PLC/SCADA execution systems with enterprise ERP to achieve millisecond production traceability, scrap reduction, and real-time OEE tracking.",
        "lead": "Bridging shop-floor PLC/SCADA execution systems with enterprise ERP to achieve millisecond production traceability, scrap reduction, and real-time OEE tracking.",
        "image": {
            "url": "/static/images/content/Manufacturing.jpg",
            "alt": "Manufacturing Execution Systems Integration",
            "caption": "Shop Floor MES and ERP Collaboration Architecture"
        },
        "content": [
            {
                "heading": "Connecting Shop Floor to Top Floor",
                "body": "Enterprise-wide collaboration capabilities are the cornerstones of modern manufacturing companies across the Automobile, Aerospace, High-Tech, and Industrial domains. The global manufacturing scenario is rapidly changing, with company operations spanning continents. The need for an efficient supply-chain network is driving companies to adopt sophisticated manufacturing IT solutions.\n\nSumeru provides comprehensive manufacturing enterprise solutions directed towards creating a collaborative network that enhances profitability and delivers customer value. We bridge the critical gap between shop floor PLCs, SCADA units, and central ERP systems using ISA-95 standards, eliminating the latency between physical production and financial reporting."
            },
            {
                "heading": "Tailored for ETO & MTO Operations",
                "body": "In addition to our end-to-end services portfolio, Sumeru's Manufacturing solutions practice has deep experience in creating customized solutions for Engineer-To-Order (ETO) and Manufacture-To-Order (MTO) companies, focusing on enhancing the reach and depth of information while reducing its latency."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "ISA-95 Level 2/3 Mapping", "desc": "Auditing shop-floor PLC controllers, robotic cells, and MES scheduling boundaries."},
            {"step": "PHASE 02", "name": "Real-Time Transaction Bridge", "desc": "Engineering asynchronous event interfaces between MES production receipts and ERP inventory ledgers."},
            {"step": "PHASE 03", "name": "OEE & Scrap Telemetry", "desc": "Configuring live Overall Equipment Effectiveness (OEE) dashboards for shop floor supervisors."},
            {"step": "PHASE 04", "name": "Quality Traceability Validation", "desc": "Enforcing component-level serial tracking to support instant regulatory recall traceability."}
        ],
        "technologies": ["ISA-95 Framework", "SAP Digital Manufacturing (DMC)", "Siemens Opcenter", "OPC-UA / MQTT", "Real-Time OEE Analytics"],
        "deliverables": [
            "ISA-95 MES-to-ERP Integration Architecture",
            "Real-Time Shop Floor OEE Telemetry Dashboard",
            "Component Serialization & Traceability Blueprint",
            "ETO / MTO Custom Production Scheduling Engine"
        ],
        "qa": {
            "q": "How does Sumeru address the latency between shop floor part completion and ERP stock updates?",
            "a": "We deploy edge event streaming (MQTT/Kafka) that captures barcode scans and PLC triggers at the assembly station, posting material backflush transactions to the ERP in sub-second intervals to keep inventory 100% accurate."
        },
        "sources": [
            {"title": "Sumeru Manufacturing Enterprise Solutions", "url": "https://sumerutechnologies.com/industries/manufacturing", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

EDUCATION_TOPICS = [
    {
        "id": "sap-learning-solutions",
        "slug": "sap-learning-solutions",
        "nav_label": "Education as a Service in SAP",
        "badge": "EDUCATION • SAP LMS & ELEARNING",
        "title": "Education as a Service in SAP & Enterprise Learning Management (LMS)",
        "summary": "Advancing educational technology through comprehensive SAP offerings: LMS integration, SCORM/AICC compliance, content development, and educational assessment reports.",
        "lead": "Advancing educational technology through comprehensive SAP offerings: LMS integration, SCORM/AICC compliance, content development, and educational assessment reports.",
        "image": {
            "url": "/static/images/content/Education.jpg",
            "alt": "Education as a Service in SAP",
            "caption": "Education as a Service in SAP & Adaptive Learning Infrastructure"
        },
        "content": [
            {
                "heading": "Advancing Educational Technology in SAP",
                "body": "The constant evolution of knowledge necessitates frequent, accessible, and reliable web-enabled learning systems. Sumeru is committed to advancing educational technology through our comprehensive SAP offerings. Our solutions in this space include:\n- Learning Solutions: Specializing in Learning Management Solutions (LMS) and LMS integration with enterprise applications and content management solutions.\n- Industry Standards: Strict adherence to recognized industry standards such as SCORM, SIF, AICC, and LTI.\n- Educational Publishing: Providing solutions around integrated publishing, custom publishing, and rights management.\n- Assessment Solutions: Developing educational assessment reports and solutions through our Center of Excellence.\n- Content Development: Expert in courseware planning and creation on industry-standard platforms.\n- Content Management: Offering eLearning portals, adaptive learning environments, and content delivery platforms."
            },
            {
                "heading": "The Adaptive Learning Environment",
                "body": "Our proprietary 'Adaptive Learning Environment' is a key solution designed to provide score-based content to increase course efficiency, scale assessments to improve student quality, and offer predictive content to enhance teacher efficiency."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Pedagogical & LMS Discovery", "desc": "Analyzing academic curricula, assessment grading models, and campus SIS integration needs."},
            {"step": "PHASE 02", "name": "Standards-Compliant Architecture", "desc": "Configuring SCORM/AICC compliant course packaging and automated grade synchronization."},
            {"step": "PHASE 03", "name": "Adaptive Engine Implementation", "desc": "Deploying predictive score-based algorithms that dynamically serve content matched to student pace."},
            {"step": "PHASE 04", "name": "Campus ERP Integration", "desc": "Connecting tuition billing, student lifecycle records, and campus portal authentication."}
        ],
        "technologies": ["SAP SuccessFactors Learning", "SCORM 1.2 / 2004", "AICC & SIF Standards", "LTI 1.3 Interoperability", "Adaptive Learning Algorithms"],
        "deliverables": [
            "Education as a Service in SAP Blueprint",
            "SCORM / AICC Compliance & Certification Report",
            "Adaptive Learning Content Engine Specification",
            "Student Lifecycle & SIS Integration Architecture"
        ],
        "qa": {
            "q": "How does Sumeru's Adaptive Learning Environment improve teaching efficiency?",
            "a": "It automatically scores formative assessments, analyzes learner weaknesses in real time, and recommends targeted remediation modules, freeing instructors from manual grading to focus on personalized coaching."
        },
        "sources": [
            {"title": "Sumeru Education Practice Overview", "url": "https://sumerutechnologies.com/industries/education", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

TEXTILE_TOPICS = [
    {
        "id": "fiber-to-fashion",
        "slug": "fiber-to-fashion",
        "nav_label": "From Fiber to Fashion",
        "badge": "TEXTILE & APPAREL • PRECONFIGURED SAP",
        "title": "Integrated Pre-Configured SAP Solution: From Fiber to Fashion",
        "summary": "A ready-to-use preconfigured SAP solution developed specifically for the Textile and Apparel industry, covering spinning, weaving, garmenting, lot tracking, and fashion retail.",
        "lead": "A ready-to-use preconfigured SAP solution developed specifically for the Textile and Apparel industry, covering spinning, weaving, garmenting, lot tracking, and fashion retail.",
        "image": {
            "url": "/static/images/content/Textile-and-Apparel.jpg",
            "alt": "Textile and Apparel SAP Solution",
            "caption": "From Fiber to Fashion — Pre-Configured SAP Vertical Solution"
        },
        "content": [
            {
                "heading": "Comprehensive Pre-Configured Vertical Solution",
                "body": "Sumeru Technologies delivers an integrated Pre-Configured SAP Solution for the entire Textile & Apparel industry: From Fiber to Fashion. Developed to address the typical business scenarios prevailing in global textile production, our solution covers all processes from Fiber to Fabric and Fabric to Garments.\n\nThe foremost benefit gained by our clients lies in the ready-to-use complete set of functions starting from yarn spinning and weave planning to cutting order distribution and retail fulfillment, covering about 85% of day-to-day business tasks straight out of the box."
            },
            {
                "heading": "Addressing Complex Industry Complexities",
                "body": "Textile manufacturing involves intricate lot and shade variations, dimensional matrix tracking (size, color, inseam, cup), shrinkage calculations, and complex multi-currency export quota documentation. Our solution pre-configures these rules, eliminating years of custom ERP programming."
            }
        ],
        "methodology": [
            {"step": "PHASE 01", "name": "Value Chain Sizing", "desc": "Mapping ginning, spinning, weaving, wet processing, and garment cutting workflows."},
            {"step": "PHASE 02", "name": "Apparel Matrix Configuration", "desc": "Configuring multi-dimensional size/color/fit inventory matrices and bill of materials (BOM)."},
            {"step": "PHASE 03", "name": "Lot & Shade Traceability", "desc": "Setting up batch-level dye-lot tracking to eliminate shade variation in finished garments."},
            {"step": "PHASE 04", "name": "Global Trade & Export Cutover", "desc": "Enabling automated duty drawback, multi-currency export packing lists, and EDI customs forms."}
        ],
        "technologies": ["SAP S/4HANA for Fashion & Vertical Business", "SAP AFS Pre-Configurations", "Apparel Matrix Engine", "Dye-Lot Tracking", "Export Compliance EDI"],
        "deliverables": [
            "From Fiber to Fashion Pre-Configured SAP Blueprint",
            "Apparel Matrix Inventory Management Configuration",
            "Dye-Lot & Shade Batch Quality Traceability Spec",
            "Multi-Currency Export Documentation Package"
        ],
        "qa": {
            "q": "How does Sumeru's preconfigured solution handle shrinkage and dye-lot variations?",
            "a": "Our preconfigured formulas automatically calculate fabric shrinkage allowances during marker making and cutting order release, while dye-lot batch tracking ensures fabric rolls from identical dye baths are paired together, preventing garment shade mismatches."
        },
        "sources": [
            {"title": "Sumeru Textile & Apparel Solutions", "url": "https://sumerutechnologies.com/industries/textile-apparel", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

print("enrich_industries.py defined.")
