/**
 * Sumeru Technologies LLC - Autonomous Enterprise Architectural Controller
 * Complete client-side database, interactive animation overlays, mandate cart,
 * responsive pages navigation, and zero-backend resilience.
 */

// ========================================================
// 1. CLIENT-SIDE DATABASE ENGINE (SumeruClientDB)
// ========================================================
const SumeruClientDB = {
  storageKey: 'sumeru_enterprise_db_v1',
  tables: {},

  init() {
    const saved = localStorage.getItem(this.storageKey);
    if (saved) {
      try {
        this.tables = JSON.parse(saved);
      } catch (e) {
        console.warn('Resetting corrupt client DB:', e);
        this.seedInitialData();
      }
    } else {
      this.seedInitialData();
    }
  },

  seedInitialData() {
    this.tables = {
      telemetry_nodes: {
        SUMERU_CORE: {
          node_id: 'SUMERU_CORE',
          name: 'CENTRAL SYNAPSE ORCHESTRATOR',
          category: 'COORDINATOR',
          base_latency: 0.4,
          status: 'MASTER CLUSTER OPTIMAL',
          protocol: 'TLS 1.3 / SOV-IPC',
          throughput_ops: 184000,
          memory_pct: 38.4,
          cpu_pct: 24.1,
          description: 'Autonomous control plane coordinating air-gapped sovereign intelligence pipelines and hybrid cloud message buses.'
        },
        AI_CORE: {
          node_id: 'AI_CORE',
          name: 'SOVEREIGN SLM REASONING MESH',
          category: 'INTELLIGENCE',
          base_latency: 3.8,
          status: 'ISOLATED TENANT HEALTHY',
          protocol: 'gRPC v2 / mTLS',
          throughput_ops: 64200,
          memory_pct: 54.2,
          cpu_pct: 41.8,
          description: 'On-premises private 8B/70B Small Language Models performing domain reasoning with zero cloud telemetry egress.'
        },
        SAP_CORE: {
          node_id: 'SAP_CORE',
          name: 'SAP S/4HANA CLEAN CORE KERNEL',
          category: 'ERP_ENGINE',
          base_latency: 1.8,
          status: 'CLEAN CORE EXTENSIONS COMPLIANT',
          protocol: 'OData v4 / Event Mesh',
          throughput_ops: 92100,
          memory_pct: 42.1,
          cpu_pct: 29.5,
          description: 'Tier-1 untouched core ERP foundation integrated with BTP cloud-native side-by-side extension runtime.'
        },
        CLOUD_INFRA: {
          node_id: 'CLOUD_INFRA',
          name: 'HYBRID MULTI-CLOUD FABRIC',
          category: 'INFRASTRUCTURE',
          base_latency: 2.1,
          status: 'MULTI-REGION REPLICATED',
          protocol: 'WireGuard / BGP',
          throughput_ops: 145000,
          memory_pct: 36.8,
          cpu_pct: 22.3,
          description: 'Cross-platform mesh spanning AWS, Azure, and Google Cloud with sub-60s active-active failover.'
        },
        DATA_FABRIC: {
          node_id: 'DATA_FABRIC',
          name: 'MASTER DATA LAKEHOUSE (MDM)',
          category: 'DATA_MANAGEMENT',
          base_latency: 4.2,
          status: 'PARQUET STREAM HARMONIZED',
          protocol: 'Apache Kafka / Iceberg',
          throughput_ops: 118000,
          memory_pct: 48.7,
          cpu_pct: 34.6,
          description: 'Harmonized Kalido MDM and Apache Iceberg storage preserving ACID compliance across global subsidiaries.'
        },
        SECURITY: {
          node_id: 'SECURITY',
          name: 'ZERO-TRUST CRYPTOGRAPHIC DEFENSE',
          category: 'DEFENSIVE_SECURITY',
          base_latency: 0.9,
          status: 'ZERO BREACH ANOMALIES',
          protocol: 'KMS HSM / FIPS 140-3',
          throughput_ops: 210000,
          memory_pct: 31.0,
          cpu_pct: 18.2,
          description: 'Hardware Security Module key management, mutual TLS, and continuous SIEM anomaly telemetry verification.'
        },
        ENGINEERING: {
          node_id: 'ENGINEERING',
          name: 'POLYGLOT CORE ENGINE NODES',
          category: 'RUNTIME_ENGINE',
          base_latency: 1.1,
          status: 'LOW-LATENCY GO/RUST POOL',
          protocol: 'QUIC / REST-v3',
          throughput_ops: 178000,
          memory_pct: 33.5,
          cpu_pct: 19.8,
          description: 'High-throughput microservices and distributed transaction managers handling millions of concurrent events.'
        }
      },
      solutions: {
        'sovereign-ai': {
          id: 'sovereign-ai',
          title: 'Private Enterprise AI & Automation',
          category: 'ai-data',
          category_label: 'SOVEREIGN AI SUITE',
          headline: 'Air-gapped domain reasoning models operating entirely inside your corporate boundary.',
          summary: 'On-premises and private-VPC Small Language Models (SLMs), fine-tuned domain reasoning, and governed multi-agent execution engines.',
          deliverables: [
            'Air-Gapped RAG Pipelines with dense/sparse hybrid search',
            'Deterministic Enterprise Workflows via SAP BTP Event Mesh',
            'Model Risk, Bias, and SOX/HIPAA Compliance Auditing',
            'Domain-specific LoRA parameter-efficient fine-tuning',
            'Private GPU cluster orchestration (NVIDIA Triton & vLLM)'
          ],
          compliance_frameworks: ['ISO 27001', 'SOC 2 Type II', 'HIPAA', 'EU AI Act Sovereign Article 10'],
          architecture_overview: 'Deploying local 8B to 70B parameter models within an isolated VPC or bare-metal GPU clusters. Data never traverses external internet gateways. Ingestion pipelines execute real-time PII scrubbing and format data into knowledge graphs linked to ERP master ledgers.',
          sla_guarantee: '99.99% availability, sub-100ms p95 token generation latency, zero data egress guarantee.'
        },
        'sap-modernization': {
          id: 'sap-modernization',
          title: 'SAP S/4HANA Modernization',
          category: 'sap',
          category_label: 'SAP EXCELLENCE',
          headline: 'Future-proofing core enterprise ERP with pristine Clean Core architecture.',
          summary: 'Clean Core paradigm transitions, RISE with SAP roadmaps, and SAP BTP cloud-native side-by-side extension engineering.',
          deliverables: [
            'Zero-Modification Core Migration with ABAP Cloud decoupling',
            'SAP Cloud ALM Operations & Automated Regression Testing',
            'SAP Joule Generative Copilot Integration across FICO and MM',
            'Brownfield, Greenfield, and Selective Data Transition Playbooks',
            'Automated Technical Debt Remediation and Z-program elimination'
          ],
          compliance_frameworks: ['SAP Clean Core Certified Standard', 'IFRS', 'SOX 404', 'GxP'],
          architecture_overview: 'Eliminating direct table access and user exits in favor of Tier 1 untouched core, Tier 2 released APIs and event mesh, and Tier 4 side-by-side extensions running on SAP Business Technology Platform (BTP). Ensures biannual upgrades complete in days rather than quarters.',
          sla_guarantee: '100% upgradeability guarantee, zero unplanned downtime during brownfield cutover.'
        },
        'hybrid-cloud': {
          id: 'hybrid-cloud',
          title: 'Hybrid Multi-Cloud Engineering',
          category: 'infra-sec',
          category_label: 'CLOUD ARCHITECTURE',
          headline: 'Sovereign cloud fabrics across AWS, Azure, and Google Cloud with automated failover.',
          summary: 'AWS, Azure, and Google Cloud cross-platform meshes engineered for regulatory data sovereignty and resilient failover topologies.',
          deliverables: [
            'Terraform / OpenTofu Infrastructure as Code GitOps pipelines',
            'Multi-Region Active-Active Cloud Nodes with automatic BGP routing',
            'FinOps Cloud Margin Governance saving 30-45% cloud spend',
            'Sovereign data residency boundary containment',
            'Unified Kubernetes (EKS/AKS/GKE) cluster federations'
          ],
          compliance_frameworks: ['FedRAMP High', 'GDPR Data Sovereignty', 'DoD IL5/IL6', 'PCI-DSS 4.0'],
          architecture_overview: 'Zero single points of failure multi-cloud fabric. Mesh networking configured with mutual TLS WireGuard overlays, providing sub-millisecond data replication across geographically dispersed availability zones.',
          sla_guarantee: '99.999% cloud fabric uptime, sub-60-second cross-cloud failover RTO.'
        },
        'data-fabric': {
          id: 'data-fabric',
          title: 'Modern Data Fabric & MDM',
          category: 'ai-data',
          category_label: 'DATA GOVERNANCE',
          headline: 'Single source of enterprise truth with Kalido MDM and Apache Iceberg Lakehouses.',
          summary: 'Unified Master Data Management (Kalido & Informatica), low-latency Apache Iceberg lakes, and real-time Kafka streaming.',
          deliverables: [
            'Kalido MDM & Informatica Master Data Harmonization',
            'Apache Iceberg & Parquet Open Lakehouse Architectures',
            'Automated Lineage, Data Cataloging, and Regulatory Compliance',
            'Sub-second Kafka / Redpanda event streaming pipelines',
            'Reverse-ETL synchronization into SAP HANA and Salesforce'
          ],
          compliance_frameworks: ['BCBS 239', 'GDPR Right to Be Forgotten', 'CCPA', 'HIPAA Data Governance'],
          architecture_overview: 'Decoupling analytical compute from storage. Master data schemas are harmonized in Kalido MDM and streamed in real time to multi-engine query systems (Trino, Snowflake, BigQuery) preserving ACID guarantees.',
          sla_guarantee: '100% transactional consistency, zero duplicate master records across subsidiaries.'
        },
        'enterprise-security': {
          id: 'enterprise-security',
          title: 'Enterprise Security & Defense',
          category: 'infra-sec',
          category_label: 'DEFENSIVE RESILIENCE',
          headline: 'Cryptographic Zero-Trust resilience and hardware-backed key protection.',
          summary: 'Zero-Trust network segmentation, sovereign key management (KMS), and proactive SOC automation for regulated financial and defense nodes.',
          deliverables: [
            'Zero-Trust IAM, Least-Privilege Role & Microsegmentation',
            'Hardware Security Module (HSM) FIPS 140-3 Key Enclaves',
            'Continuous Compliance Telemetry with automated SIEM/SOAR',
            'Post-Quantum Cryptography (PQC) readiness migration',
            'Red Team Adversarial Emulation and Chaos Engineering'
          ],
          compliance_frameworks: ['NIST SP 800-53 Rev 5', 'ISO 27001:2022', 'FIPS 140-3', 'CIS Top 18'],
          architecture_overview: 'Every packet, request, and query must be authenticated and authorized. Microsegmentation isolates core databases from application tiers, with automated cryptographic rotation every 24 hours.',
          sla_guarantee: 'Zero breach history, sub-5-minute mean time to detect (MTTD) on anomalous telemetry.'
        },
        'app-engineering': {
          id: 'app-engineering',
          title: 'Mission-Critical App Engineering',
          category: 'infra-sec',
          category_label: 'ENGINEERING CORE',
          headline: 'Sub-millisecond polyglot transaction processing and sovereign distributed architectures.',
          summary: 'Polyglot microservices, distributed transaction managers, and reactive web applications engineered for millions of concurrent interactions.',
          deliverables: [
            'High-Throughput Go / Rust Microservices and Actor systems',
            'gRPC / Protobuf Internal Fabrics with zero serialization bloat',
            'Formal Invariant Verification for mission-critical trading & billing',
            'Distributed SAGA pattern transaction orchestrators',
            'Autonomous Chaos Engineering test harnesses in CI/CD'
          ],
          compliance_frameworks: ['IEEE 1012', 'ISO 25010', 'BSI IT-Grundschutz', 'OpenSSF Best Practices'],
          architecture_overview: 'Engineered for extreme resiliency and predictability. Systems adhere to formal mathematical verification models, guaranteeing sub-millisecond execution bounds under peak load surges.',
          sla_guarantee: '99.999% transaction success rate, p99 API latency < 8ms.'
        }
      },
      pipeline_stages: {
        1: {
          stage_number: 1,
          code: '01 INGEST',
          name: 'Multi-Modal Ingest & Sanitization Engine',
          short_desc: 'Structured & Raw',
          full_description: 'Continuous automated parsing of structured databases (SAP HANA, SQL), unstructured documents (PDF specs, contracts), and streaming telemetry via TLS 1.3 encrypted conduits with automated PII masking.',
          stats: {
            'INGEST SPEED': '124k docs / sec',
            'PII ACCURACY': '99.98% Sanitized',
            'ISOLATION': 'Dedicated Tenant'
          }
        },
        2: {
          stage_number: 2,
          code: '02 GRAPH',
          name: 'Enterprise Semantic Knowledge Mesh',
          short_desc: 'Semantic Triples',
          full_description: 'Constructs contextual entity graphs linking business ontologies, enterprise master records (Kalido/Informatica), and historical transactions without human annotation lag.',
          stats: {
            'GRAPH ENTITIES': '18M Entities',
            'SEMANTIC MATCH': '99.4% Accuracy',
            'UPDATE FREQUENCY': 'Realtime CDC'
          }
        },
        3: {
          stage_number: 3,
          code: '03 VECTOR',
          name: 'Deterministic Hybrid RAG Layer',
          short_desc: 'Dense / Sparse Search',
          full_description: 'Combines dense vector embeddings with BM25 lexical precision to eradicate AI hallucinations. Every retrieval is strictly cited to verified corporate documents.',
          stats: {
            'RETRIEVAL LATENCY': '38ms p99',
            'PROVENANCE TRACE': '100% Verified',
            'DISTANCE METRIC': 'Cosine Re-ranking'
          }
        },
        4: {
          stage_number: 4,
          code: '04 SLM',
          name: 'Private SLM Reasoning Core',
          short_desc: 'Local Air-Gapped Weights',
          full_description: 'Compact, fine-tuned Small Language Models running entirely on sovereign GPU clusters or inside enterprise VPCs. Unsurpassed domain precision with minimal carbon footprint.',
          stats: {
            'MODEL SIZE': '8B / 70B Quantized',
            'DATA EGRESS': 'Zero External Calls',
            'INFERENCE SPEED': '85 tokens/sec'
          }
        },
        5: {
          stage_number: 5,
          code: '05 AGENTS',
          name: 'Multi-Agent Evaluation Swarm',
          short_desc: 'Multi-Role Evaluators',
          full_description: 'Autonomous agent swarms executing specialized roles: plan generator, compliance validator, financial auditor, and executive synthesizer with mutual consensus checks.',
          stats: {
            'CONSENSUS PROTOCOL': '4-Way Byzantine',
            'HALLUCINATION GATE': 'Zero Tolerance',
            'AUDIT LOG': 'Immutable Trace'
          }
        },
        6: {
          stage_number: 6,
          code: '06 FLOWS',
          name: 'Deterministic Enterprise Workflows',
          short_desc: 'Deterministic BTP',
          full_description: 'Translates validated LLM deductions into transactional operations: automated PO creation, SAP BTP event dispatches, or CRM customer service workflows.',
          stats: {
            'WORKFLOW INTEGRITY': 'ACID Guaranteed',
            'TRANSACTION SPEED': '18ms End-to-End',
            'BTP INTEGRATION': 'Native CAP/Sidecar'
          }
        },
        7: {
          stage_number: 7,
          code: '07 INTERFACE',
          name: 'Enterprise Governance UI & APIs',
          short_desc: 'SAP Fiori & APIs',
          full_description: 'Delivering synthesized intelligence through enterprise glass: SAP Fiori worklists, sovereign portal dashboards, and bi-directional executive API endpoints.',
          stats: {
            'UI PROTOCOL': 'Adaptive Fiori / UI5',
            'CONCURRENCY': '100k Users Active',
            'UPTIME': '99.999% Production'
          }
        }
      },
      industry_case_studies: {
        healthcare: {
          id: 'healthcare',
          name: 'Healthcare & Life Sciences',
          badge: 'FDA / HIPAA COMPLIANT',
          image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDSBYzb5_DUhokqpeWwKN2X5_Zd9kTX1FnS3253V4GIfhUuFL2CXCplckfGZRlOtLItqQ-0oLhGZdC3qN5R4U5tU2XsnZC1m6GG78IIE416-rRFAmssEVCZNPSLJMXDdLaBXDozcC54L0jdv8tLSl-yGuot7fV7rhzA1DhYx-BCxtoLNJsFLbesSx5RnbMDD8vZNYJiWBR2VdR7f-kdbYLVwtt-JIRqcNfjNr3b93UhfDefqPTKd7xYxA',
          challenge: 'Global pharmaceutical and biotech manufacturer faced escalating validation overhead across disparate GxP systems, manual clinical trial reconciliation, and risk of non-compliance with 21 CFR Part 11.',
          solution: 'Sumeru engineered an air-gapped sovereign intelligence mesh with automated serialization tracking, GAMP 5 automated testing pipelines, and encrypted clinical trial telemetry integration with SAP S/4HANA.',
          metrics: [
            { label: 'Audit Readiness', val: '100% GxP Verified' },
            { label: 'Reconciliation Speed', val: '8.4x Faster' },
            { label: 'PHI Breach Risk', val: 'Zero Data Egress' }
          ],
          compliance: ['21 CFR Part 11', 'HIPAA Title II', 'GAMP 5 Certified', 'EU GDPR Health Annex']
        },
        energy: {
          id: 'energy',
          name: 'Energy, Oil & Gas',
          badge: 'MISSION-CRITICAL SCADA',
          image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDMG361Zgf5MxqrOEMUOahSG6f-0K7B-KfPoIigrSseCT7Pfl64DnOTFmav9YiUL2WpbzRjU0zo6A6HdgA0W8p6-cCyhq_hMj-MheXBZOO_bBwmC48r1vM89PUgP_Nq_aK-597dGfd8NwhRcWroRnW-HcNPtkWXR2sPfU6NYRP54MJ5n8hVioah7-B5BMxuxqi0ZCBqJHQT-TsV6KGQIjOUkkU6l6nxDIfXsHiiw7d14W7Rqcq2Dv8iFw',
          challenge: 'Offshore extraction assets and pipeline grids suffered from fragmented sensor telemetry, unpredictable downtime, and delayed work orders between SCADA field controllers and SAP PM.',
          solution: 'Deployed low-latency edge computing nodes streaming real-time IoT vibrations into a private predictive maintenance model, triggering automated work permits and inventory dispatches in SAP S/4HANA.',
          metrics: [
            { label: 'Unplanned Downtime', val: '-44% Reduction' },
            { label: 'Telemetry Throughput', val: '2.4M msgs/sec' },
            { label: 'Annual Savings', val: '$14.2M OPEX' }
          ],
          compliance: ['NERC CIP', 'FERC Regulations', 'API Standard 1164', 'ISO 55001 Asset Mgmt']
        },
        manufacturing: {
          id: 'manufacturing',
          name: 'Precision Manufacturing',
          badge: 'INDUSTRY 4.0 MES',
          image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCw2-Yf68jRwMOmnNyMrof3vXFBLHOLbDfPHCQUCU0AxqvsAiM8j3n3uJW-_vu9DQGuFej94CbEY_TRTxD687Djw9IoA05Fv2MiRsrDLi0yBmGXdQEyCsrE4Wos57rX2Fvoji-OnTDroDeKC4N1C_AiczVJhn4bOOp7Zfwxsac8tvSCsbJDBMRUHY-MgLvm30htgcA2GKghQZQ13498nmBWiAovKdYmRJ07pVJsf44_o4vBXA1yCr0Xew',
          challenge: 'High-precision aerospace equipment manufacturer experienced batch variance and latency between plant floor Manufacturing Execution Systems (MES) and global procurement schedules.',
          solution: 'Architected automated side-by-side BTP adapters linking shop-floor robotics directly to SAP S/4HANA Clean Core, featuring optical micro-defect classification powered by local vision models.',
          metrics: [
            { label: 'Overall Equipment Effectiveness (OEE)', val: '+19.6% Increase' },
            { label: 'Defect Catch Rate', val: '99.94% Automated' },
            { label: 'Scrap Reduction', val: '32% Year-Over-Year' }
          ],
          compliance: ['AS9100D Aerospace', 'ISO 9001:2015', 'NIST SP 800-171 Defense', 'ITAR Boundary']
        },
        education: {
          id: 'education',
          name: 'Higher Education & Research',
          badge: 'FERPA SOVEREIGN',
          image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCtsO6VaPa_vpyYWwA2eshazcErCroLzZx1ANDtL8LACc7k30Vc-mdab_EkdqRAl73jINYRWOo5nu6t0pdKQJIbU-7bY_k_doSDC3IEe0AMTPLdWP0kBtFfjP3k1-38WTaQWCGJ5Q0EgJ4dtMzWQlqj0CH0B8ZUqFCfXu2U0-0fAkxzPPtMWgU2PIvBiIN1U_1vJG1R9P_HjPZ-a83o5COywnl2ZEUCSim-WU7voJTZhqcjjUBNpmewAQ',
          challenge: 'Major collegiate university system maintained 40+ legacy departmental silos, creating crippling friction in student financial services, endowment allocations, and grant research billing.',
          solution: 'Unified campus operations under a sovereign cloud ERP mesh with FERPA-hardened role-based access control, modern Fiori mobile self-service, and automated federal grant accounting.',
          metrics: [
            { label: 'Student Self-Service Adoption', val: '96% Campus Wide' },
            { label: 'Grant Closeout Velocity', val: '60 Days Faster' },
            { label: 'System TCO Reduction', val: '28% Over 5 Yrs' }
          ],
          compliance: ['FERPA 34 CFR Part 99', 'Title IV Compliance', 'GLBA Safeguards', 'NCAA Financial Rules']
        },
        textile: {
          id: 'textile',
          name: 'Textile & Apparel Supply Chains',
          badge: 'GLOBAL SCM & PLM',
          image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDupE-wzD5Ba-oNYbzUhiZco5VAoiPLHPEvLNuwQ6mRKjGqq0fGDFKrpYbKN1wFa7ljzEaH3oFFFlNdcyBAZaxAp62gM34thirGEJveo4PGlO4iXxn16gg3BX9lE8ubDfkU1UCpM4jiJ-YHNDbOGNdkVX9HnQe4HR8pIEAX-sZae0nJDw2p0XO4xbweW2E7e7hmA2i_7IF0FBnPKz925ZslH_TgFHseFLKfyAqP9WK2LSuAvG05Fru8fg',
          challenge: 'Global apparel brand operated multi-continental spinning mills and retail networks with volatile material costs, complex cross-border customs tariffs, and seasonal demand mismatches.',
          solution: 'Implemented an event-driven master data and inventory allocation platform integrated with SAP TM and Kalido MDM, dynamically adjusting shipping corridors and production batches.',
          metrics: [
            { label: 'Tariff Penalty Avoidance', val: '$6.8M Annual' },
            { label: 'Inventory Turnover', val: '+24% Velocity' },
            { label: 'Carbon Traceability', val: 'Tier-3 Provenance' }
          ],
          compliance: ['UFLPA Traceability', 'OEKO-TEX Certified', 'EU Ecodesign Mandate', 'US Customs C-TPAT']
        },
        logistics: {
          id: 'logistics',
          name: 'Logistics & Freight Transport',
          badge: 'EVENT-DRIVEN DISPATCH',
          image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuD_7fsYS6pUkEfPDxEdHsKgxXSLLKGsTN0ZNCNj3KQYMYDKNJcstZkUnEdJprVsoXEDxxg0N3WdVkbbpxr0wiLwZacT_tBWAVZs2bKSbO17qW39bw555Ujcbf2xeUJQYvanNXS1ujIxZCfTlHu_CI-uDfklBBGogntw5o-Dg-EwTCm-Kya5AC8mSxoDgCUTlK_zjli6EoRo3_Gr79RhM0nUyf1TnXce12JfnlwV-nh6DZ5YiH-oQn37NA',
          challenge: 'Multi-modal intermodal freight carrier faced dead-head routing, cold-chain temperature telemetry delays, and manual customs clearance at maritime border checkpoints.',
          solution: 'Engineered sub-second GPS/IoT gateway synchronizers feeding autonomous route optimization models, automatically filing customs EDI documents and updating SAP Transportation Management.',
          metrics: [
            { label: 'Route Fuel Efficiency', val: '+14.2% Miles/Gal' },
            { label: 'Customs Clearance Latency', val: 'Sub-4 Minutes' },
            { label: 'Cold-Chain Compliance', val: '99.99% Spoiled-Free' }
          ],
          compliance: ['DOT FMCSA Hours-of-Service', 'FDA Food Safety FSMA', 'IATA Cargo Standards', 'Customs ACE EDI']
        }
      },
      advisory_requests: [
        {
          ticket_id: 'SUM-ADV-2501-A98B',
          executive_name: 'Eleanor Vance',
          corporate_email: 'vance@enterprise.com',
          organization: 'Global Logistics Corp',
          focus_practice: 'sap',
          mandate_scope: 'Cross-border Clean Core upgrade evaluation and BTP event mesh decoupling.',
          status: 'ASSIGNED_TO_PARTNER',
          assigned_partner: 'Marcus Vance, Senior SAP Principal',
          target_callback_time_utc: 'Today within 2 business hours',
          security_hash: 'SHA256-9a4f78b12e6c4a8901',
          created_at: new Date().toISOString()
        }
      ],
      mandate_cart: [
        {
          id: 'sovereign-ai',
          title: 'Private Enterprise AI & Automation',
          category: 'SOVEREIGN AI SUITE',
          sla: '99.99% Sovereign SLA',
          type: 'solution'
        },
        {
          id: 'sap-modernization',
          title: 'SAP S/4HANA Modernization',
          category: 'SAP EXCELLENCE',
          sla: '100% Clean Core Guarantee',
          type: 'solution'
        }
      ],
      pipeline_simulations: [],
      portal_account: {
        client_name: 'Global Enterprise Client',
        organization: 'Fortune 100 Regulated Institutional Partner',
        active_tenants: 3,
        synapse_nodes_online: 7,
        sla_uptime: '99.994%',
        clean_core_score: '94/100 (A+ Clean Core)',
        recent_deployments: [
          { release: 'v4.8.2-PROD', status: 'LIVE', component: 'Synapse SLM Reasoning Mesh', region: 'US-East (Warrenville VPC)' },
          { release: 'v2.4.1', status: 'LIVE', component: 'SAP BTP Event Decoupler', region: 'Frankfurt EMEA Hub' },
          { release: 'v1.9.0', status: 'STAGING', component: 'Kalido MDM Stream Cache', region: 'India Core Dev' }
        ],
        active_advisories: [
          { id: 'SUM-ADV-2501-A91B', mandate: 'SAP Clean Core 2025 S/4HANA Upgrade Strategy', status: 'IN_PROGRESS', lead: 'Senior Architecture Partner' },
          { id: 'SUM-ADV-2412-C83E', mandate: 'Private RAG Air-Gapped Governance Audit', status: 'COMPLETED_DELIVERED', lead: 'Sovereign Intelligence Fellow' }
        ]
      }
    };
    this.save();
  },

  save() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.tables));
    } catch (e) {
      console.warn('Storage quota warning:', e);
    }
  }
};

// Initialize DB immediately
SumeruClientDB.init();

// ========================================================
// 2. TRANSPARENT CLIENT-SIDE API INTERCEPTOR
// Handles all calls to /api/... with zero-backend failure
// ========================================================
const OriginalFetch = window.fetch;
window.fetch = async function(url, options = {}) {
  const urlStr = String(url);

  // If not an API call, let browser fetch normally
  if (!urlStr.includes('/api/')) {
    return OriginalFetch(url, options);
  }

  // Attempt real network call first if not on file:///
  if (window.location.protocol.startsWith('http')) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 1800);
      const res = await OriginalFetch(url, { ...options, signal: controller.signal });
      clearTimeout(timeoutId);
      if (res.ok) return res;
    } catch (err) {
      // Backend not running, transparently fall back to client database!
    }
  }

  // Mock / Client DB Response Engine
  return new Promise((resolve) => {
    setTimeout(() => {
      // 1. Telemetry endpoints
      if (urlStr.includes('/telemetry/nodes/')) {
        const key = urlStr.split('/telemetry/nodes/')[1].split('?')[0];
        const node = SumeruClientDB.tables.telemetry_nodes[key] || SumeruClientDB.tables.telemetry_nodes.SUMERU_CORE;
        const jitter = (Math.random() * 0.3 - 0.15);
        const dynamicNode = {
          ...node,
          latency_ms: Math.max(0.2, +(node.base_latency + jitter).toFixed(2)),
          throughput_ops: node.throughput_ops + Math.floor(Math.random() * 2000 - 1000)
        };
        resolve(new Response(JSON.stringify(dynamicNode), { status: 200, headers: { 'Content-Type': 'application/json' } }));
        return;
      }

      // 2. Solutions specifications
      if (urlStr.includes('/solutions/')) {
        const id = urlStr.split('/solutions/')[1].split('?')[0];
        const sol = SumeruClientDB.tables.solutions[id] || SumeruClientDB.tables.solutions['sovereign-ai'];
        resolve(new Response(JSON.stringify(sol), { status: 200, headers: { 'Content-Type': 'application/json' } }));
        return;
      }

      // 3. Pipeline stages
      if (urlStr.includes('/pipeline/stages/')) {
        const step = parseInt(urlStr.split('/pipeline/stages/')[1], 10) || 1;
        const stage = SumeruClientDB.tables.pipeline_stages[step] || SumeruClientDB.tables.pipeline_stages[1];
        resolve(new Response(JSON.stringify(stage), { status: 200, headers: { 'Content-Type': 'application/json' } }));
        return;
      }

      // 4. Pipeline simulation execution
      if (urlStr.includes('/pipeline/simulate')) {
        const execId = 'SIM-SOV-' + Math.random().toString(36).substring(2, 8).toUpperCase();
        const simResult = {
          execution_id: execId,
          total_latency_ms: 138,
          final_output_preview: 'Verified air-gapped reasoning trace: PII masked across 12 master records, deterministic vector retrieval confirmed against SAP ledger, unanimous 4/4 Byzantine agent consensus achieved.',
          stages_executed: [
            { stage: 1, name: 'Ingest & Mask', duration_ms: 12, status: 'PASSED', detail: 'Sanitized 14 entity triples via TLS 1.3' },
            { stage: 2, name: 'Knowledge Graph', duration_ms: 22, status: 'MATCHED', detail: 'Mapped to Kalido MDM product catalog' },
            { stage: 3, name: 'Deterministic RAG', duration_ms: 31, status: 'GROUNDED', detail: 'Cosine similarity 0.94 strictly bound to S/4HANA PO ledger' },
            { stage: 4, name: 'SLM Reasoning Core', duration_ms: 45, status: 'OPTIMAL', detail: 'Local FP8 weights executed in on-prem VPC' },
            { stage: 5, name: 'Agent Consensus', duration_ms: 18, status: 'UNANIMOUS', detail: '4/4 validators signed cryptographic invariant' },
            { stage: 6, name: 'Workflow Assembly', duration_ms: 7, status: 'ASSEMBLED', detail: 'Deterministic BTP transaction payload signed' },
            { stage: 7, name: 'Delivery Glass', duration_ms: 3, status: 'DISPATCHED', detail: 'OData v4 streaming telemetry rendered' }
          ],
          provenance_trace: [
            'SHA256: 8a4c1f9b0... (Corpus Document Immutable Seal)',
            'VPC-ENCLAVE: AWS-US-EAST-AIRGAP-TENANT-04',
            'ZERO-EGRESS: NetFilter firewall logged 0 external IP packets'
          ]
        };
        SumeruClientDB.tables.pipeline_simulations.push(simResult);
        SumeruClientDB.save();
        resolve(new Response(JSON.stringify(simResult), { status: 200, headers: { 'Content-Type': 'application/json' } }));
        return;
      }

      // 5. SAP Clean Core audit
      if (urlStr.includes('/sap/audit')) {
        let body = {};
        try { body = JSON.parse(options.body || '{}'); } catch (e) {}
        const zCount = body.custom_z_programs_count || 120;
        const directDb = !!body.direct_db_modifications;
        const btpRate = body.btp_adoption_rate || 'Enterprise';

        let score = 100;
        if (zCount > 500) score -= 35;
        else if (zCount > 200) score -= 22;
        else if (zCount > 50) score -= 12;
        else score -= 4;

        if (directDb) score -= 30;
        if (btpRate === 'Enterprise') score += 15;
        else if (btpRate === 'Pilot') score += 5;
        else score -= 10;

        score = Math.max(28, Math.min(98, score));

        const auditResponse = {
          clean_core_index_pct: score,
          compliance_grade: score >= 80 ? 'A+ Sovereign Compliant' : (score >= 65 ? 'B Tier Decoupling Ready' : 'C Technical Debt Alert'),
          risk_level: score >= 80 ? 'MINIMAL' : (score >= 65 ? 'MODERATE' : 'ELEVATED'),
          estimated_migration_savings: score >= 80 ? '$2.4M across 3-year cycle' : '$1.2M with BTP refactoring',
          recommended_pathway: score >= 80 ? 'S/4HANA 2023 with side-by-side BTP extension suite' : 'Selective Data Transition with custom Z remediation',
          tier_recommendations: [
            { tier: 'Tier 1 (Kernel)', action: 'Decouple direct table queries using released CDS views.' },
            { tier: 'Tier 2 (APIs)', action: 'Switch to SAP Event Mesh for asynchronous ledger triggers.' },
            { tier: 'Tier 4 (BTP)', action: 'Containerize custom business algorithms on Cloud Foundry or Kyma runtime.' }
          ]
        };
        resolve(new Response(JSON.stringify(auditResponse), { status: 200, headers: { 'Content-Type': 'application/json' } }));
        return;
      }

      // 6. Advisory consultation dispatch
      if (urlStr.includes('/advisory/dispatch')) {
        let body = {};
        try { body = JSON.parse(options.body || '{}'); } catch (e) {}
        const ticketId = 'SUM-ADV-' + Math.floor(1000 + Math.random() * 9000) + '-' + Math.random().toString(36).substring(2, 6).toUpperCase();
        const assignedPartner = body.focus_practice === 'sap' ? 'Marcus Vance, Senior SAP Principal' : 'Dr. Aris Thorne, Sovereign AI Fellow';
        const newTicket = {
          ticket_id: ticketId,
          executive_name: body.executive_name || 'Executive Lead',
          corporate_email: body.corporate_email || 'executive@company.com',
          organization: body.organization || 'Enterprise Partner',
          focus_practice: body.focus_practice || 'all',
          mandate_scope: body.mandate_scope || 'Comprehensive enterprise architecture evaluation.',
          status: 'RECORDED_IN_SOVEREIGN_QUEUE',
          assigned_partner: assignedPartner,
          target_callback_time_utc: 'Today within 2 business hours',
          security_hash: 'SHA256-' + Math.random().toString(36).substring(2, 12).toUpperCase(),
          created_at: new Date().toISOString()
        };
        SumeruClientDB.tables.advisory_requests.unshift(newTicket);
        SumeruClientDB.save();
        resolve(new Response(JSON.stringify(newTicket), { status: 200, headers: { 'Content-Type': 'application/json' } }));
        return;
      }

      // 7. Client Portal authenticate
      if (urlStr.includes('/portal/authenticate')) {
        let body = {};
        try { body = JSON.parse(options.body || '{}'); } catch (e) {}
        const email = (body.email || '').toLowerCase();
        const key = (body.access_key || '').toLowerCase();

        if (email.includes('@') && key.length >= 3) {
          resolve(new Response(JSON.stringify(SumeruClientDB.tables.portal_account), { status: 200, headers: { 'Content-Type': 'application/json' } }));
        } else {
          resolve(new Response(JSON.stringify({ detail: 'Invalid credentials' }), { status: 401, headers: { 'Content-Type': 'application/json' } }));
        }
        return;
      }

      // Default fallback
      resolve(new Response(JSON.stringify({ status: 'OK', fallback: true }), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    }, 120);
  });
};

// ========================================================
// 3. NAVIGATION & PAGES DROPDOWN CONTROLLER
// Handles Home button, About Us, Pages dropdown, and mobile menu
// ========================================================
const NavigationController = {
  init() {
    this.bindNavLinks();
    this.bindPagesDropdown();
    this.bindMobileDrawer();
    this.bindKeyboardShortcuts();
  },

  bindNavLinks() {
    // Brand logo click -> smooth scroll home
    const brandLogo = document.querySelector('header a[href="#"], header a[href="/"]');
    if (brandLogo) {
      brandLogo.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // Home link
    document.querySelectorAll('[data-path="home"]').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        this.closeMobileDrawer();
        this.closePagesDropdown();
      });
    });

    // All hash links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href && href.length > 1) {
          const target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            NavigationController.closeMobileDrawer();
            NavigationController.closePagesDropdown();
          }
        }
      });
    });
  },

  bindPagesDropdown() {
    const btn = document.getElementById('pages-dropdown-btn');
    const menu = document.getElementById('pages-dropdown-menu');

    if (btn && menu) {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        menu.classList.toggle('hidden');
      });

      document.addEventListener('click', (e) => {
        if (!menu.contains(e.target) && !btn.contains(e.target)) {
          menu.classList.add('hidden');
        }
      });
    }
  },

  closePagesDropdown() {
    const menu = document.getElementById('pages-dropdown-menu');
    if (menu) menu.classList.add('hidden');
  },

  toggleMobileDrawer() {
    const drawer = document.getElementById('mobile-nav-drawer');
    if (drawer) {
      drawer.classList.toggle('hidden');
      document.body.style.overflow = drawer.classList.contains('hidden') ? '' : 'hidden';
    }
  },

  closeMobileDrawer() {
    const drawer = document.getElementById('mobile-nav-drawer');
    if (drawer && !drawer.classList.contains('hidden')) {
      drawer.classList.add('hidden');
      document.body.style.overflow = '';
    }
  },

  bindKeyboardShortcuts() {
    // ESC key closes any open modal, overlay, drawer, or dropdown
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        AnimationOverlayController.close();
        MandateCartController.close();
        IndustryController.closeModal();
        SolutionsController.closeSpecificationModal();
        CleanCoreController.closeAuditModal();
        PipelineController.closeSimulationModal();
        PortalController.closeModal();
        PillarModalController.close();
        RegionModalController.close();
        NavigationController.closeMobileDrawer();
        NavigationController.closePagesDropdown();
      }
    });
  }
};

// ========================================================
// 4. ANIMATION OVERLAY CONTROLLER
// Interactive, full-scale overlays for any clicked animation
// with clear and simple Cancel option
// ========================================================
const AnimationOverlayController = {
  currentType: null,
  activeNode: 'SUMERU_CORE',
  simSpeed: 1,
  animInterval: null,

  open(type, contextNode = 'SUMERU_CORE') {
    this.currentType = type;
    this.activeNode = contextNode;

    const overlay = document.getElementById('animation-overlay-modal');
    if (!overlay) return;

    const titleEl = document.getElementById('anim-overlay-title');
    const subtitleEl = document.getElementById('anim-overlay-subtitle');
    const contentArea = document.getElementById('anim-overlay-content');

    if (type === 'synapse') {
      if (titleEl) titleEl.textContent = 'Synapse Mesh Matrix • Interactive Topology';
      if (subtitleEl) subtitleEl.textContent = 'Air-Gapped Sovereign Cluster Telemetry & Active Node Inspector';
      this.renderSynapseMesh(contentArea);
    } else if (type === 'global_sync') {
      if (titleEl) titleEl.textContent = 'Follow-the-Sun Global Synchronous Delivery';
      if (subtitleEl) subtitleEl.textContent = 'Warrenville IL • London EMEA • India Core Development Handoff';
      this.renderGlobalSync(contentArea);
    } else if (type === 'pipeline') {
      if (titleEl) titleEl.textContent = '7-Stage Sovereign Reasoning Pipeline Engine';
      if (subtitleEl) subtitleEl.textContent = 'Air-Gapped Deterministic Traversal with Cryptographic Invariant Verification';
      this.renderPipelineTraversal(contentArea);
    } else if (type === 'clean_core') {
      if (titleEl) titleEl.textContent = 'SAP Clean Core 5-Tier Decoupling Architecture';
      if (subtitleEl) subtitleEl.textContent = 'Pristine Kernel Isolation with BTP Side-by-Side Cloud-Native Extensibility';
      this.renderCleanCoreHierarchy(contentArea);
    }

    overlay.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  },

  close() {
    const overlay = document.getElementById('animation-overlay-modal');
    if (overlay) overlay.classList.add('hidden');
    document.body.style.overflow = '';
    if (this.animInterval) {
      clearInterval(this.animInterval);
      this.animInterval = null;
    }
  },

  selectNode(nodeKey) {
    this.activeNode = nodeKey;
    const contentArea = document.getElementById('anim-overlay-content');
    if (this.currentType === 'synapse') {
      this.renderSynapseMesh(contentArea);
    }
  },

  renderSynapseMesh(container) {
    const node = SumeruClientDB.tables.telemetry_nodes[this.activeNode] || SumeruClientDB.tables.telemetry_nodes.SUMERU_CORE;
    const allNodes = SumeruClientDB.tables.telemetry_nodes;

    container.innerHTML = `
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-space-md items-center h-full">
        <!-- Interactive Canvas / SVG Area -->
        <div class="lg:col-span-7 bg-surface-container rounded-2xl p-space-md flex flex-col items-center justify-center relative overflow-hidden aspect-[4/3] shadow-inner">
          <svg class="w-full h-full" viewBox="0 0 600 450" fill="none">
            <defs>
              <radialGradient id="overlayGlow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#c59b27" stop-opacity="0.45"/>
                <stop offset="100%" stop-color="#c59b27" stop-opacity="0"/>
              </radialGradient>
            </defs>
            <circle cx="300" cy="225" r="160" fill="url(#overlayGlow)" class="animate-pulse-glow" />
            <circle cx="300" cy="225" r="180" stroke="#d1c5af" stroke-dasharray="4 6" stroke-opacity="0.4"/>
            <circle cx="300" cy="225" r="120" stroke="#c59b27" stroke-dasharray="2 4" stroke-opacity="0.6"/>

            <!-- Dynamic Lines -->
            <line x1="300" y1="225" x2="130" y2="100" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>
            <line x1="300" y1="225" x2="300" y2="60" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>
            <line x1="300" y1="225" x2="470" y2="100" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>
            <line x1="300" y1="225" x2="470" y2="340" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>
            <line x1="300" y1="225" x2="300" y2="390" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>
            <line x1="300" y1="225" x2="130" y2="340" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>

            <!-- Center Core Hub -->
            <g class="cursor-pointer ${this.activeNode === 'SUMERU_CORE' ? 'active-node-ring' : ''}" onclick="AnimationOverlayController.selectNode('SUMERU_CORE')">
              <circle cx="300" cy="225" r="48" fill="#775a00"/>
              <circle cx="300" cy="225" r="42" fill="#fff8f6" stroke="#c59b27" stroke-width="3"/>
              <text x="300" y="222" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#775a00" text-anchor="middle" letter-spacing="1.5">SUMERU</text>
              <text x="300" y="235" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="600" fill="#8c4f1c" text-anchor="middle">SYNAPSE 4.8</text>
            </g>

            <!-- Peripheral Nodes -->
            <g class="cursor-pointer ${this.activeNode === 'AI_CORE' ? 'active-node-ring' : ''}" onclick="AnimationOverlayController.selectNode('AI_CORE')">
              <circle cx="130" cy="100" r="30" fill="#fff8f6" stroke="#974355" stroke-width="2.5"/>
              <circle cx="130" cy="100" r="22" fill="#ffd9de"/>
              <text x="130" y="97" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="700" fill="#782a3d" text-anchor="middle">AI / SLM</text>
              <text x="130" y="108" font-family="Plus Jakarta Sans" font-size="7" font-weight="600" fill="#974355" text-anchor="middle">REASONING</text>
            </g>

            <g class="cursor-pointer ${this.activeNode === 'SAP_CORE' ? 'active-node-ring' : ''}" onclick="AnimationOverlayController.selectNode('SAP_CORE')">
              <circle cx="300" cy="60" r="30" fill="#fff8f6" stroke="#775a00" stroke-width="2.5"/>
              <circle cx="300" cy="60" r="22" fill="#ffdf98"/>
              <text x="300" y="57" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="700" fill="#473500" text-anchor="middle">SAP CORE</text>
              <text x="300" y="68" font-family="Plus Jakarta Sans" font-size="7" font-weight="600" fill="#775a00" text-anchor="middle">S/4 CLEAN</text>
            </g>

            <g class="cursor-pointer ${this.activeNode === 'CLOUD_INFRA' ? 'active-node-ring' : ''}" onclick="AnimationOverlayController.selectNode('CLOUD_INFRA')">
              <circle cx="470" cy="100" r="30" fill="#fff8f6" stroke="#8c4f1c" stroke-width="2.5"/>
              <circle cx="470" cy="100" r="22" fill="#ffdcc5"/>
              <text x="470" y="97" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="700" fill="#5a2b00" text-anchor="middle">CLOUD</text>
              <text x="470" y="108" font-family="Plus Jakarta Sans" font-size="7" font-weight="600" fill="#8c4f1c" text-anchor="middle">MULTI-MESH</text>
            </g>

            <g class="cursor-pointer ${this.activeNode === 'DATA_FABRIC' ? 'active-node-ring' : ''}" onclick="AnimationOverlayController.selectNode('DATA_FABRIC')">
              <circle cx="470" cy="340" r="30" fill="#fff8f6" stroke="#c59b27" stroke-width="2.5"/>
              <circle cx="470" cy="340" r="22" fill="#ffdf98"/>
              <text x="470" y="337" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="700" fill="#473500" text-anchor="middle">DATA MESH</text>
              <text x="470" y="348" font-family="Plus Jakarta Sans" font-size="7" font-weight="600" fill="#775a00" text-anchor="middle">MDM / LAKE</text>
            </g>

            <g class="cursor-pointer ${this.activeNode === 'SECURITY' ? 'active-node-ring' : ''}" onclick="AnimationOverlayController.selectNode('SECURITY')">
              <circle cx="300" cy="390" r="30" fill="#fff8f6" stroke="#974355" stroke-width="2.5"/>
              <circle cx="300" cy="390" r="22" fill="#ffd9de"/>
              <text x="300" y="387" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="700" fill="#782a3d" text-anchor="middle">SECURITY</text>
              <text x="300" y="398" font-family="Plus Jakarta Sans" font-size="7" font-weight="600" fill="#974355" text-anchor="middle">ZERO TRUST</text>
            </g>

            <g class="cursor-pointer ${this.activeNode === 'ENGINEERING' ? 'active-node-ring' : ''}" onclick="AnimationOverlayController.selectNode('ENGINEERING')">
              <circle cx="130" cy="340" r="30" fill="#fff8f6" stroke="#775a00" stroke-width="2.5"/>
              <circle cx="130" cy="340" r="22" fill="#ffdf98"/>
              <text x="130" y="337" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="700" fill="#473500" text-anchor="middle">CORE ENG</text>
              <text x="130" y="348" font-family="Plus Jakarta Sans" font-size="7" font-weight="600" fill="#775a00" text-anchor="middle">MICROSERVICES</text>
            </g>
          </svg>
          <div class="absolute bottom-3 left-4 text-[11px] text-tertiary font-mono bg-surface/80 px-2 py-0.5 rounded backdrop-blur">
            CLICK ANY NODE IN DIAGRAM TO INSPECT TELEMETRY
          </div>
        </div>

        <!-- Node Telemetry Deep Inspector Right -->
        <div class="lg:col-span-5 flex flex-col gap-space-sm h-full justify-between">
          <div class="flex flex-col gap-space-xs">
            <div class="flex items-center justify-between">
              <span class="px-space-xs py-0.5 rounded bg-primary-container text-on-primary-container font-label-sm text-label-sm font-bold uppercase tracking-wider">
                ${node.category} NODE
              </span>
              <span class="flex items-center gap-1 text-[12px] font-bold text-primary">
                <span class="w-2 h-2 rounded-full bg-primary animate-ping"></span>
                ACTIVE IN-SYNCHRONY
              </span>
            </div>
            <h4 class="font-headline-sm text-headline-sm text-on-surface font-bold">${node.name}</h4>
            <p class="font-body-sm text-body-sm text-on-surface-variant">${node.description}</p>
          </div>

          <!-- Live Metrics Grid -->
          <div class="grid grid-cols-2 gap-space-xs bg-surface-container p-space-sm rounded-xl">
            <div class="flex flex-col">
              <span class="font-label-sm text-label-sm text-on-surface-variant">ROUNDTRIP LATENCY:</span>
              <span class="font-headline-sm text-headline-sm text-primary font-bold">${node.base_latency}ms</span>
            </div>
            <div class="flex flex-col">
              <span class="font-label-sm text-label-sm text-on-surface-variant">THROUGHPUT:</span>
              <span class="font-headline-sm text-headline-sm text-secondary font-bold">${(node.throughput_ops / 1000).toFixed(1)}k ops/s</span>
            </div>
            <div class="flex flex-col pt-1">
              <span class="font-label-sm text-label-sm text-on-surface-variant">PROTOCOL CONDUIT:</span>
              <span class="font-label-md text-label-md text-tertiary font-semibold">${node.protocol}</span>
            </div>
            <div class="flex flex-col pt-1">
              <span class="font-label-sm text-label-sm text-on-surface-variant">HEALTH STATE:</span>
              <span class="font-label-md text-label-md text-on-surface font-bold">${node.status}</span>
            </div>
          </div>

          <!-- Fast Switch Node Strip -->
          <div class="flex flex-col gap-1">
            <span class="font-label-sm text-label-sm text-on-surface-variant uppercase font-semibold">Switch Topology Node:</span>
            <div class="flex flex-wrap gap-1">
              ${Object.keys(allNodes).map(k => `
                <button onclick="AnimationOverlayController.selectNode('${k}')" class="px-2 py-1 rounded text-[11px] font-bold transition-all ${k === this.activeNode ? 'bg-primary text-on-primary' : 'bg-surface-container text-on-surface hover:bg-surface-variant'}">
                  ${k}
                </button>
              `).join('')}
            </div>
          </div>

          <!-- Bottom Action Buttons: Cancel and Add to Mandate -->
          <div class="pt-space-xs flex items-center justify-between border-t border-outline-variant/30">
            <button onclick="AnimationOverlayController.close()" class="btn-cancel-action px-space-md py-space-xs rounded-xl bg-surface-container text-on-surface font-label-md text-label-md">
              Cancel &amp; Close
            </button>
            <button onclick="MandateCartController.add('sovereign-ai', 'Synapse Sovereign AI Cluster', 'SOVEREIGN MESH'); AnimationOverlayController.close();" class="px-space-md py-space-xs rounded-xl bg-primary-container text-on-primary-container font-label-md text-label-md font-bold hover:bg-primary hover:text-on-primary transition-all">
              Add Node Cluster to Mandate
            </button>
          </div>
        </div>
      </div>
    `;
  },

  renderGlobalSync(container) {
    const now = new Date();
    const cstTime = new Date(now.toLocaleString("en-US", { timeZone: "America/Chicago" })).toTimeString().split(' ')[0] + ' CST';
    const gmtTime = new Date(now.toLocaleString("en-US", { timeZone: "Europe/London" })).toTimeString().split(' ')[0] + ' GMT';
    const istTime = new Date(now.toLocaleString("en-US", { timeZone: "Asia/Kolkata" })).toTimeString().split(' ')[0] + ' IST';

    container.innerHTML = `
      <div class="flex flex-col gap-space-md">
        <!-- Enlarged World Map Canvas -->
        <div class="w-full bg-surface-container rounded-2xl p-space-md flex flex-col items-center justify-center relative overflow-hidden aspect-[2/1] shadow-inner">
          <svg class="w-full h-full" viewBox="0 0 700 350" fill="none">
            <!-- Pulsing Radar Hubs -->
            <circle cx="170" cy="130" r="9" fill="#775a00" class="animate-ping" opacity="0.6"/>
            <circle cx="170" cy="130" r="6" fill="#775a00"/>
            <text x="170" y="112" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#775a00" text-anchor="middle">WARRENVILLE, IL (USA)</text>

            <circle cx="360" cy="110" r="9" fill="#974355" class="animate-ping" opacity="0.6"/>
            <circle cx="360" cy="110" r="6" fill="#974355"/>
            <text x="360" y="92" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#974355" text-anchor="middle">LONDON HUB (EMEA)</text>

            <circle cx="530" cy="180" r="9" fill="#8c4f1c" class="animate-ping" opacity="0.6"/>
            <circle cx="530" cy="180" r="6" fill="#8c4f1c"/>
            <text x="530" y="162" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#8c4f1c" text-anchor="middle">INDIA CENTERS (APAC)</text>

            <!-- Arcs -->
            <path d="M 170 130 Q 265 60 360 110" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>
            <path d="M 360 110 Q 445 100 530 180" stroke="#c59b27" stroke-width="2.5" class="animate-dash-stream"/>
            <path d="M 530 180 Q 350 280 170 130" stroke="#974355" stroke-width="2" stroke-dasharray="4 4" opacity="0.7"/>

            <!-- Status Indicator Badge -->
            <rect x="250" y="275" width="200" height="40" rx="10" fill="#fff8f6" stroke="#c59b27" stroke-width="1.5"/>
            <circle cx="270" cy="295" r="5" fill="#775a00" class="animate-pulse"/>
            <text x="285" y="299" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#201a18">SYNC PROTOCOL: 24HR ACTIVE</text>
          </svg>
        </div>

        <!-- 3 Continuous Timezone Panels -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-space-sm">
          <div class="p-space-sm rounded-xl bg-surface-container flex flex-col">
            <span class="font-label-sm text-label-sm text-primary font-bold">WARRENVILLE, IL (USA HQ)</span>
            <span class="font-headline-md text-headline-md text-on-surface font-mono font-bold mt-1">${cstTime}</span>
            <span class="font-body-sm text-[12px] text-on-surface-variant">Core Strategy &amp; Executive Architectural Governance</span>
          </div>
          <div class="p-space-sm rounded-xl bg-surface-container flex flex-col">
            <span class="font-label-sm text-label-sm text-secondary font-bold">LONDON REGIONAL GATEWAY (UK)</span>
            <span class="font-headline-md text-headline-md text-on-surface font-mono font-bold mt-1">${gmtTime}</span>
            <span class="font-body-sm text-[12px] text-on-surface-variant">EMEA Advisory, Regulatory Compliance &amp; Banking Hub</span>
          </div>
          <div class="p-space-sm rounded-xl bg-surface-container flex flex-col">
            <span class="font-label-sm text-label-sm text-tertiary font-bold">INDIA EXCELLENCE CENTERS</span>
            <span class="font-headline-md text-headline-md text-on-surface font-mono font-bold mt-1">${istTime}</span>
            <span class="font-body-sm text-[12px] text-on-surface-variant">Continuous L3 Engineering, S/4HANA Migration Labs</span>
          </div>
        </div>

        <!-- Cancel / Close Action -->
        <div class="flex items-center justify-between pt-space-xs border-t border-outline-variant/30">
          <span class="font-body-sm text-body-sm text-on-surface-variant">Zero downtime shift handoff guarantee across all enterprise accounts.</span>
          <button onclick="AnimationOverlayController.close()" class="btn-cancel-action px-space-lg py-space-xs rounded-xl bg-surface-container text-on-surface font-label-md text-label-md">
            Cancel &amp; Close
          </button>
        </div>
      </div>
    `;
  },

  renderPipelineTraversal(container) {
    const stages = SumeruClientDB.tables.pipeline_stages;
    container.innerHTML = `
      <div class="flex flex-col gap-space-md">
        <p class="font-body-sm text-body-sm text-on-surface-variant">
          Step-by-step traversal of Sumeru's proprietary air-gapped sovereign intelligence pipeline. Each stage strictly verifies mathematical invariant contracts before proceeding to the next layer.
        </p>

        <!-- 7 Stages Horizontal Carousel -->
        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-space-xs">
          ${[1, 2, 3, 4, 5, 6, 7].map(s => `
            <div class="p-space-sm rounded-xl bg-surface-container flex flex-col justify-between border border-outline-variant/30 hover:border-primary transition-all">
              <span class="font-label-sm text-label-sm text-primary font-bold">STAGE 0${s}</span>
              <h5 class="font-label-md text-label-md text-on-surface font-bold my-1">${stages[s].short_desc}</h5>
              <span class="text-[11px] text-secondary font-mono">ENCLAVE SECURE</span>
            </div>
          `).join('')}
        </div>

        <div class="p-space-md rounded-xl bg-surface-container flex flex-col gap-space-xs">
          <span class="font-label-sm text-label-sm text-primary uppercase font-bold">SOVEREIGN AIR-GAP VALIDATION:</span>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-space-sm font-body-sm text-body-sm text-on-surface">
            <div class="p-2 rounded bg-surface flex items-center gap-2">
              <span class="material-symbols-outlined text-primary text-[18px]">lock</span>
              <span>100% On-Premise GPU Inference</span>
            </div>
            <div class="p-2 rounded bg-surface flex items-center gap-2">
              <span class="material-symbols-outlined text-secondary text-[18px]">verified_user</span>
              <span>Byzantine 4-Agent Consensus</span>
            </div>
            <div class="p-2 rounded bg-surface flex items-center gap-2">
              <span class="material-symbols-outlined text-tertiary text-[18px]">policy</span>
              <span>Zero External Cloud Telemetry</span>
            </div>
          </div>
        </div>

        <div class="flex items-center justify-between pt-space-xs border-t border-outline-variant/30">
          <button onclick="AnimationOverlayController.close()" class="btn-cancel-action px-space-md py-space-xs rounded-xl bg-surface-container text-on-surface font-label-md text-label-md">
            Cancel &amp; Close
          </button>
          <button onclick="PipelineController.runSimulation(); AnimationOverlayController.close();" class="px-space-md py-space-xs rounded-xl bg-primary text-on-primary font-label-md text-label-md font-bold">
            Simulate Full Sovereign Trace &rarr;
          </button>
        </div>
      </div>
    `;
  },

  renderCleanCoreHierarchy(container) {
    container.innerHTML = `
      <div class="flex flex-col gap-space-md">
        <p class="font-body-sm text-body-sm text-on-surface-variant">
          Visual decomposition of the SAP Clean Core hierarchy. Eliminating standard table modifications enables continuous SAP feature adoption without breaking customized workflows.
        </p>

        <div class="flex flex-col gap-2">
          <div class="p-3 rounded-xl bg-surface-container flex items-center justify-between">
            <span class="font-label-sm text-label-sm font-bold text-tertiary">TIER 5 • FIORI &amp; ADAPTIVE UI5</span>
            <span class="text-body-sm text-[12px] text-on-surface-variant">Decoupled UX consuming OData v4</span>
          </div>
          <div class="p-3 rounded-xl bg-surface-container flex items-center justify-between">
            <span class="font-label-sm text-label-sm font-bold text-secondary">TIER 4 • BTP SIDE-BY-SIDE EXTENSIONS</span>
            <span class="text-body-sm text-[12px] text-on-surface-variant">Node.js, Java, and CAP services running in decoupled cloud</span>
          </div>
          <div class="p-3 rounded-xl bg-surface-container flex items-center justify-between">
            <span class="font-label-sm text-label-sm font-bold text-tertiary">TIER 3 • SAP CLOUD ALM &amp; GOVERNANCE</span>
            <span class="text-body-sm text-[12px] text-on-surface-variant">Automated regression test suites &amp; telemetry monitoring</span>
          </div>
          <div class="p-3 rounded-xl bg-surface-container flex items-center justify-between">
            <span class="font-label-sm text-label-sm font-bold text-primary">TIER 2 • STANDARD PUBLIC APIS &amp; EVENT MESH</span>
            <span class="text-body-sm text-[12px] text-on-surface-variant">Officially released stable gateway contracts</span>
          </div>
          <div class="p-3 rounded-xl bg-primary-container text-on-primary-container flex items-center justify-between font-bold">
            <span class="font-label-sm text-label-sm">TIER 1 • PRISTINE SAP S/4HANA KERNEL</span>
            <span class="text-body-sm text-[12px]">Zero core modification • 100% Perpetual Upgrade Readiness</span>
          </div>
        </div>

        <div class="flex items-center justify-between pt-space-xs border-t border-outline-variant/30">
          <button onclick="AnimationOverlayController.close()" class="btn-cancel-action px-space-md py-space-xs rounded-xl bg-surface-container text-on-surface font-label-md text-label-md">
            Cancel &amp; Close
          </button>
          <button onclick="CleanCoreController.openAuditModal(); AnimationOverlayController.close();" class="px-space-md py-space-xs rounded-xl bg-primary text-on-primary font-label-md text-label-md font-bold">
            Launch Clean Core Audit Calculator &rarr;
          </button>
        </div>
      </div>
    `;
  }
};

window.openAnimationOverlay = function(type, context) {
  AnimationOverlayController.open(type, context);
};

// ========================================================
// 5. MANDATE CART CONTROLLER (Image Cart / Solution Cart)
// Lets users collect architectural solutions & industry practices
// ========================================================
const MandateCartController = {
  open() {
    this.render();
    const drawer = document.getElementById('mandate-cart-drawer');
    if (drawer) {
      drawer.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }
  },

  close() {
    const drawer = document.getElementById('mandate-cart-drawer');
    if (drawer) {
      drawer.classList.add('hidden');
      document.body.style.overflow = '';
    }
  },

  add(id, title, category, type = 'solution') {
    const exists = SumeruClientDB.tables.mandate_cart.some(item => item.id === id);
    if (!exists) {
      SumeruClientDB.tables.mandate_cart.push({ id, title, category, type });
      SumeruClientDB.save();
    }
    this.updateBadge();
    this.open();
  },

  remove(id) {
    SumeruClientDB.tables.mandate_cart = SumeruClientDB.tables.mandate_cart.filter(item => item.id !== id);
    SumeruClientDB.save();
    this.render();
    this.updateBadge();
  },

  clear() {
    SumeruClientDB.tables.mandate_cart = [];
    SumeruClientDB.save();
    this.render();
    this.updateBadge();
  },

  updateBadge() {
    const count = SumeruClientDB.tables.mandate_cart.length;
    document.querySelectorAll('.cart-count-badge').forEach(badge => {
      badge.textContent = count;
      badge.style.display = count > 0 ? 'inline-flex' : 'none';
    });
  },

  render() {
    const list = document.getElementById('cart-items-list');
    const emptyState = document.getElementById('cart-empty-state');
    const footerActions = document.getElementById('cart-footer-actions');
    const items = SumeruClientDB.tables.mandate_cart;

    if (!list) return;

    if (items.length === 0) {
      list.innerHTML = '';
      if (emptyState) emptyState.classList.remove('hidden');
      if (footerActions) footerActions.classList.add('hidden');
      return;
    }

    if (emptyState) emptyState.classList.add('hidden');
    if (footerActions) footerActions.classList.remove('hidden');

    list.innerHTML = items.map(item => `
      <div class="p-space-sm rounded-xl bg-surface border border-outline-variant/30 flex items-start justify-between gap-space-xs shadow-sm">
        <div class="flex flex-col">
          <span class="font-label-sm text-[10px] text-primary uppercase font-bold tracking-wider">${item.category}</span>
          <h5 class="font-label-md text-label-md text-on-surface font-semibold">${item.title}</h5>
          <span class="text-[11px] text-tertiary">Verified Sovereign Component</span>
        </div>
        <button onclick="MandateCartController.remove('${item.id}')" class="text-on-surface-variant hover:text-error transition-colors p-1" title="Remove component">
          <span class="material-symbols-outlined text-[18px]">delete</span>
        </button>
      </div>
    `).join('');
  },

  transferToAdvisory() {
    const items = SumeruClientDB.tables.mandate_cart;
    const summary = items.map(i => `• ${i.title} (${i.category})`).join('\n');
    const textarea = document.querySelector('#dispatch-form textarea');
    if (textarea) {
      textarea.value = `Mandate Scope from Architectural Cart:\n${summary}\n\nPlease prepare technical briefing and SLA recommendations for the above practices.`;
    }
    this.close();
    const dispatchSec = document.getElementById('executive-dispatch');
    if (dispatchSec) {
      dispatchSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
};

window.openMandateCart = function() {
  MandateCartController.open();
};

// ========================================================
// 6. INDUSTRY CASE STUDY & IMAGE CARD CONTROLLER
// Clicking any photo card opens rich overlay with full details & cancel option
// ========================================================
const IndustryController = {
  openModal(key) {
    const data = SumeruClientDB.tables.industry_case_studies[key];
    if (!data) return;

    const modal = document.getElementById('industry-case-modal');
    if (!modal) return;

    document.getElementById('ind-modal-badge').textContent = data.badge;
    document.getElementById('ind-modal-title').textContent = data.name;
    document.getElementById('ind-modal-image').src = data.image;
    document.getElementById('ind-modal-image').alt = data.name;
    document.getElementById('ind-modal-challenge').textContent = data.challenge;
    document.getElementById('ind-modal-solution').textContent = data.solution;

    // Metrics
    const metricsContainer = document.getElementById('ind-modal-metrics');
    metricsContainer.innerHTML = data.metrics.map(m => `
      <div class="p-space-sm rounded-xl bg-surface-container flex flex-col">
        <span class="font-label-sm text-label-sm text-on-surface-variant uppercase">${m.label}</span>
        <span class="font-headline-sm text-headline-sm text-primary font-bold mt-1">${m.val}</span>
      </div>
    `).join('');

    // Compliance badges
    const compContainer = document.getElementById('ind-modal-compliance');
    compContainer.innerHTML = data.compliance.map(c => `
      <span class="px-space-xs py-0.5 rounded bg-surface-container text-tertiary font-label-sm text-label-sm font-semibold">${c}</span>
    `).join('');

    // Add to cart button hook
    const addBtn = document.getElementById('ind-modal-add-cart');
    if (addBtn) {
      addBtn.onclick = () => {
        MandateCartController.add(data.id, data.name, data.badge, 'industry');
        IndustryController.closeModal();
      };
    }

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  },

  closeModal() {
    const modal = document.getElementById('industry-case-modal');
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

window.openIndustryModal = function(key) {
  IndustryController.openModal(key);
};

// ========================================================
// 7. ARCHITECTURAL PILLAR & TRUST CREDENTIAL CONTROLLER
// ========================================================
const PillarModalController = {
  pillars: {
    'systems-integration': {
      title: 'Systems Integration & Middleware',
      headline: 'Harmonizing heterogenous legacy mainframes, microservices, and partner APIs.',
      description: 'Since 1994, Sumeru has resolved complex multi-generation architectural sprawl. We deploy non-blocking event loops, Kafka topics, and REST/gRPC wrappers around legacy systems to ensure reliable ACID transactions without rewriting proven core code.'
    },
    'alm-lifecycle': {
      title: 'ALM Lifecycle Governance',
      headline: 'Methodical governance from blueprint design, rigorous staging, to continuous telemetry.',
      description: 'Our Application Lifecycle Management framework guarantees full compliance traceability. Automated gating ensures code cannot reach production without formal invariant verification, security static analysis, and zero-drift infrastructure tests.'
    },
    'custom-dev': {
      title: 'Custom Sovereign Development',
      headline: 'High-throughput microservices, sub-millisecond trading relays, and mission-critical engines.',
      description: 'Polyglot systems built in Go, Rust, Java, and modern Python. Optimized for concurrency, memory efficiency, and deterministic latency SLAs.'
    },
    'package-deployment': {
      title: 'Enterprise Package Deployment',
      headline: 'Turnkey rollouts of Tier-1 ERP and governance tools with zero operational downtime.',
      description: 'Blue/green phased deployment strategies allowing massive institutional cutovers with automated rollback snapshots and synchronized live data validation.'
    },
    'crm-erp-sync': {
      title: 'CRM & ERP Synchronization',
      headline: 'Bi-directional event synchronization maintaining ACID compliance across hybrid clouds.',
      description: 'Eliminates dirty reads and split-brain data across Salesforce, SAP, and custom data lakes through distributed transaction consensus protocols.'
    },
    'qa-resiliency': {
      title: 'QA & Resiliency Chaos Testing',
      headline: 'Automated regression suites, chaos engineering, and continuous penetration simulations.',
      description: 'Continuous automated validation of failure states, latency degradation, and partition tolerance inspired by Chaos Monkey and formal verification models.'
    },
    'business-integration': {
      title: 'Business & B2B Integration',
      headline: 'B2B EDI pipelines, sovereign supply chain nodes, and partner extranet governance.',
      description: 'Secure multi-tenant partner extranets complying with AS2, EDIFACT, and sovereign cryptographic standards.'
    },
    'app-management': {
      title: 'Application Management Services',
      headline: '24/7/365 follow-the-sun L3 engineering, patch compliance, and automated telemetry remediation.',
      description: 'Unbroken operational uptime through our synchronized Warrenville, London, and India operations centers.'
    }
  },

  open(key) {
    const item = this.pillars[key];
    if (!item) return;

    const modal = document.getElementById('pillar-modal');
    if (!modal) return;

    document.getElementById('pillar-modal-title').textContent = item.title;
    document.getElementById('pillar-modal-headline').textContent = item.headline;
    document.getElementById('pillar-modal-desc').textContent = item.description;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  },

  close() {
    const modal = document.getElementById('pillar-modal');
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

window.openPillarModal = function(key) {
  PillarModalController.open(key);
};

// ========================================================
// 8. REGION & CURRENCY SWITCHER MODAL
// ========================================================
const RegionModalController = {
  currentRegion: 'US • USD',

  open() {
    const modal = document.getElementById('region-modal');
    if (modal) {
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }
  },

  close() {
    const modal = document.getElementById('region-modal');
    if (modal) {
      modal.classList.add('hidden');
      document.body.style.overflow = '';
    }
  },

  select(regStr) {
    this.currentRegion = regStr;
    document.querySelectorAll('.region-currency-label').forEach(el => {
      el.textContent = regStr;
    });
    this.close();
  }
};

window.openRegionModal = function() {
  RegionModalController.open();
};

// ========================================================
// 9. TOPOLOGY CONTROLLER (Synapse Mesh Matrix Live Telemetry)
// ========================================================
const TopologyController = {
  currentNode: 'SUMERU_CORE',
  pollInterval: null,

  init() {
    this.updateClock();
    setInterval(() => this.updateClock(), 1000);
    this.fetchNodeTelemetry(this.currentNode);

    // Background polling for live jitter & telemetry updates
    this.pollInterval = setInterval(() => {
      this.fetchNodeTelemetry(this.currentNode, false);
    }, 4000);
  },

  updateClock() {
    const clockEl = document.getElementById('topology-clock');
    if (clockEl) {
      const now = new Date();
      clockEl.textContent = now.toTimeString().split(' ')[0] + ' UTC';
    }
  },

  async fetchNodeTelemetry(nodeKey, animate = true) {
    this.currentNode = nodeKey;
    try {
      const res = await fetch(`/api/telemetry/nodes/${nodeKey}`);
      const data = await res.json();
      this.renderTelemetry(data, animate);
    } catch (err) {
      console.warn('Fallback telemetry:', err);
    }
  },

  renderTelemetry(data, animate) {
    const nameEl = document.getElementById('node-name');
    const latencyEl = document.getElementById('node-latency');
    const statusEl = document.getElementById('node-status');
    const protocolEl = document.getElementById('node-protocol');

    if (nameEl) nameEl.textContent = data.name;
    if (latencyEl) latencyEl.textContent = `LATENCY: ${data.latency_ms}ms`;
    if (statusEl) statusEl.textContent = `STATE: ${data.status}`;
    if (protocolEl) protocolEl.textContent = `PROTOCOL: ${data.protocol}`;

    const container = document.getElementById('telemetry-readout');
    if (container && animate) {
      container.classList.remove('animate-fade-in');
      void container.offsetWidth;
      container.classList.add('animate-fade-in');
    }
  }
};

window.inspectNode = function(key) {
  TopologyController.fetchNodeTelemetry(key, true);
};

// ========================================================
// 10. SOLUTIONS & SPECIFICATIONS CONTROLLER
// ========================================================
const SolutionsController = {
  activeCategory: 'all',

  init() {
    this.bindEvents();
  },

  bindEvents() {
    const specButtons = document.querySelectorAll('.solution-card');
    const solutionIds = [
      'sovereign-ai',
      'sap-modernization',
      'hybrid-cloud',
      'data-fabric',
      'enterprise-security',
      'app-engineering'
    ];

    specButtons.forEach((card, index) => {
      // Entire card clickable to open specification
      card.style.cursor = 'pointer';
      card.addEventListener('click', (e) => {
        if (!e.target.closest('button')) {
          SolutionsController.openSpecificationModal(solutionIds[index]);
        }
      });
    });
  },

  filter(category) {
    this.activeCategory = category;
    const cards = document.querySelectorAll('.solution-card');
    const buttons = document.querySelectorAll('.solution-filter-btn');

    buttons.forEach(btn => {
      if (btn.getAttribute('data-filter') === category) {
        btn.className = 'solution-filter-btn px-space-sm py-space-xs rounded-lg font-label-md text-label-md transition-all bg-primary-container text-on-primary-container shadow-sm';
      } else {
        btn.className = 'solution-filter-btn px-space-sm py-space-xs rounded-lg font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all';
      }
    });

    cards.forEach(card => {
      const cardCat = card.getAttribute('data-category');
      if (category === 'all' || cardCat === category) {
        card.style.display = 'flex';
        card.classList.add('animate-fade-in');
      } else {
        card.style.display = 'none';
        card.classList.remove('animate-fade-in');
      }
    });
  },

  async openSpecificationModal(solutionId) {
    try {
      const res = await fetch(`/api/solutions/${solutionId}`);
      const data = await res.json();

      document.getElementById('modal-spec-category').textContent = data.category_label;
      document.getElementById('modal-spec-title').textContent = data.title;
      document.getElementById('modal-spec-headline').textContent = data.headline;
      document.getElementById('modal-spec-overview').textContent = data.architecture_overview;
      document.getElementById('modal-spec-sla').textContent = data.sla_guarantee;

      const delivContainer = document.getElementById('modal-spec-deliverables');
      delivContainer.innerHTML = '';
      data.deliverables.forEach(item => {
        const li = document.createElement('li');
        li.className = 'flex items-start gap-space-xs font-body-sm text-body-sm text-on-surface';
        li.innerHTML = `<span class="material-symbols-outlined text-primary text-[18px] shrink-0 mt-0.5">check_circle</span><span>${item}</span>`;
        delivContainer.appendChild(li);
      });

      const compContainer = document.getElementById('modal-spec-compliance');
      compContainer.innerHTML = '';
      data.compliance_frameworks.forEach(tag => {
        const badge = document.createElement('span');
        badge.className = 'px-space-xs py-0.5 rounded bg-surface-container text-tertiary font-label-sm text-label-sm font-semibold';
        badge.textContent = tag;
        compContainer.appendChild(badge);
      });

      // Hook up add to cart in spec modal
      const addCartBtn = document.getElementById('modal-spec-add-cart');
      if (addCartBtn) {
        addCartBtn.onclick = () => {
          MandateCartController.add(data.id, data.title, data.category_label, 'solution');
          SolutionsController.closeSpecificationModal();
        };
      }

      const modal = document.getElementById('spec-modal');
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    } catch (err) {
      console.error(err);
    }
  },

  closeSpecificationModal() {
    const modal = document.getElementById('spec-modal');
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

window.filterSolutions = function(cat) {
  SolutionsController.filter(cat);
};

// ========================================================
// 11. SOVEREIGN REASONING PIPELINE CONTROLLER
// ========================================================
const PipelineController = {
  currentStep: 1,

  async selectStep(stepNum) {
    this.currentStep = stepNum;

    const buttons = document.querySelectorAll('.pipeline-step-btn');
    buttons.forEach(btn => {
      const step = parseInt(btn.getAttribute('data-step'), 10);
      if (step === stepNum) {
        btn.className = 'pipeline-step-btn p-space-sm rounded-xl bg-surface text-left transition-all shadow-sm ring-2 ring-primary';
        btn.querySelector('span').className = 'font-label-sm text-label-sm text-primary font-bold';
      } else {
        btn.className = 'pipeline-step-btn p-space-sm rounded-xl bg-surface-container text-left transition-all hover:bg-surface';
        btn.querySelector('span').className = 'font-label-sm text-label-sm text-on-surface-variant font-bold';
      }
    });

    try {
      const res = await fetch(`/api/pipeline/stages/${stepNum}`);
      const data = await res.json();

      document.getElementById('step-eyebrow').textContent = `STAGE 0${data.stage_number} OF 07 • ${data.code}`;
      document.getElementById('step-title').textContent = data.name;
      document.getElementById('step-desc').textContent = data.full_description;

      const keys = Object.keys(data.stats);
      if (keys[0]) {
        document.getElementById('step-stat-1').textContent = data.stats[keys[0]];
        document.getElementById('step-stat-1').parentElement.querySelector('span').textContent = keys[0] + ':';
      }
      if (keys[1]) {
        document.getElementById('step-stat-2').textContent = data.stats[keys[1]];
        document.getElementById('step-stat-2').parentElement.querySelector('span').textContent = keys[1] + ':';
      }
      if (keys[2]) {
        document.getElementById('step-stat-3').textContent = data.stats[keys[2]];
        document.getElementById('step-stat-3').parentElement.querySelector('span').textContent = keys[2] + ':';
      }

      const card = document.getElementById('step-detail-card');
      card.classList.remove('animate-fade-in');
      void card.offsetWidth;
      card.classList.add('animate-fade-in');
    } catch (err) {
      console.warn('Pipeline stage error:', err);
    }
  },

  async runSimulation() {
    const btn = document.getElementById('btn-run-simulation');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<span class="material-symbols-outlined text-[18px] animate-spin">refresh</span><span>Executing Sovereign Air-Gapped Trace...</span>';
    btn.disabled = true;

    try {
      const res = await fetch('/api/pipeline/simulate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          mandate_or_query: 'Cross-border SAP S/4HANA PO validation and tariff optimization',
          enable_anti_hallucination: true,
          target_environment: 'SOVEREIGN_ON_PREM_VPC'
        })
      });

      const data = await res.json();
      this.displaySimulationResults(data);
    } catch (err) {
      console.error('Simulation error:', err);
    } finally {
      btn.innerHTML = originalText;
      btn.disabled = false;
    }
  },

  displaySimulationResults(data) {
    const modal = document.getElementById('sim-result-modal');
    document.getElementById('sim-exec-id').textContent = data.execution_id;
    document.getElementById('sim-latency').textContent = `${data.total_latency_ms}ms (Realtime End-to-End)`;
    document.getElementById('sim-output').textContent = data.final_output_preview;

    const list = document.getElementById('sim-stages-list');
    list.innerHTML = '';
    data.stages_executed.forEach(s => {
      const div = document.createElement('div');
      div.className = 'p-space-xs rounded bg-surface border border-outline-variant/30 flex flex-col gap-0.5';
      div.innerHTML = `
        <div class="flex items-center justify-between font-label-sm text-label-sm">
          <span class="font-bold text-primary">Stage 0${s.stage}: ${s.name}</span>
          <span class="text-tertiary">${s.duration_ms}ms • ${s.status}</span>
        </div>
        <p class="font-body-sm text-[12px] text-on-surface-variant">${s.detail}</p>
      `;
      list.appendChild(div);
    });

    const prov = document.getElementById('sim-provenance');
    prov.innerHTML = '';
    data.provenance_trace.forEach(trace => {
      const tag = document.createElement('div');
      tag.className = 'font-mono text-[11px] text-on-surface-variant bg-surface-container px-2 py-1 rounded truncate';
      tag.textContent = trace;
      prov.appendChild(tag);
    });

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  },

  closeSimulationModal() {
    const modal = document.getElementById('sim-result-modal');
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = '';
  }
};

window.selectPipelineStep = function(stepNum) {
  PipelineController.selectStep(stepNum);
};

// ========================================================
// 12. SAP CLEAN CORE ASSESSMENT CONTROLLER
// ========================================================
const CleanCoreController = {
  openAuditModal() {
    const modal = document.getElementById('clean-core-modal');
    if (modal) {
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }
  },

  closeAuditModal() {
    const modal = document.getElementById('clean-core-modal');
    if (modal) {
      modal.classList.add('hidden');
      document.body.style.overflow = '';
    }
  },

  async submitAudit(e) {
    e.preventDefault();
    const version = document.getElementById('sap-version-input').value;
    const zCount = parseInt(document.getElementById('sap-zcount-input').value, 10) || 0;
    const directDb = document.getElementById('sap-directdb-input').checked;
    const btpRate = document.getElementById('sap-btp-input').value;
    const industry = document.getElementById('sap-industry-input').value;

    const btn = document.getElementById('sap-audit-submit-btn');
    btn.disabled = true;
    btn.innerHTML = '<span class="material-symbols-outlined text-[18px] animate-spin">refresh</span><span>Evaluating Clean Core Index...</span>';

    try {
      const res = await fetch('/api/sap/audit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sap_version: version,
          custom_z_programs_count: zCount,
          direct_db_modifications: directDb,
          btp_adoption_rate: btpRate,
          industry: industry
        })
      });

      const data = await res.json();

      document.getElementById('audit-form-view').classList.add('hidden');
      const resultView = document.getElementById('audit-result-view');
      resultView.classList.remove('hidden');

      document.getElementById('audit-score-num').textContent = `${data.clean_core_index_pct}/100`;
      document.getElementById('audit-grade').textContent = data.compliance_grade;
      document.getElementById('audit-risk').textContent = data.risk_level;
      document.getElementById('audit-savings').textContent = data.estimated_migration_savings;
      document.getElementById('audit-pathway').textContent = data.recommended_pathway;

      const recContainer = document.getElementById('audit-tier-recs');
      recContainer.innerHTML = '';
      data.tier_recommendations.forEach(rec => {
        const item = document.createElement('div');
        item.className = 'p-space-xs rounded bg-surface flex items-start gap-space-xs border border-outline-variant/30';
        item.innerHTML = `
          <span class="font-label-sm text-label-sm font-bold text-primary shrink-0">${rec.tier}:</span>
          <span class="font-body-sm text-[12px] text-on-surface">${rec.action}</span>
        `;
        recContainer.appendChild(item);
      });
    } catch (err) {
      console.error(err);
    } finally {
      btn.disabled = false;
      btn.innerHTML = 'Calculate Clean Core Index';
    }
  },

  resetAuditForm() {
    document.getElementById('audit-form-view').classList.remove('hidden');
    document.getElementById('audit-result-view').classList.add('hidden');
  }
};

// ========================================================
// 13. EXECUTIVE ADVISORY DISPATCH CONTROLLER
// ========================================================
const AdvisoryController = {
  async handleSubmit(e) {
    e.preventDefault();
    const form = document.getElementById('dispatch-form');
    const submitBtn = form.querySelector('button[type="submit"]');

    const nameInput = form.querySelector('input[type="text"][placeholder*="Eleanor"]');
    const emailInput = form.querySelector('input[type="email"]');
    const orgInput = form.querySelector('input[type="text"][placeholder*="Logistics"]');
    const practiceSelect = form.querySelector('select');
    const mandateTextarea = form.querySelector('textarea');
    const ndaCheck = document.getElementById('nda-box');

    const payload = {
      executive_name: nameInput ? nameInput.value.trim() : 'Executive Partner',
      corporate_email: emailInput ? emailInput.value.trim() : 'executive@enterprise.com',
      organization: orgInput ? orgInput.value.trim() : 'Enterprise Partner',
      focus_practice: practiceSelect ? practiceSelect.value : 'sap',
      mandate_scope: mandateTextarea ? mandateTextarea.value.trim() : '',
      nda_requested: ndaCheck ? ndaCheck.checked : false
    };

    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="material-symbols-outlined text-[18px] animate-spin">refresh</span><span>Transmitting over Sovereign Conduit...</span>';

    try {
      const res = await fetch('/api/advisory/dispatch', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      form.classList.add('hidden');

      const successBox = document.getElementById('dispatch-success');
      successBox.classList.remove('hidden');

      document.getElementById('ticket-id-display').textContent = data.ticket_id;
      document.getElementById('ticket-partner-display').textContent = data.assigned_partner;
      document.getElementById('ticket-target-display').textContent = data.target_callback_time_utc;
      document.getElementById('ticket-seal-display').textContent = data.security_hash;

    } catch (err) {
      console.error(err);
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<span class="material-symbols-outlined text-[18px]">send</span><span>Dispatch Advisory Request</span>';
    }
  }
};

window.handleDispatchSubmit = function(e) {
  AdvisoryController.handleSubmit(e);
};

// ========================================================
// 14. CLIENT PORTAL AUTHENTICATION & DASHBOARD
// ========================================================
const PortalController = {
  openModal() {
    const modal = document.getElementById('portal-modal');
    if (modal) {
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }
  },

  closeModal() {
    const modal = document.getElementById('portal-modal');
    if (modal) {
      modal.classList.add('hidden');
      document.body.style.overflow = '';
    }
  },

  async handleLogin(e) {
    e.preventDefault();
    const email = document.getElementById('portal-email').value.trim();
    const key = document.getElementById('portal-key').value.trim();
    const errEl = document.getElementById('portal-error');
    errEl.classList.add('hidden');

    try {
      const res = await fetch('/api/portal/authenticate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email, access_key: key })
      });

      if (!res.ok) throw new Error('Invalid credentials');
      const data = await res.json();
      this.renderDashboard(data);
    } catch (err) {
      errEl.textContent = 'Authentication denied. Verify your enterprise email and authorization key.';
      errEl.classList.remove('hidden');
    }
  },

  renderDashboard(data) {
    document.getElementById('portal-login-view').classList.add('hidden');
    const dashView = document.getElementById('portal-dashboard-view');
    dashView.classList.remove('hidden');

    document.getElementById('portal-client-title').textContent = data.client_name;
    document.getElementById('portal-org-title').textContent = data.organization;
    document.getElementById('portal-stat-uptime').textContent = data.sla_uptime;
    document.getElementById('portal-stat-nodes').textContent = `${data.synapse_nodes_online} Active Nodes`;
    document.getElementById('portal-stat-score').textContent = data.clean_core_score;

    const depList = document.getElementById('portal-deployments-list');
    depList.innerHTML = '';
    data.recent_deployments.forEach(d => {
      const div = document.createElement('div');
      div.className = 'p-space-xs rounded bg-surface border border-outline-variant/30 flex items-center justify-between text-body-sm text-[12px]';
      div.innerHTML = `
        <div class="flex items-center gap-space-xs">
          <span class="w-2 h-2 rounded-full bg-primary-container"></span>
          <span class="font-bold text-on-surface">${d.component}</span>
          <span class="text-tertiary">(${d.release})</span>
        </div>
        <span class="font-mono text-primary font-semibold">${d.region}</span>
      `;
      depList.appendChild(div);
    });
  }
};

// ========================================================
// 15. INITIALIZATION ON DOM READY
// ========================================================
document.addEventListener('DOMContentLoaded', () => {
  NavigationController.init();
  TopologyController.init();
  SolutionsController.init();
  MandateCartController.updateBadge();

  // Attach backdrop dismiss to all modals
  document.querySelectorAll('.modal-backdrop-anim').forEach(backdrop => {
    backdrop.addEventListener('click', function(e) {
      if (e.target === this) {
        this.classList.add('hidden');
        document.body.style.overflow = '';
      }
    });
  });

  // Bind Client Portal header links
  document.querySelectorAll('[data-path="client-portal-access"]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      PortalController.openModal();
    });
  });
});
