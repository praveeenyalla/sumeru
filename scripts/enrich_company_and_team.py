"""
Module: enrich_company_and_team.py
Contains enriched topic cards for Company Overview, Leadership, Quality, Partners, Careers, and Contact.
"""

COMPANY_TOPICS = [
    {
        "id": "company-profile",
        "slug": "company-profile",
        "nav_label": "Company Profile",
        "badge": "PROFILE • ENTERPRISE CAPABILITY",
        "title": "Executive Company Introduction & Operating Model",
        "summary": "Sumeru Technologies is a global software services company delivering consulting, systems integration, and outsourcing solutions to Fortune 500 and multinational organizations worldwide.",
        "lead": "Sumeru Technologies is a global software services company delivering consulting, systems integration, and outsourcing solutions to Fortune 500 and multinational organizations worldwide.",
        "image": {
            "url": "/static/images/content/about-us-600x578.jpg",
            "alt": "Sumeru Company Overview",
            "caption": "Executive Company Profile & Operating Architecture"
        },
        "content": [
            {
                "heading": "Executive Introduction",
                "body": "Sumeru Technologies LLC operates as a premier software services partner for enterprises seeking high-reliability Systems Integration, Application Lifecycle Management, Custom Application Development, Package Deployment, and Managed Operations.\n\nHeadquartered in Warrenville, Illinois, with an EMEA hub in Madrid, Spain, and premier global delivery centers in Hyderabad and Bangalore, India, Sumeru provides an optimal blend of local executive leadership and distributed technical execution."
            },
            {
                "heading": "Business Operating Model",
                "body": "Our operating model is engineered to eliminate technical debt and avoid runaway implementation expenditures. By maintaining dedicated Centers of Excellence across SAP, Oracle, Cloud Integration, and Database Administration, we deliver proven architectures that scale reliably with enterprise growth."
            }
        ],
        "methodology": [
            {"step": "STAGE 01", "name": "Strategic Alignment", "desc": "Collaborating with client executive sponsors to establish clear business goals and ROI benchmarks."},
            {"step": "STAGE 02", "name": "Architectural Design", "desc": "Designing complete, scalable solutions that integrate seamlessly with existing enterprise systems."},
            {"step": "STAGE 03", "name": "Phased Delivery", "desc": "Applying agile delivery rituals and automated regression testing to ensure predictable milestones."},
            {"step": "STAGE 04", "name": "Managed Operations", "desc": "Providing 24x7 ongoing systems administration, application maintenance, and SLA tracking."}
        ],
        "technologies": ["Systems Integration", "SAP ERP", "Oracle EBS", "Cloud Modernization", "Database Administration"],
        "deliverables": [
            "Corporate Capability Matrix",
            "Executive Service Portfolio Blueprint",
            "Global Delivery Model SLA Guarantee"
        ],
        "qa": {
            "q": "What is Sumeru's engagement approach for new enterprise clients?",
            "a": "We begin with a focused 2-week Discovery workshop assessing current architecture, pain points, and strategic priorities. This produces an Operational Baseline Report and a fixed-scope roadmap before commercial licensing or implementation commitments."
        },
        "sources": [
            {"title": "Sumeru Technologies Corporate Overview", "url": "https://sumerutechnologies.com/company", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    },
    {
        "id": "service-portfolio-overview",
        "slug": "service-portfolio-overview",
        "nav_label": "Service Portfolio",
        "badge": "PORTFOLIO • END-TO-END SERVICES",
        "title": "Comprehensive Service Portfolio Across 5 Core Practices",
        "summary": "From strategic architecture consulting and SAP S/4HANA transitions to 24x7 database administration and specialized staffing, our portfolio covers the full enterprise lifecycle.",
        "lead": "From strategic architecture consulting and SAP S/4HANA transitions to 24x7 database administration and specialized staffing, our portfolio covers the full enterprise lifecycle.",
        "image": {
            "url": "/static/images/content/sumeru_enterprise_hero_bg.jpg",
            "alt": "Sumeru Service Portfolio",
            "caption": "Five Primary Practice Areas Delivering Enterprise Agility"
        },
        "content": [
            {
                "heading": "Five Interconnected Practices",
                "body": "Sumeru's capabilities span five primary practices: Consulting (strategy, process analysis, telemetry), Enterprise Solutions (SAP, Oracle, transaction systems), Information Management (BI, storage, security, MDM), Outsourcing (remote DBA, application maintenance, ODC), and Professional Services (staff augmentation, PMP management).\n\nEach practice is headed by seasoned industry leaders with dedicated engineering pods in our delivery centers."
            },
            {
                "heading": "Lifecycle Continuity",
                "body": "Because all five practices share unified architectural standards and our signature 4D methodology, clients transition seamlessly from initial strategy through deployment and multi-year operations under single accountability."
            }
        ],
        "methodology": [
            {"step": "PRACTICE 01", "name": "Consulting", "desc": "Strategic IT planning, BPA workflow optimization, and Clean Core architecture design."},
            {"step": "PRACTICE 02", "name": "Enterprise Solutions", "desc": "SAP S/4HANA migrations, Oracle EBS customization, and transaction processing engines."},
            {"step": "PRACTICE 03", "name": "Information Management", "desc": "Adaptive MDM with Kalido/Informatica, SAN/NAS storage, and cyber governance."},
            {"step": "PRACTICE 04", "name": "Outsourcing & Staffing", "desc": "24x7 remote database administration, application maintenance, and senior staffing."}
        ],
        "technologies": ["SAP S/4HANA", "Oracle Fusion", "Informatica", "Kalido", "MuleSoft", "AWS/Azure"],
        "deliverables": [
            "End-to-End Enterprise Service Catalog",
            "Cross-Practice Delivery Framework",
            "Multi-Tier Support SLA Matrix"
        ],
        "qa": {
            "q": "Can clients engage Sumeru for a single practice or only full-lifecycle projects?",
            "a": "Clients frequently begin with a targeted engagement—such as an architecture audit, a database tuning mandate, or specialized staff augmentation—and expand as trust and business impact are demonstrated."
        },
        "sources": [
            {"title": "Sumeru Services Architecture", "url": "https://sumerutechnologies.com/services", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

TEAM_TOPICS = [
    {
        "id": "leadership-philosophy",
        "slug": "leadership-philosophy",
        "nav_label": "Practitioner Leadership",
        "badge": "LEADERSHIP • PRACTITIONER GOVERNANCE",
        "title": "Practitioner-Led Executive Leadership & Technical Governance",
        "summary": "Guided by hands-on engineering leaders who combine executive business acumen with deep architectural expertise in enterprise software systems.",
        "lead": "Guided by hands-on engineering leaders who combine executive business acumen with deep architectural expertise in enterprise software systems.",
        "image": {
            "url": "/static/images/content/Professional-Services-580x400.jpg",
            "alt": "Practitioner Leadership and Engineering Architects",
            "caption": "Hands-on Technical Leadership & Architectural Oversight"
        },
        "content": [
            {
                "heading": "Hands-On Engineering Mastery",
                "body": "At Sumeru Technologies, leadership is defined by practical engineering mastery, not theoretical management. Our practice heads and senior partners have spent decades in the trenches designing ERP cores, high-throughput message fabrics, and mission-critical databases for Fortune 500 corporations.\n\nEvery client engagement is directly sponsored by an executive partner who remains actively engaged throughout Discovery, Design, and Deployment to ensure architectural integrity and milestone predictability."
            },
            {
                "heading": "Architectural Review Board (ARB)",
                "body": "We maintain an internal Architectural Review Board composed of our senior-most technical directors. The ARB reviews all client blueprints, interface contracts, and non-functional specifications before deployment, ensuring zero single points of failure."
            }
        ],
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
        },
        "sources": [
            {"title": "Sumeru Leadership & Team", "url": "https://sumerutechnologies.com/company/team", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    },
    {
        "id": "solution-architects",
        "slug": "solution-architects",
        "nav_label": "Solution Architects",
        "badge": "EXPERTISE • SYSTEMS ENGINEERING",
        "title": "Enterprise Solution Architects & Systems Engineering Practice",
        "summary": "Certified solution architects who bridge business requirements and scalable cloud/on-premise architectures with zero technical debt.",
        "lead": "Certified solution architects who bridge business requirements and scalable cloud/on-premise architectures with zero technical debt.",
        "image": {
            "url": "/static/images/content/Architecture-Implementation-580x400.jpg",
            "alt": "Enterprise Solution Architects",
            "caption": "Sumeru Enterprise Solution Architects and Systems Engineers"
        },
        "content": [
            {
                "heading": "Architectural Rigor",
                "body": "Sumeru's architects specialize in designing multi-tier, high-availability environments that integrate legacy mainframe cores with modern cloud services and ERP platforms. We enforce Clean Core principles, decoupled API middleware, and automated testability so that enterprise applications scale smoothly with business growth."
            },
            {
                "heading": "Cross-Platform Expertise",
                "body": "Our architects hold top-tier certifications across SAP, Oracle, AWS, Azure, and TOGAF, enabling objective evaluation of cloud vs on-premise trade-offs and buy-vs-build options."
            }
        ],
        "methodology": [
            {"step": "STAGE 01", "name": "NFR Benchmarking", "desc": "Establishing strict throughput, latency, security, and RPO/RTO disaster recovery metrics."},
            {"step": "STAGE 02", "name": "Topology Specification", "desc": "Blueprinting modular microservices, Clean Core ERP extensions, and hybrid cloud fabrics."},
            {"step": "STAGE 03", "name": "Interface Contract Modeling", "desc": "Specifying synchronous/asynchronous API contracts, event streams, and schemas."},
            {"step": "STAGE 04", "name": "Implementation Quality Gates", "desc": "Leading architectural spike pilots and automated CI/CD code regression quality gates."}
        ],
        "technologies": ["TOGAF 10", "Clean Core on SAP BTP", "Microservices & Kubernetes", "OData v4 & REST", "Apache Kafka"],
        "deliverables": [
            "Solution Architecture Document (SAD)",
            "System Integration Specification",
            "Disaster Recovery & High-Availability Architecture"
        ],
        "qa": {
            "q": "How do your architects ensure custom software remains maintainable over a 10-year horizon?",
            "a": "We enforce strict loose coupling, standard API contracts, in-line code documentation, automated unit test suites (>85% coverage), and architectural ADRs (Architecture Decision Records) stored directly in source control."
        },
        "sources": [
            {"title": "Sumeru Architectural Standards", "url": "https://sumerutechnologies.com/company/team", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

QUALITY_TOPICS = [
    {
        "id": "quality-credo",
        "slug": "quality-credo",
        "nav_label": "Quality Credo & Ruskin",
        "badge": "QUALITY • JOHN RUSKIN CREDO",
        "title": "Quality is Never an Accident: It is Always the Result of Intelligent Effort",
        "summary": "Our operational creed, inspired by Victorian thinker John Ruskin, governs every line of code, architectural blueprint, and SLA commitment we make.",
        "lead": "Our operational creed, inspired by Victorian thinker John Ruskin, governs every line of code, architectural blueprint, and SLA commitment we make.",
        "image": {
            "url": "/static/images/content/consulting_new2-580x400.jpg",
            "alt": "Quality Commitment",
            "caption": "Sumeru Quality Credo and Process Excellence"
        },
        "content": [
            {
                "heading": "The Ruskin Credo in Enterprise Software",
                "body": "According to great Victorian thinker John Ruskin, 'Quality is never an accident. It is always the result of intelligent effort.' Sumeru Technologies strongly believes in this credo. In enterprise computing, software defects, interface timeouts, or data corruption have catastrophic financial and operational consequences.\n\nWe are committed to creating and delivering high technology services that consistently exceed expectations and enhance the level of business agility for our clients."
            },
            {
                "heading": "Goal-Driven Quality Management",
                "body": "Our quality implementation efforts are pervasive across all delivery streams, beginning with our stated goal: 'Believing in 3i's – intelligence, innovation and integrity, Sumeru Technologies shall relentlessly strive to deliver software solutions and management consultancy services to the satisfaction of the customers with focus on continual improvement by implementing Quality Management System.'"
            }
        ],
        "methodology": [
            {"step": "OBJECTIVE 01", "name": "Customer Delight", "desc": "Exceeding expectations through rigorous quality gates and peer-reviewed code."},
            {"step": "OBJECTIVE 02", "name": "Zero-Defect Delivery", "desc": "Enforcing automated unit, regression, and load testing before production cutover."},
            {"step": "OBJECTIVE 03", "name": "Continual Improvement", "desc": "Refining our Solution Delivery tool sets using empirical project retrospectives."},
            {"step": "OBJECTIVE 04", "name": "Process Consistency", "desc": "Standardizing operating procedures across onshore and offshore delivery teams."}
        ],
        "technologies": ["SonarQube Quality Gates", "Selenium & Cypress Automation", "JMeter Load Testing", "ISO 9001 Alignment", "ITIL v4 Framework"],
        "deliverables": [
            "Corporate Quality Policy Statement",
            "Automated Regression Test Certification",
            "Security Vulnerability Audit Scorecard",
            "Binding Operational SLA Commitment"
        ],
        "qa": {
            "q": "What specific metrics does Sumeru use to measure delivery quality?",
            "a": "We track test coverage (>85%), defect density (<0.1 defects per KLOC), automated regression pass rates (100% before cutover), and strict adherence to binding SLA response and resolution times."
        },
        "sources": [
            {"title": "Sumeru Quality Policy", "url": "https://sumerutechnologies.com/company/quality", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

CAREERS_TOPICS = [
    {
        "id": "workplace-culture",
        "slug": "workplace-culture",
        "nav_label": "Workplace Culture",
        "badge": "CAREERS • ENTREPRENEURIAL CULTURE",
        "title": "An Entrepreneurial Workplace Fostering Technical Mastery",
        "summary": "Join a global software company where ideas are valued, individual growth is nurtured, and engineers work on mission-critical Fortune 500 platforms.",
        "lead": "Join a global software company where ideas are valued, individual growth is nurtured, and engineers work on mission-critical Fortune 500 platforms.",
        "image": {
            "url": "/static/images/content/sumeru_office_glass_hero.jpg",
            "alt": "Careers at Sumeru Technologies",
            "caption": "Professional Growth & Technical Mastery at Sumeru Technologies"
        },
        "content": [
            {
                "heading": "Career Building Philosophy",
                "body": "Sumeru Technologies is unique in its ability to attract and retain the highest caliber professionals in the business. Our entrepreneurial culture and commitment to business principles have fostered sustained organizational stability and ever-growing career opportunities across the USA, Europe, and India.\n\nWe view ourselves as career builders, helping employees expand their architectural skills, master current and emerging platforms (such as SAP S/4HANA, BTP, and cloud infrastructures), and take ownership of high-impact enterprise deliverables."
            },
            {
                "heading": "Global Exposure & Meritocracy",
                "body": "Team members collaborate daily across our Warrenville headquarters, Madrid office, and Hyderabad/Bangalore centers. We emphasize associate dignity, equality, and continuous professional development in an open, merit-driven environment."
            }
        ],
        "methodology": [
            {"step": "PILLAR 01", "name": "Hands-on Technical Depth", "desc": "Working directly with seasoned Principal Architects on live production enterprise systems."},
            {"step": "PILLAR 02", "name": "Global Exposure", "desc": "Collaborating with multinational Fortune 500 clients across regulated global sectors."},
            {"step": "PILLAR 03", "name": "Continuous Certification", "desc": "Full sponsorship for vendor certifications across SAP, Oracle, AWS, Azure, and PMP."},
            {"step": "PILLAR 04", "name": "Work-Life Integration", "desc": "Flexible work policies and competitive compensation packages tailored to employee growth."}
        ],
        "technologies": ["SAP S/4HANA", "Oracle Cloud", "Enterprise Java / Spring", ".NET Core", "DevOps & IaC", "DBA Systems"],
        "deliverables": [
            "Professional Development & Training Roadmap",
            "Vendor Certification Sponsorship Program",
            "Annual Technical Merit Review Process"
        ],
        "qa": {
            "q": "How can prospective candidates apply to Sumeru Technologies?",
            "a": "Candidates can submit their resume and portfolio directly to our talent acquisition team at HR@sumerutechnologies.com. Applications are reviewed directly by technical practice leads."
        },
        "sources": [
            {"title": "Sumeru Careers Portal", "url": "https://sumerutechnologies.com/careers", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    },
    {
        "id": "active-opening-teamcenter",
        "slug": "active-opening-teamcenter",
        "nav_label": "Team Center Test Lead",
        "badge": "ACTIVE OPENING • WARRENVILLE, IL",
        "title": "Team Center Test Lead (Warrenville, IL / U.S. Locations)",
        "summary": "Sumeru Technologies LLC has an opening for Team Center Test Lead in Warrenville, IL ($88,088/yr). Oversee regression testing automation, ADO traceability, and PLM implementation harmonization.",
        "lead": "Sumeru Technologies LLC has an opening for Team Center Test Lead in Warrenville, IL ($88,088/yr). Oversee regression testing automation, ADO traceability, and PLM implementation harmonization.",
        "image": {
            "url": "/static/images/content/about-us.jpg",
            "alt": "Team Center Test Lead Position",
            "caption": "Engineering Opportunities at Sumeru Technologies LLC"
        },
        "content": [
            {
                "heading": "Position Overview & Responsibilities",
                "body": "SUMERU TECHNOLOGIES LLC has an active opening in Warrenville, IL for a Team Center Test Lead:\n- Oversee the creation of a process for regression testing along with automation for each release.\n- Coordinate functional automation, performance testing, and upgrade testing.\n- Coordinate the mapping of requirements with test cases with bugs for traceability of scenarios using ADO (Azure DevOps).\n- As team lead, identify the Domain, Application, Capability, and Key functions to set up the foundation for the Quality Center of Excellence team.\n- Coordinate the preparation of the test case for the business process of PLM systems.\n- Oversee workshops and provide demonstrations of the process to business stakeholders alongside core-team members and business SMEs.\n- Collaborate with the PLM implementation team on activities related to PLM Implementations including Changes in the System, Job Requests, Variants setup, and Queries creation.\n- Perform final review and issue final approval of user documentation for business process standardization and coordinate the harmonization for PLM systems."
            },
            {
                "heading": "Requirements & Compensation",
                "body": "Will work in various unanticipated locations throughout the U.S. Requires Bachelor's in Computer Science, Engineering, or related and 2 years experience. Compensation: $88,088.00 per year. Standard benefits package offered to eligible employees including paid time off, paid holidays, and other benefits in accordance with company policy.\n\nTo apply, send resume to HR@sumerutechnologies.com referencing 'Team Center Test Lead'."
            }
        ],
        "methodology": [
            {"step": "STEP 01", "name": "Resume Submission", "desc": "Send CV to HR@sumerutechnologies.com with position title in subject line."},
            {"step": "STEP 02", "name": "Technical Screening", "desc": "Phone discussion with a Senior Architect evaluating PLM and automated testing experience."},
            {"step": "STEP 03", "name": "Panel Review", "desc": "In-depth review of ADO traceability, automation frameworks, and leadership scenario demonstration."},
            {"step": "STEP 04", "name": "Formal Offer & Onboarding", "desc": "Prompt offer dispatch and structured onboarding with our Warrenville engineering team."}
        ],
        "technologies": ["Siemens Teamcenter PLM", "Azure DevOps (ADO)", "Regression Automation", "Selenium", "Test Case Traceability", "PLM Systems Harmonization"],
        "deliverables": [
            "Quality Center of Excellence Foundation Charter",
            "ADO Requirements-to-Test Traceability Matrix",
            "PLM Automated Regression Suite",
            "Harmonized User Process Documentation"
        ],
        "qa": {
            "q": "What qualifications are required for the Team Center Test Lead position?",
            "a": "Requires a Bachelor's degree in Computer Science, Engineering, or related technical field and a minimum of 2 years of relevant experience in PLM test coordination, regression automation, and Azure DevOps scenario mapping."
        },
        "sources": [
            {"title": "Sumeru Technologies Official Hiring Notice (August 2026)", "url": "https://sumerutechnologies.com/careers", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ],
        "lastReviewedAt": "2026-10-26T08:00:00Z",
        "contentStatus": "reviewed"
    }
]

print("enrich_company_and_team.py defined.")
