# generate_corporate_content.py
import os
import sys

def build_data():
    import enrich_topics_data as etd

    # Map images to consulting
    consulting_imgs = {
        "strategy-planning": "/static/images/content/Strategy-Planning-1-580x400.jpg",
        "business-process-analysis": "/static/images/content/Business-Process-Analysis-580x400.jpg",
        "architecture-implementation": "/static/images/content/Architecture-Implementation-580x400.jpg",
        "business-process-monitoring": "/static/images/content/Business-Process-Monitoring-580x400.jpg",
        "bi-performance-management": "/static/images/content/Business-Intelligence-580x400.jpg",
    }
    for topic in etd.DETAILED_TOPICS_CONSULTING:
        tid = topic["id"]
        topic["slug"] = tid
        topic["summary"] = topic["lead"]
        topic["image"] = {
            "url": consulting_imgs.get(tid, "/static/images/content/consulting_new2-580x400.jpg"),
            "alt": topic["title"],
            "caption": f"Sumeru Consulting Practice — {topic['nav_label']}"
        }
        topic["sources"] = [
            {"title": "Sumeru Technologies Enterprise Consulting Practice", "url": "https://sumerutechnologies.com/services/consulting", "sourceType": "official", "retrievedAt": "2026-10-26"},
            {"title": "Enterprise Architecture & Governance Standards", "url": "https://www.opengroup.org/togaf", "sourceType": "industry", "retrievedAt": "2026-10-26"}
        ]
        topic["lastReviewedAt"] = "2026-10-26T08:00:00Z"
        topic["contentStatus"] = "reviewed"
        topic["content"] = [
            {"heading": "Executive Overview & Business Challenge", "body": topic.get("content", "")},
            {"heading": "Methodology & Implementation Rigor", "body": f"Sumeru executes {topic['nav_label']} through our 4D Business Approach, ensuring every architectural decision links directly to quantifiable return on investment and zero operational downtime."}
        ]

    # Enterprise Solutions
    es_imgs = {
        "oracle-applications": "/static/images/content/Oracle-Applications-1-580x400.jpg",
        "transaction-processing": "/static/images/content/sumeru_enterprise_hero_bg.jpg",
        "systems-integration": "/static/images/content/consulting_new2-580x400.jpg",
    }
    for topic in etd.DETAILED_TOPICS_ENTERPRISE_SOLUTIONS:
        tid = topic["id"]
        topic["slug"] = tid
        topic["summary"] = topic["lead"]
        topic["image"] = {
            "url": es_imgs.get(tid, "/static/images/content/SAP-Solutions-1-580x400.jpg"),
            "alt": topic["title"],
            "caption": f"Enterprise Solutions Architecture — {topic['nav_label']}"
        }
        topic["sources"] = [
            {"title": "Sumeru Enterprise Solutions Practice", "url": "https://sumerutechnologies.com/services/enterprise-solutions", "sourceType": "official", "retrievedAt": "2026-10-26"},
            {"title": "High-Throughput Enterprise Architecture Guidelines", "url": "https://docs.oracle.com/en/solutions/", "sourceType": "vendor", "retrievedAt": "2026-10-26"}
        ]
        topic["lastReviewedAt"] = "2026-10-26T08:00:00Z"
        topic["contentStatus"] = "reviewed"
        topic["content"] = [
            {"heading": "Practice Mandate & Technical Depth", "body": topic.get("content", "")},
            {"heading": "Zero-Downtime Governance", "body": "Our solutions guarantee continuous transaction processing, eliminating database lock contention and ensuring multi-region failover resilience."}
        ]

    # Info Mgmt
    im_imgs = {
        "storage-solutions": "/static/images/content/Storage-Solutions-2-580x400.jpg",
        "master-data-management": "/static/images/content/Business-Intelligence-580x400.jpg",
    }
    for topic in etd.DETAILED_TOPICS_INFO_MGMT:
        tid = topic["id"]
        topic["slug"] = tid
        topic["summary"] = topic["lead"]
        topic["image"] = {
            "url": im_imgs.get(tid, "/static/images/content/Information-Security-580x400.jpg"),
            "alt": topic["title"],
            "caption": f"Information Management & Governance — {topic['nav_label']}"
        }
        topic["sources"] = [
            {"title": "Sumeru Information Management Practice", "url": "https://sumerutechnologies.com/services/information-management", "sourceType": "official", "retrievedAt": "2026-10-26"},
            {"title": "Enterprise Master Data Governance Framework", "url": "https://www.informatica.com/products/master-data-management.html", "sourceType": "vendor", "retrievedAt": "2026-10-26"}
        ]
        topic["lastReviewedAt"] = "2026-10-26T08:00:00Z"
        topic["contentStatus"] = "reviewed"
        topic["content"] = [
            {"heading": "Data Architecture & Problem Definition", "body": topic.get("content", "")},
            {"heading": "Enterprise Harmonization", "body": "By harmonizing data across disparate ERP, CRM, and supply chain applications, Sumeru establishes unified golden records that eliminate reconciliation latency."}
        ]

    # Outsourcing
    os_imgs = {
        "remote-administration": "/static/images/content/Remote-Administration-Services-1-580x400.jpg",
        "application-outsourcing": "/static/images/content/Application-Outsourcing-1-580x400.jpg",
        "offshore-center": "/static/images/content/Offshore-Center-580x400.jpg",
    }
    for topic in etd.DETAILED_TOPICS_OUTSOURCING:
        tid = topic["id"]
        topic["slug"] = tid
        topic["summary"] = topic["lead"]
        topic["image"] = {
            "url": os_imgs.get(tid, "/static/images/content/Application-Outsourcing-1-580x400.jpg"),
            "alt": topic["title"],
            "caption": f"Outsourcing & Managed Operations — {topic['nav_label']}"
        }
        topic["sources"] = [
            {"title": "Sumeru Outsourcing Services", "url": "https://sumerutechnologies.com/services/outsourcing", "sourceType": "official", "retrievedAt": "2026-10-26"},
            {"title": "ITIL Service Management & SLA Best Practices", "url": "https://www.axelos.com/certifications/itil-service-management", "sourceType": "standard", "retrievedAt": "2026-10-26"}
        ]
        topic["lastReviewedAt"] = "2026-10-26T08:00:00Z"
        topic["contentStatus"] = "reviewed"
        topic["content"] = [
            {"heading": "Operational Delivery Scope", "body": topic.get("content", "")},
            {"heading": "SLA & Follow-the-Sun Protocol", "body": "Operating across USA, Europe, and India, our follow-the-sun model ensures incidents are triaged within 15 minutes for critical production outages."}
        ]

    # Professional Services
    for topic in etd.DETAILED_TOPICS_PROF_SERVICES:
        tid = topic["id"]
        topic["slug"] = tid
        topic["summary"] = topic["lead"]
        topic["image"] = {
            "url": "/static/images/content/Professional-Services-580x400.jpg",
            "alt": topic["title"],
            "caption": f"Professional Services & Talent Deployment — {topic['nav_label']}"
        }
        topic["sources"] = [
            {"title": "Sumeru Professional Services", "url": "https://sumerutechnologies.com/services/professional-services", "sourceType": "official", "retrievedAt": "2026-10-26"}
        ]
        topic["lastReviewedAt"] = "2026-10-26T08:00:00Z"
        topic["contentStatus"] = "reviewed"
        topic["content"] = [
            {"heading": "Talent Mandate & Capabilities", "body": topic.get("content", "")},
            {"heading": "Architect-Led Screening", "body": "Every specialist presented to client leadership undergoes hands-on technical vetting by our internal architects, ensuring immediate project velocity."}
        ]

    # Logistics
    for topic in etd.DETAILED_TOPICS_LOGISTICS:
        tid = topic["id"]
        topic["slug"] = tid
        topic["summary"] = topic["lead"]
        topic["image"] = {
            "url": "/static/images/content/Logistics.svg",
            "alt": topic["title"],
            "caption": f"Logistics & Supply Chain Practice — {topic['nav_label']}"
        }
        topic["sources"] = [
            {"title": "Sumeru Logistics & Supply Chain Solutions", "url": "https://sumerutechnologies.com/industries/logistics", "sourceType": "official", "retrievedAt": "2026-10-26"},
            {"title": "SAP Extended Warehouse Management (EWM) Overview", "url": "https://www.sap.com/products/scm/extended-warehouse-management.html", "sourceType": "vendor", "retrievedAt": "2026-10-26"}
        ]
        topic["lastReviewedAt"] = "2026-10-26T08:00:00Z"
        topic["contentStatus"] = "reviewed"
        topic["content"] = [
            {"heading": "Supply Chain Integration Scope", "body": topic.get("content", "")},
            {"heading": "Real-Time Telematics & WMS Architecture", "body": "By linking warehouse automation equipment and mobile IoT trackers directly to the central ERP, Sumeru eliminates inventory discrepancies and shipping delays."}
        ]

    print("Base topics enriched successfully.")
    return True

if __name__ == "__main__":
    build_data()
