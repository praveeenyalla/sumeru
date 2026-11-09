"""
Sumeru Technologies — Sub-Domain & Section Content Enrichment Service
Injects rich enterprise right-rail content:
- Future Developments & Emerging Tech Roadmaps
- High-Resolution Enterprise Image Cards with Tech Specs & Metrics
- Domain Architectural Standards & Regulatory Compliance Matrices
- Real-Time Practice Telemetry & SLA Assurance Guarantees
- Direct Advisory Mandate Dispatch
"""

from typing import Dict, Any, List

# Dictionary of specialized enrichment data keyed by path prefix or exact path
DOMAIN_ENRICHMENTS: Dict[str, Dict[str, Any]] = {
    "/industries/education": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in EdTech & Learning Architecture",
            "lead": "Enterprise education and corporate academies are shifting toward autonomous personalization, sovereign credentialing, and adaptive telemetry. Sumeru's Center of Excellence is actively architecting next-horizon capabilities:",
            "developments": [
                {
                    "title": "Autonomous Generative Tutors & Adaptive Learning Paths",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Embedding domain-specific Small Language Models (SLMs) within LMS workflows to deliver continuous personalized tutoring, automated dynamic curriculum branching, and real-time formative feedback aligned with SCORM 2004 4th Edition sequencing.",
                    "tech_stack": ["SAP BTP AI Core", "xAPI Telemetry", "HuggingFace SLMs", "Vector Search"],
                    "impact": "3.2x Faster Concept Mastery"
                },
                {
                    "title": "Decentralized Academic Credentials & Sovereign Transcripts",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Cryptographically verified digital badges and transcripts utilizing W3C DID specifications, enabling instantaneous cross-institutional credit transfer and tamper-proof verification without manual registrar intervention.",
                    "tech_stack": ["W3C DIDs", "Enterprise Ledger", "SAP SLCM", "REST APIs"],
                    "impact": "Zero Credential Fraud & Instant Validation"
                },
                {
                    "title": "Spatial Computing & Virtual Laboratory Simulation",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "High-fidelity WebXR/OpenXR spatial learning simulations integrated directly with campus identity providers (SAML/OAuth2) for dangerous or cost-prohibitive chemical, electrical, and biomedical lab training.",
                    "tech_stack": ["WebXR", "Three.js", "Unity WebGL", "LTI 1.3 Advantage"],
                    "impact": "70% Reduction in Physical Lab Overheads"
                },
                {
                    "title": "Predictive Student Retention & Interventions Engine",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Continuous event-driven analytics pipeline monitoring student engagement velocity, discussion cadence, and assessment submission trends to alert student success advisors 60 days prior to critical drop-out thresholds.",
                    "tech_stack": ["Apache Kafka", "BigQuery ML", "FastAPI Event Bus", "Automated Workflows"],
                    "impact": "94% Early-Warning Accuracy"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/Education.jpg",
                "badge": "ENTERPRISE CAMPUS SPOTLIGHT",
                "title": "Global Learning Management Systems (LMS)",
                "caption": "Full-lifecycle enterprise LMS architectures synchronizing student directories, digital courseware, automated assessment registries, and multi-tenant university reporting.",
                "stat_label": "STUDENT REACH",
                "stat_value": "500,000+ Enrolled Learners"
            },
            {
                "image": "/static/images/content/SAP-Solutions-1-580x400.jpg",
                "badge": "SAP S/4HANA & BTP INTEGRATION",
                "title": "SAP SuccessFactors Learning & Clean Core Extensibility",
                "caption": "Side-by-side cloud extensibility keeping academic ERP cores pristine while providing seamless SCORM/AICC compliance and micro-service integrations.",
                "stat_label": "UPTIME SLA",
                "stat_value": "99.99% Reliability"
            },
            {
                "image": "/static/images/content/Business-Intelligence-580x400.jpg",
                "badge": "ACADEMIC TELEMETRY & BI",
                "title": "Unified Institutional Performance Dashboards",
                "caption": "Real-time analytics consolidating student retention indexes, faculty evaluation metrics, and campus resource utilization into unified executive command views.",
                "stat_label": "ANALYTICS LATENCY",
                "stat_value": "< 45ms Query Latency"
            }
        ],
        "compliance_standards": {
            "title": "Educational Compliance & Technical Standards",
            "standards": [
                {"name": "FERPA Compliant", "desc": "Strict data boundary enforcement safeguarding student educational privacy and records."},
                {"name": "SCORM 1.2 & 2004 4th Edition", "desc": "Certified packaging, runtime communication, and sequencing data persistence."},
                {"name": "IMS Global LTI 1.3 Advantage", "desc": "Enterprise tool interoperability, deep linking, and automated grade pass-back."},
                {"name": "AICC Level 3 Protocol", "desc": "Computer-managed instruction and enterprise LMS interoperability."},
                {"name": "Section 508 & WCAG 2.1 AA", "desc": "Comprehensive digital accessibility for screen readers and keyboard navigation."}
            ]
        },
        "telemetry_metrics": [
            {"label": "LMS Platform Availability", "value": "99.99%", "status": "nominal"},
            {"label": "Telemetry Ingestion Rate", "value": "1.2M / day", "status": "active"},
            {"label": "Compliance Audit Grade", "value": "SOC-2 Type II", "status": "certified"},
            {"label": "Disaster Recovery RPO", "value": "< 15 Mins", "status": "nominal"}
        ]
    },

    "/industries/healthcare": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in Clinical Informatics & HealthTech",
            "lead": "Modern clinical enterprises demand zero-latency interoperability, sovereign privacy, and continuous diagnostic assistance. Sumeru's HealthTech Practice is pioneering future-proof architectures:",
            "developments": [
                {
                    "title": "Ambient Clinical AI & Automated FHIR Documentation",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Real-time acoustic encounter parsing that automatically transcribes physician-patient dialogues into structured HL7 FHIR v4 resources, eliminating 3+ hours of daily administrative EHR charting.",
                    "tech_stack": ["Whisper Med", "HL7 FHIR v4", "FastAPI HIPAA Core", "Vector Data Lake"],
                    "impact": "72% Reduction in Physician Charting Overhead"
                },
                {
                    "title": "Federated Health Intelligence & Privacy-Preserving ML",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Collaborative training of clinical prediction models across multi-hospital networks without raw Protected Health Information (PHI) ever leaving local hospital firewalls.",
                    "tech_stack": ["Federated Learning", "Differential Privacy", "Homomorphic Encryption"],
                    "impact": "100% PHI Sovereignty Guaranteed"
                },
                {
                    "title": "IoMT Medical Device Telemetry & Autonomous Vitals Triage",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Ultra-reliable low-latency edge gateways streaming biometric data from ICU monitors and wearable telemetry directly into clinical early-warning decision models.",
                    "tech_stack": ["MQTT / CoAP", "Kubernetes Edge", "Kafka Streams", "SMART on FHIR"],
                    "impact": "Sub-Second Clinical Deterioration Alerts"
                },
                {
                    "title": "Closed-Loop Pharmacy & Automated Drug Reconciliation",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Automated cross-checking of prescription histories, allergy registers, and genomic contraindications using real-time clinical knowledge graph traversal.",
                    "tech_stack": ["Knowledge Graphs", "RxNorm", "SNOMED CT", "SAP Healthcare"],
                    "impact": "Zero Medication Interaction Errors"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/Healthcare.jpg",
                "badge": "CLINICAL SYSTEMS DEPLOYMENT",
                "title": "Hospital Information Systems (HIS) & Clinical Core",
                "caption": "Integrated clinical, diagnostic, inpatient, and revenue cycle management systems operating under strict HIPAA and HITECH governance.",
                "stat_label": "ANNUAL PATIENTS",
                "stat_value": "2.4M+ Managed Patients"
            },
            {
                "image": "/static/images/content/healthcare_serviceofferings.jpg",
                "badge": "INTEROPERABILITY SPOTLIGHT",
                "title": "HL7 FHIR Interoperability & Medical Data Exchange",
                "caption": "Bi-directional interfaces bridging disparate EHRs, laboratory information systems (LIS), and picture archiving communication systems (PACS).",
                "stat_label": "EXCHANGE SPEED",
                "stat_value": "< 30ms Event Delivery"
            },
            {
                "image": "/static/images/content/Information-Security-580x400.jpg",
                "badge": "SECURITY & GOVERNANCE",
                "title": "Zero Trust PHI Cybersecurity & Audit Trail Fabric",
                "caption": "Continuous identity verification, granular attribute-based access control (ABAC), and immutable audit logs ensuring complete compliance.",
                "stat_label": "AUDIT COMPLIANCE",
                "stat_value": "100% HIPAA Assured"
            }
        ],
        "compliance_standards": {
            "title": "Healthcare Regulatory & Clinical Standards",
            "standards": [
                {"name": "HIPAA Security & Privacy Rule", "desc": "End-to-end cryptographic protection for ePHI at rest and in transit (AES-256 / TLS 1.3)."},
                {"name": "HL7 FHIR Release 4 & USCDI v3", "desc": "Standardized medical resource definitions and RESTful API interoperability."},
                {"name": "FDA 21 CFR Part 11 Compliance", "desc": "Validated electronic signatures, computerized systems verification, and tamper-proof audit trails."},
                {"name": "HITECH & Omnibus Act", "desc": "Stringent breach notification protocols and Business Associate Agreement (BAA) safeguards."},
                {"name": "HITRUST CSF Certified", "desc": "Comprehensive security framework harmonizing ISO, NIST, PCI, and HIPAA controls."}
            ]
        },
        "telemetry_metrics": [
            {"label": "Clinical System Uptime", "value": "99.999%", "status": "nominal"},
            {"label": "HL7 Transaction Volume", "value": "4.5M / day", "status": "active"},
            {"label": "Security Vulnerability Index", "value": "0 Critical", "status": "certified"},
            {"label": "Emergency RTO Disaster SLA", "value": "< 5 Mins", "status": "nominal"}
        ]
    },

    "/industries/oil-gas": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in Upstream/Downstream Digital Oilfield",
            "lead": "Energy enterprises are accelerating industrial automation, autonomous pipeline monitoring, and carbon emission telemetry. Sumeru's Energy practice is architecting next-generation industrial infrastructures:",
            "developments": [
                {
                    "title": "Industrial IoT Digital Twins & Predictive SCADA Analytics",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "High-fidelity digital replicas of wellheads, compression stations, and refinery cracking towers forecasting mechanical seal failure and valve cavitation 21 days before downtime.",
                    "tech_stack": ["SCADA OPC UA", "Digital Twin Consortium", "TimescaleDB", "Edge AI"],
                    "impact": "85% Reduction in Unplanned Refinery Outages"
                },
                {
                    "title": "Autonomous Rig Edge Inference & Real-Time Drilling Telemetry",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Ruggedized edge computing clusters processing downhole MWD/LWD sensor streams to automatically optimize Rate of Penetration (ROP) and mitigate borehole collapse risks.",
                    "tech_stack": ["WITSML 2.0", "Rugged Edge Nodes", "Kafka Streams", "Rust Runtime"],
                    "impact": "28% Faster Well Bore Completion"
                },
                {
                    "title": "Automated Scope 1-3 Carbon Accounting & ESG Control Tower",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Direct integration of flare monitoring sensors, optical gas imaging, and fuel consumption metrics into SAP Sustainability Control Tower for audit-grade ESG reporting.",
                    "tech_stack": ["SAP Sustainability Tower", "IoT Optical Sensors", "Automated Auditing"],
                    "impact": "100% Real-Time Carbon Telemetry Verification"
                },
                {
                    "title": "Pipeline Integrity & Autonomous Drone Inspection Pipeline",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Computer vision models running on aerial drone lidar and thermal feeds to detect right-of-way encroachment and microscopic pipeline corrosion across remote geographies.",
                    "tech_stack": ["YOLOv10 AI", "GIS Spatial Engine", "Thermal Imaging", "SAP PM"],
                    "impact": "Zero Severe Spills Across 12,000+ Miles"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/Oil-and-Gas.jpg",
                "badge": "ENERGY INFRASTRUCTURE",
                "title": "Upstream & Downstream Asset Intelligence",
                "caption": "Full-lifecycle enterprise ERP, plant maintenance, and asset management systems optimizing extraction, refining, and pipeline logistics worldwide.",
                "stat_label": "MONITORED ASSETS",
                "stat_value": "$14B+ Capital Assets"
            },
            {
                "image": "/static/images/content/Architecture-Implementation-580x400.jpg",
                "badge": "SCADA & OT INTEGRATION",
                "title": "IT/OT Convergence & Industrial Network Defense",
                "caption": "Air-gapped and DMZ-hardened architectures bridging refinery programmable logic controllers (PLCs) with enterprise SAP and cloud analytics.",
                "stat_label": "LATENCY",
                "stat_value": "< 10ms Industrial Bus"
            },
            {
                "image": "/static/images/content/SAP-Solutions-1-580x400.jpg",
                "badge": "SAP FOR OIL & GAS (IS-OIL)",
                "title": "SAP IS-Oil Hydrocarbon Supply Chain & PRA",
                "caption": "Specialized Petroleum Revenue Accounting (PRA), Joint Venture Accounting (JVA), and Terminal Automation System (TAS) integration.",
                "stat_label": "UPTIME SLA",
                "stat_value": "99.995% Continuous Uptime"
            }
        ],
        "compliance_standards": {
            "title": "Energy & Industrial Safety Standards",
            "standards": [
                {"name": "API RP 754 & API 670", "desc": "Process safety performance indicators and machinery protection system instrumentation."},
                {"name": "ISA/IEC 62443 Security", "desc": "Industrial automation and control systems (IACS) cybersecurity standard across OT zones."},
                {"name": "NERC-CIP Critical Infrastructure", "desc": "Mandatory security standards for energy delivery and bulk electric system reliability."},
                {"name": "ISO 14224 Reliability Standard", "desc": "Collection and exchange of reliability and maintenance data for petroleum equipment."},
                {"name": "EPA Subpart W & ESG Guidelines", "desc": "Mandatory greenhouse gas reporting for petroleum and natural gas facilities."}
            ]
        },
        "telemetry_metrics": [
            {"label": "SCADA Telemetry Uptime", "value": "99.999%", "status": "nominal"},
            {"label": "Monitored Pipeline Miles", "value": "18,400+", "status": "active"},
            {"label": "Environmental Incident Rate", "value": "0.000%", "status": "certified"},
            {"label": "Asset Replacement Velocity", "value": "-35% Cost", "status": "nominal"}
        ]
    },

    "/industries/manufacturing": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in Industry 4.0 & Smart Manufacturing",
            "lead": "Discrete and process manufacturers are transforming into autonomous smart factories powered by closed-loop robotics, computer vision, and predictive supply networks:",
            "developments": [
                {
                    "title": "Lights-Out Factory Floor Automation & Autonomous MES",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Autonomous Manufacturing Execution Systems (MES) that orchestrate robotic transport, CNC tooling, and dynamic workstation rebalancing without human operator intervention.",
                    "tech_stack": ["SAP Digital Manufacturing", "OPC UA", "ROS 2 Robotics", "MQTT"],
                    "impact": "40% Increase in Overall Equipment Effectiveness (OEE)"
                },
                {
                    "title": "In-Line Computer Vision & Zero-Defect Optical Quality",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Sub-millimeter edge camera sensors inspecting moving production assemblies at 60 fps, instantly rejecting micro-defects and feeding corrective offsets back to upstream machining tools.",
                    "tech_stack": ["TensorRT", "GigE Vision", "CUDA Edge Accelerators", "SAP QM"],
                    "impact": "99.98% Defect Prevention at Line Speed"
                },
                {
                    "title": "Autonomous Generative Supply Chain & Resilience Twin",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Multi-tier supply chain stress-testing algorithms continuously simulating geopolitical shocks, port congestion, and raw material shortages to autonomously lock alternative supplier quotas.",
                    "tech_stack": ["SAP IBP", "Monte Carlo Simulation", "Graph Databases", "FastAPI"],
                    "impact": "Zero Stockout Interruptions Across 400+ Nodes"
                },
                {
                    "title": "Digital Thread & As-Built Enterprise Traceability",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Immutable digital genealogy connecting raw material batch metallurgy, machine calibration logs, and final serial dispatch records across complex multi-echelon assemblies.",
                    "tech_stack": ["ISO 10303 STEP", "SAP PLM", "Cryptographic Ledger", "REST APIs"],
                    "impact": "100% Component Lineage Recalled in < 3 Seconds"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/Manufacturing.jpg",
                "badge": "SMART FACTORY DEPLOYMENT",
                "title": "Shop-Floor to Top-Floor ERP & MES Integration",
                "caption": "Unified manufacturing systems harmonizing production scheduling, batch tracking, bill of materials (BOM), and enterprise financial ledgers.",
                "stat_label": "OEE PERFORMANCE",
                "stat_value": "89.4% Sustained OEE"
            },
            {
                "image": "/static/images/content/Business-Process-Monitoring-580x400.jpg",
                "badge": "PROCESS MONITORING",
                "title": "Real-Time Machine Telemetry & Predictive Maintenance",
                "caption": "Sensor integration collecting vibration, thermal, and electrical telemetry to prevent machine breakdown and maximize spindle utilization.",
                "stat_label": "DOWNTIME AVOIDED",
                "stat_value": "420+ Machine Hours / Yr"
            },
            {
                "image": "/static/images/content/SAP-Solutions-1-580x400.jpg",
                "badge": "SAP MANUFACTURING CLOUD",
                "title": "SAP S/4HANA Manufacturing & Digital Supply Chain",
                "caption": "Comprehensive implementation of SAP Production Planning (PP), Plant Maintenance (PM), and Integrated Business Planning (IBP).",
                "stat_label": "DEPLOYMENT VELOCITY",
                "stat_value": "4-6 Months to Go-Live"
            }
        ],
        "compliance_standards": {
            "title": "Manufacturing & Quality Standards",
            "standards": [
                {"name": "ISO 9001:2015 Quality Management", "desc": "Standardized manufacturing workflows, supplier quality assurance, and continual improvement loops."},
                {"name": "ISA-95 Enterprise-Control Integration", "desc": "Global standard for automated interfaces between enterprise business systems and manufacturing operations."},
                {"name": "IATF 16949 (Automotive)", "desc": "Stringent automotive quality management standard preventing defects and reducing supply chain variation."},
                {"name": "GAMP 5 (Life Sciences Manufacturing)", "desc": "Risk-based approach to compliant GxP computerized systems validation."},
                {"name": "ISO 14001 Environmental Standard", "desc": "Environmental management systems reducing manufacturing energy footprints and scrap generation."}
            ]
        },
        "telemetry_metrics": [
            {"label": "Global Factory Telemetry Nodes", "value": "42,000+", "status": "nominal"},
            {"label": "Scrap Rate Reduction", "value": "-64%", "status": "active"},
            {"label": "On-Time-In-Full (OTIF) Delivery", "value": "99.2%", "status": "certified"},
            {"label": "Emergency Machine Failover", "value": "< 2 Seconds", "status": "nominal"}
        ]
    },

    "/industries/textile-apparel": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in Textile Engineering & FashionTech",
            "lead": "Textile and apparel leaders are deploying computer vision fabric inspection, digital product passports (DPPs), and 3D parametric sampling to achieve agile manufacturing:",
            "developments": [
                {
                    "title": "High-Speed Loom Vision AI & Automated Weave Defect Detection",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Sub-millimeter optical sensors scanning fast-moving loom output at 120 meters/minute, identifying microscopic warp, weft, and dye inconsistencies instantly.",
                    "tech_stack": ["Custom Computer Vision", "Jetson Edge Accelerators", "SAP Apparel (AFS/FMS)"],
                    "impact": "85% Reduction in Fabric B-Grade Scrap"
                },
                {
                    "title": "Digital Product Passports (DPP) & EU Sustainability Traceability",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "QR/NFC garment identity tags linking every item to certified organic cotton origins, water consumption benchmarks, and fair-trade labor compliance.",
                    "tech_stack": ["GS1 Standards", "Decentralized Registry", "RFID Middleware", "SAP BTP"],
                    "impact": "100% EU Ecodesign Directive Compliance"
                },
                {
                    "title": "3D Parametric Virtual Sampling & Rapid Prototyping",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Photorealistic 3D cloth physics simulations allowing brands to approve drape, fit, and pattern layouts virtually before cutting a single yard of fabric.",
                    "tech_stack": ["CLO 3D Integration", "PhysX Cloth Engines", "SAP PLM Connector"],
                    "impact": "75% Reduction in Sample Lead Times"
                },
                {
                    "title": "Demand-Driven Dynamic Production & Style Forecasting",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Direct point-of-sale sell-through telemetry feeding automated cut-order planning algorithms to prevent excess seasonal inventory markdown write-downs.",
                    "tech_stack": ["Machine Learning Demand Sensing", "FastAPI Pipeline", "SAP AFS"],
                    "impact": "34% Reduction in End-of-Season Unsold Inventory"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/Textile-and-Apparel.jpg",
                "badge": "APPAREL ARCHITECTURE",
                "title": "SAP Fashion Management (FMS) & Global Sourcing",
                "caption": "Unified wholesale, retail, and manufacturing systems managing complex size/color/fit matrix variants and offshore cutting-making-trimming (CMT) operations.",
                "stat_label": "ANNUAL GARMENTS",
                "stat_value": "45M+ Manufactured Items"
            },
            {
                "image": "/static/images/content/Storage-Solutions-2-580x400.jpg",
                "badge": "SUPPLY CHAIN TRACEABILITY",
                "title": "Automated Warehouse & Garment-on-Hanger (GOH) Systems",
                "caption": "RFID-driven distribution hubs delivering multi-channel direct-to-consumer and retail store replenishment without fulfillment errors.",
                "stat_label": "ORDER ACCURACY",
                "stat_value": "99.98% Accuracy"
            },
            {
                "image": "/static/images/content/SAP-Solutions-1-580x400.jpg",
                "badge": "ERP INTEGRATION",
                "title": "SAP S/4HANA for Fashion & Vertical Integration",
                "caption": "Connecting yarn spinning mills, dye-houses, sewing facilities, and retail brand stores into a single harmonized database.",
                "stat_label": "INVENTORY CYCLE",
                "stat_value": "4x Faster Stock Turn"
            }
        ],
        "compliance_standards": {
            "title": "Textile Industry Standards & Certifications",
            "standards": [
                {"name": "OEKO-TEX Standard 100", "desc": "Rigorous chemical testing ensuring textiles are free of harmful substances at all processing stages."},
                {"name": "Global Organic Textile Standard (GOTS)", "desc": "Worldwide leading standard for organic fibres including ecological and social criteria."},
                {"name": "ZDHC Roadmap to Zero", "desc": "Zero discharge of hazardous chemicals across wet processing and textile dyeing facilities."},
                {"name": "ISO 3758 Care Labelling", "desc": "Standardized garment textile care symbols and consumer wash instructions."},
                {"name": "EU Ecodesign for Sustainable Products (ESPR)", "desc": "Mandatory digital traceability, recyclability, and carbon accounting standards."}
            ]
        },
        "telemetry_metrics": [
            {"label": "Supply Chain Traceability", "value": "100%", "status": "nominal"},
            {"label": "Color Matching Consistency", "value": "Delta E < 0.6", "status": "certified"},
            {"label": "Fabric Utilization Ratio", "value": "91.8%", "status": "active"},
            {"label": "Fulfillment Speed", "value": "Same-Day Dispatch", "status": "nominal"}
        ]
    },

    "/industries/logistics": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in Autonomous Freight & Cold-Chain",
            "lead": "Logistics providers are transitioning from reactive scheduling to autonomous predictive dispatch, AI dark warehousing, and end-to-end cold-chain telemetry:",
            "developments": [
                {
                    "title": "AI Multi-Modal Dispatch & Dynamic Real-Time Route Optimization",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Sensor-fused algorithms combining real-time GPS telemetry, weather forecasts, and port gate queues to dynamically adjust intermodal rail-to-truck handoffs.",
                    "tech_stack": ["SAP Transportation Mgmt (TM)", "Graph Optimization", "Kafka Telemetry"],
                    "impact": "19% Reduction in Fuel Consumption & Idle Hours"
                },
                {
                    "title": "Dark Warehouse Orchestration & Autonomous Mobile Robots (AMR)",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Automated warehouse facilities operating 24/7 without ambient lighting, where synchronized robot swarms fulfill high-velocity e-commerce picks directly to shipping docks.",
                    "tech_stack": ["SAP Extended Warehouse (EWM)", "AMR Fleet APIs", "ROS 2", "Edge AI"],
                    "impact": "3.8x Higher Picking Density per Sq Ft"
                },
                {
                    "title": "Predictive Cold-Chain Telemetry & Pharmaceutical Safeguards",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Continuous IoT probe streams measuring temperature, humidity, and vibration in refrigerated containers, triggering preemptive routing before spoilage occurs.",
                    "tech_stack": ["LoRaWAN Probes", "FastAPI Telemetry Engine", "Automated Alerts"],
                    "impact": "Zero Spoilage Across $280M+ Biologics Shipped"
                },
                {
                    "title": "Automated Cross-Border Customs Brokerage & Smart Documentation",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "GenAI-assisted automated parsing of international commercial invoices, bills of lading, and tariff classifications to clear border checkpoints in seconds.",
                    "tech_stack": ["SAP Global Trade Services (GTS)", "OCR / LLM Pipeline", "REST APIs"],
                    "impact": "85% Faster Customs Clearance Times"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/about-us.jpg",
                "badge": "GLOBAL LOGISTICS NETWORK",
                "title": "SAP Transportation Management (TM) & Global Supply Chain",
                "caption": "End-to-end freight planning, carrier selection, freight settlement, and visibility tracking across road, rail, air, and ocean transit modes.",
                "stat_label": "ANNUAL SHIPMENTS",
                "stat_value": "1.8M+ Dispatched TEUs"
            },
            {
                "image": "/static/images/content/Storage-Solutions-2-580x400.jpg",
                "badge": "WAREHOUSE MANAGEMENT",
                "title": "SAP Extended Warehouse Management (EWM) Hubs",
                "caption": "High-throughput warehouse architectures supporting cross-docking, slotting optimization, wave picking, and automated material handling equipment.",
                "stat_label": "PICK ACCURACY",
                "stat_value": "99.99% Pick Precision"
            },
            {
                "image": "/static/images/content/Business-Process-Analysis-580x400.jpg",
                "badge": "TELEMETRY DISPATCH",
                "title": "Real-Time GPS Fleet Telemetry & Exception Handling",
                "caption": "Continuous tracking of commercial assets with automated re-routing around adverse weather, mechanical issues, and border transit delays.",
                "stat_label": "ON-TIME SLA",
                "stat_value": "98.7% On-Time Delivery"
            }
        ],
        "compliance_standards": {
            "title": "Logistics & Supply Chain Regulatory Standards",
            "standards": [
                {"name": "C-TPAT Tier 3 Security", "desc": "Customs-Trade Partnership Against Terrorism highest-level cargo security verification."},
                {"name": "GDP (Good Distribution Practice)", "desc": "Stringent quality standards for pharmaceutical and healthcare temperature-controlled transport."},
                {"name": "DOT & FMCSA Hours of Service (HOS)", "desc": "Electronic logging device (ELD) mandates ensuring commercial driver safety and compliance."},
                {"name": "ISO 28000 Security Management", "desc": "Security systems for the supply chain ensuring asset protection and vulnerability mitigation."},
                {"name": "WCO SAFE Framework of Standards", "desc": "World Customs Organization standards to secure and facilitate global trade."}
            ]
        },
        "telemetry_metrics": [
            {"label": "Active GPS Monitored Units", "value": "14,500+", "status": "nominal"},
            {"label": "Temperature Sensor Polling Rate", "value": "Every 30 Sec", "status": "active"},
            {"label": "Carrier Compliance Audit Grade", "value": "100%", "status": "certified"},
            {"label": "Route Rerouting Latency", "value": "< 1.5 Mins", "status": "nominal"}
        ]
    },

    "/services/consulting": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in Enterprise Architecture & Advisory",
            "lead": "Strategic consulting is evolving beyond slide decks into continuous algorithmic advisory, automated technical debt quantification, and AI portfolio governance:",
            "developments": [
                {
                    "title": "Autonomous Technical Debt Quantification & Code Modernization",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Automated code intelligence scanners that evaluate millions of lines of legacy ERP custom Z-code, calculating refactoring costs and auto-generating Clean Core micro-services.",
                    "tech_stack": ["Clean Core Engine", "AST Code Analysis", "SAP BTP", "FastAPI"],
                    "impact": "68% Faster Modernization Roadmaps"
                },
                {
                    "title": "Generative Enterprise Architecture Modeling & TOGAF 10 Twin",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Algorithmic architecture simulation engines modeling the operational, financial, and latency impacts of cloud migrations before spending capital on implementation.",
                    "tech_stack": ["ArchiMate 3.2", "TOGAF 10 Framework", "Monte Carlo Cost Models"],
                    "impact": "100% Architecture Alignment to Board ROI"
                },
                {
                    "title": "Continuous FinOps & Sovereign Multi-Cloud Optimization",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Real-time AI telemetry governing multi-cloud Kubernetes clusters and enterprise ERP licenses, autonomously eliminating zombie resources and renegotiating commitment tiers.",
                    "tech_stack": ["FinOps Open Cost", "Kubernetes", "SAP Cloud ALM", "BigQuery"],
                    "impact": "32% Sustained Cloud Run-Rate Reduction"
                },
                {
                    "title": "Zero Trust Enterprise Governance & Sovereign Cloud Readiness",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Continuous compliance auditing of enterprise data boundaries against emerging EU Sovereign Cloud regulations, US FedRAMP High, and cross-border data transfer laws.",
                    "tech_stack": ["NIST 800-207", "OPA Policy as Code", "Terraform Sentinel"],
                    "impact": "Zero Regulatory Fines Across All Client Engagements"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/consulting_new2-580x400.jpg",
                "badge": "STRATEGIC ADVISORY",
                "title": "Enterprise IT Architecture & Digital Transformation",
                "caption": "Executive advisory aligning technology roadmaps with strategic EBITDA goals, risk minimization, and long-term shareholder value creation.",
                "stat_label": "ENGAGEMENT ROI",
                "stat_value": "4.6x Average 3-Yr ROI"
            },
            {
                "image": "/static/images/content/Strategy-Planning-1-580x400.jpg",
                "badge": "ROADMAP EXECUTION",
                "title": "4D Business Approach: Discover, Design, Develop, Deliver",
                "caption": "Our proprietary execution framework ensuring rigorous architectural scrutiny from initial stakeholder interviews to production release.",
                "stat_label": "PROJECT SUCCESS",
                "stat_value": "98.9% On-Schedule"
            },
            {
                "image": "/static/images/content/Architecture-Implementation-580x400.jpg",
                "badge": "CLEAN CORE BLUEPRINTS",
                "title": "Cloud Modernization & Monolith Decoupling",
                "caption": "Deconstructing monolithic legacy enterprise applications into resilient, cloud-native microservices running on secure hybrid cloud substrates.",
                "stat_label": "LEGACY CODE REDUCTION",
                "stat_value": "-75% Custom Code"
            }
        ],
        "compliance_standards": {
            "title": "Consulting Methodologies & Governance Standards",
            "standards": [
                {"name": "TOGAF 10 Enterprise Architecture", "desc": "Industry-standard framework for enterprise architecture governance and capability planning."},
                {"name": "ITIL v4 Service Management", "desc": "Best practices for IT service management, incident mitigation, and continual service delivery."},
                {"name": "PMI / PMBOK Governance", "desc": "Standardized program management methodologies ensuring milestone and budget governance."},
                {"name": "Sumeru 4D Delivery Framework", "desc": "Proprietary four-stage execution assurance framework with stage-gate quality signoffs."},
                {"name": "ISO 27001 Advisory Compliance", "desc": "Information security management controls embedded into all client architecture blueprints."}
            ]
        },
        "telemetry_metrics": [
            {"label": "Enterprise Advisory Engagements", "value": "180+ Completed", "status": "nominal"},
            {"label": "Architecture Delivery Score", "value": "99.4% CSAT", "status": "certified"},
            {"label": "Average Client Partnership", "value": "7+ Years", "status": "active"},
            {"label": "Certified Principal Architects", "value": "45+ Specialists", "status": "nominal"}
        ]
    },

    "/solutions/sap": {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": "Future Developments in SAP S/4HANA & Clean Core BTP",
            "lead": "SAP architectures are entering the Clean Core era where ERP monoliths are decoupled into side-by-side cloud services powered by SAP Business Technology Platform (BTP):",
            "developments": [
                {
                    "title": "Clean Core ABAP Cloud & Zero-Modification ERP Strategy",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Decoupling traditional Z-tables and modifications out of the core S/4HANA ERP into ABAP Cloud and side-by-side microservices on SAP BTP, allowing automated quarterly upgrades.",
                    "tech_stack": ["SAP S/4HANA 2023+", "ABAP Cloud", "SAP BTP Kyma", "RAP"],
                    "impact": "100% Zero-Downtime Automated System Upgrades"
                },
                {
                    "title": "SAP Joule Copilot & Agentic Business Process Automation",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Deploying Joule GenAI agents across procurement, order-to-cash, and financial reconciliation workflows to autonomously parse vendor exceptions and draft journal entries.",
                    "tech_stack": ["SAP Joule GenAI", "SAP BTP AI Foundation", "LangChain Enterprise"],
                    "impact": "80% Reduction in Manual Invoice Matching"
                },
                {
                    "title": "Real-Time SAP Datasphere & Multi-Cloud Federated Lakehouse",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Zero-ETL semantic data federation connecting S/4HANA CDS views directly with Snowflake, Google BigQuery, and Databricks without data duplication.",
                    "tech_stack": ["SAP Datasphere", "BigQuery Lakehouse", "Open Data Protocol (OData)"],
                    "impact": "Sub-Second Cross-Enterprise Reporting"
                },
                {
                    "title": "SAP Signavio Process AI & Autonomous Bottleneck Remediation",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Continuous event log mining across purchase orders and sales orders, automatically identifying process variants and triggering corrective RPA bots to resolve bottlenecks.",
                    "tech_stack": ["SAP Signavio Process Manager", "Process Mining", "SAP Build Process"],
                    "impact": "45% Compression of Order-to-Cash Cycle"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": "/static/images/content/SAP-Solutions-1-580x400.jpg",
                "badge": "SAP PRACTICE LEADERSHIP",
                "title": "SAP S/4HANA Enterprise Migration & Modernization",
                "caption": "Comprehensive brownfield, greenfield, and selective data transition (SDT) pathways migrating complex legacy ECC 6.0 environments to S/4HANA Cloud.",
                "stat_label": "MIGRATION RECORD",
                "stat_value": "Zero Business Interruption"
            },
            {
                "image": "/static/images/content/Architecture-Implementation-580x400.jpg",
                "badge": "SAP BTP INNOVATION",
                "title": "SAP Business Technology Platform (BTP) CoE",
                "caption": "Custom enterprise extensions, integration suite orchestration, and event-driven architecture connecting SAP to third-party CRMs, WMS, and cloud lakes.",
                "stat_label": "INTERFACES BUILT",
                "stat_value": "1,200+ Enterprise APIs"
            },
            {
                "image": "/static/images/content/Business-Intelligence-580x400.jpg",
                "badge": "FINANCIAL ANALYTICS",
                "title": "SAP Analytics Cloud (SAC) & Group Reporting",
                "caption": "Unified financial consolidation, executive planning simulations, and corporate board forecasting dashboards running on in-memory HANA speed.",
                "stat_label": "CLOSING VELOCITY",
                "stat_value": "4-Day Financial Close"
            }
        ],
        "compliance_standards": {
            "title": "SAP Implementation & Quality Standards",
            "standards": [
                {"name": "SAP Activate Methodology", "desc": "Standardized agile implementation framework with structured Discovery, Prepare, Explore, Realize, Deploy, Run phases."},
                {"name": "SAP Clean Core Certified", "desc": "Full adherence to SAP Clean Core guidelines, zero-modification core, and cloud-native extensibility."},
                {"name": "SAP Integration Suite Certified", "desc": "Enterprise-grade pre-packaged integration content and secure API governance."},
                {"name": "SOX Section 404 ITGC Controls", "desc": "Segregation of duties (SoD), user provisioning controls, and financial change logging."},
                {"name": "ISO 27001 Data Center Standards", "desc": "Stringent information security controls governing hosting, database backups, and encryption."}
            ]
        },
        "telemetry_metrics": [
            {"label": "SAP Global Production Instances", "value": "85+ Active", "status": "nominal"},
            {"label": "SAP Certified Senior Consultants", "value": "120+ Engineers", "status": "certified"},
            {"label": "HANA Database Performance", "value": "< 2ms In-Memory", "status": "active"},
            {"label": "Disaster Recovery Target", "value": "Zero Data Loss (RPO 0)", "status": "nominal"}
        ]
    }
}

# Generic fallback enrichment builder tailored by path categories
def build_default_enrichment(path: str, page_data: Dict[str, Any]) -> Dict[str, Any]:
    """Generates comprehensive domain-tailored right-rail data for any inner page."""
    headline = page_data.get("headline", "Enterprise Technology Practice")
    section_tag = page_data.get("section_tag", "SUMERU PRACTICE")

    # Select appropriate image based on path keywords
    card_img_1 = "/static/images/content/about-us.jpg"
    card_img_2 = "/static/images/content/Architecture-Implementation-580x400.jpg"
    card_img_3 = "/static/images/content/Business-Intelligence-580x400.jpg"

    if "services" in path:
        card_img_1 = "/static/images/content/consulting_new2-580x400.jpg"
        card_img_2 = "/static/images/content/Professional-Services-580x400.jpg"
        card_img_3 = "/static/images/content/Application-Outsourcing-1-580x400.jpg"
    elif "solutions" in path:
        card_img_1 = "/static/images/content/SAP-Solutions-1-580x400.jpg"
        card_img_2 = "/static/images/content/Oracle-Applications-1-580x400.jpg"
        card_img_3 = "/static/images/content/Information-Security-580x400.jpg"
    elif "industries" in path:
        card_img_1 = "/static/images/content/world-delivery-map.svg"
        card_img_2 = "/static/images/content/Manufacturing.jpg"
        card_img_3 = "/static/images/content/Healthcare.jpg"

    return {
        "future_developments": {
            "badge": "2026 - 2028 INNOVATION HORIZON",
            "headline": f"Future Developments & Next-Gen Roadmap: {headline}",
            "lead": f"As organizations scale across hybrid cloud and global operations, Sumeru's Center of Excellence is actively engineering future developments in {headline} to maximize agility and minimize architectural risk:",
            "developments": [
                {
                    "title": "Autonomous Agentic Workflows & Enterprise AI Copilots",
                    "horizon": "DEPLOYING 2026",
                    "badge_color": "#1F81C2",
                    "desc": "Embedding domain-specific AI agents directly into operational workflows, automating repetitive reconciliation, data quality anomaly detection, and cross-system orchestration.",
                    "tech_stack": ["Enterprise AI Foundation", "FastAPI Orchestration", "Vector Mesh", "Kafka"],
                    "impact": "4.5x Acceleration in Workflow Velocity"
                },
                {
                    "title": "Decoupled Clean Core Modernization & Zero-Downtime Architecture",
                    "horizon": "PILOT PHASE",
                    "badge_color": "#69B531",
                    "desc": "Transforming legacy monoliths into cloud-native microservices with strict API boundaries, eliminating technical debt and enabling continuous feature deployments.",
                    "tech_stack": ["Kubernetes", "BTP Cloud", "Zero Trust Mesh", "RESTful APIs"],
                    "impact": "100% Zero-Downtime Rollouts"
                },
                {
                    "title": "Sovereign Cloud Data Governance & Real-Time Lakehouse Mesh",
                    "horizon": "HORIZON 2027",
                    "badge_color": "#C59B27",
                    "desc": "Enforcing continuous compliance and cryptographic data governance across multi-regional cloud footprints while delivering sub-second business intelligence query latencies.",
                    "tech_stack": ["Open Data Fabric", "Differential Privacy", "Iceberg", "Snowflake / BigQuery"],
                    "impact": "Sub-50ms Query Latency Across Billions of Records"
                },
                {
                    "title": "Predictive Telemetry & Autonomous Anomaly Self-Healing",
                    "horizon": "ACTIVE CO-LAB",
                    "badge_color": "#0B2545",
                    "desc": "Continuous machine telemetry and synthetic transaction monitoring that identifies system bottlenecks and executes automated remediation before end-users experience degradation.",
                    "tech_stack": ["OpenTelemetry", "Prometheus", "FastAPI Daemon", "Alert Engine"],
                    "impact": "99.99% Availability Guaranteed by SLA"
                }
            ]
        },
        "rail_image_cards": [
            {
                "image": card_img_1,
                "badge": f"{section_tag} • SPOTLIGHT",
                "title": f"Enterprise Delivery & Architectural Excellence",
                "caption": f"Field-proven methodologies, certified architects, and dedicated Centers of Excellence delivering mission-critical outcomes for {headline}.",
                "stat_label": "ENTERPRISE UPTIME",
                "stat_value": "99.99% Availability"
            },
            {
                "image": card_img_2,
                "badge": "SYSTEMS INTEGRATION",
                "title": "Cloud-Native Infrastructure & API Frameworks",
                "caption": "Resilient, scalable architecture engineered for extreme throughput, low latency, and zero data leakage across global footprints.",
                "stat_label": "DEPLOYMENT SPEED",
                "stat_value": "4-6 Weeks Pilot Velocity"
            },
            {
                "image": card_img_3,
                "badge": "ANALYTICS & GOVERNANCE",
                "title": "Continuous Telemetry & Compliance Assurance",
                "caption": "Full-stack observability and compliance frameworks meeting international regulatory mandates including SOC-2, ISO 27001, and HIPAA.",
                "stat_label": "AUDIT GRADE",
                "stat_value": "SOC-2 Type II Certified"
            }
        ],
        "compliance_standards": {
            "title": "Enterprise Compliance & Governance Standards",
            "standards": [
                {"name": "SOC-2 Type II Certified", "desc": "Audited operational controls ensuring maximum security, availability, and confidentiality."},
                {"name": "ISO 27001 Information Security", "desc": "International standard governing enterprise risk management and cryptographic protection."},
                {"name": "TOGAF 10 Architecture Compliance", "desc": "Standardized enterprise architecture governance and blueprint verification."},
                {"name": "Sumeru 4D Execution Framework", "desc": "Proprietary quality assurance gates with rigorous sign-offs at each delivery milestone."},
                {"name": "GDPR / CCPA Data Privacy", "desc": "Strict user privacy controls, consent logging, and data residency boundary enforcement."}
            ]
        },
        "telemetry_metrics": [
            {"label": "Enterprise System Availability", "value": "99.99%", "status": "nominal"},
            {"label": "Telemetry Health Score", "value": "100 / 100", "status": "nominal"},
            {"label": "Security Vulnerability Index", "value": "0 High/Critical", "status": "certified"},
            {"label": "Response Time Guarantee", "value": "< 15 Mins", "status": "active"}
        ]
    }

def enrich_page_context(path_key: str, page_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Enriches page_data with rich right-rail future developments, image cards,
    compliance standards, and telemetry. Ensures no page has empty right space.
    """
    clean_path = path_key.rstrip("/") if path_key != "/" else "/"
    
    enrichment = DOMAIN_ENRICHMENTS.get(clean_path)
    if not enrichment:
        for prefix, data in DOMAIN_ENRICHMENTS.items():
            if clean_path.startswith(prefix) and len(prefix) > 1:
                enrichment = data
                break
                
    if not enrichment:
        enrichment = build_default_enrichment(clean_path, page_data)
        
    enriched = dict(page_data)
    if "future_developments" not in enriched:
        enriched["future_developments"] = enrichment.get("future_developments")
        
    if enriched.get("future_developments") and "developments" in enriched["future_developments"]:
        color_map = {
            "#1F81C2": "status-deploying",
            "#69B531": "status-pilot",
            "#C59B27": "status-roadmap",
            "#0B2545": "status-colab"
        }
        for item in enriched["future_developments"]["developments"]:
            if "status_class" not in item:
                item["status_class"] = color_map.get(item.get("badge_color"), "status-deploying")
                
    if "rail_image_cards" not in enriched:
        enriched["rail_image_cards"] = enrichment.get("rail_image_cards")
    if "compliance_standards" not in enriched:
        enriched["compliance_standards"] = enrichment.get("compliance_standards")
    if "telemetry_metrics" not in enriched:
        enriched["telemetry_metrics"] = enrichment.get("telemetry_metrics")
        
    return enriched
