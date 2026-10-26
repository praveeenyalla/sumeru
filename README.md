# Sumeru Technologies LLC — Corporate Web Platform

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB.svg?style=flat&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-Proprietary-blue.svg)](#)

Enterprise web application and interactive capability showcase for **Sumeru Technologies LLC** (Warrenville, IL — Founded 1994), featuring 26 fully enriched corporate routes, deep research-backed content, and an interactive vertical rectangular card system.

---

## 🏛️ Platform Architecture

- **Backend**: [FastAPI](https://fastapi.tiangolo.com) with asynchronous endpoint handling, lifespan state management, structured CORS policies, and HTTP security headers (`nosniff`, `SAMEORIGIN`, `strict-origin-when-cross-origin`).
- **Templating Engine**: [Jinja2](https://jinja.palletsprojects.com/) with inheritance layouts ([`base.html`](templates/base.html), [`inner.html`](templates/inner.html), [`index.html`](templates/index.html)).
- **Database / ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) supporting SQLite (`sumeru_enterprise.db`) with client inquiry management and executive advisory queue models.
- **Frontend / Styling**: Vanilla CSS design tokens with responsive grid layouts, glassmorphism dropdown menus, and accessibility focus states.
- **Interactive Scripting**: Pure Vanilla JavaScript ([`sumeru.js`](app/static/js/sumeru.js)) featuring:
  - Sticky header transitions on scroll.
  - Mobile slide-out drawer with accordion navigation.
  - Interactive 4D Business Approach lifecycle switcher.
  - **Interactive Vertical Rectangular Card System (Section 8)**: Deep-linked expandable floating rectangular cards with smooth backdrop blur, keyboard navigation (`Enter`, `Escape`), methodology steps, technology pills, deliverable checklists, exact Q&A governance, and verified source citations.

---

## 📂 Repository Structure

```text
sumeru/
├── app/
│   ├── config.py                 # Environment-aware application configuration
│   ├── database.py               # SQLAlchemy database session & engine management
│   ├── main.py                   # FastAPI app declaration, lifespan, & security middleware
│   ├── models/
│   │   ├── db_models.py          # SQLAlchemy ORM models (ContactInquiry, AdvisoryRequest)
│   │   └── domain.py             # Pydantic schemas, validation models, and DTOs
│   ├── routers/
│   │   ├── web_pages.py          # Jinja2 corporate web routes (About, Services, Industries, etc.)
│   │   ├── contact.py            # Sanitized contact inquiry dispatch API
│   │   ├── advisory.py           # Strategic advisory consultation dispatch
│   │   ├── portal.py             # Authenticated client portal dashboard
│   │   ├── sap_clean_core.py     # SAP Clean Core assessment & tiering API
│   │   ├── solutions.py          # Architecture suite whitepapers
│   │   └── telemetry.py          # Cluster and node performance telemetry
│   ├── services/
│   │   ├── corporate_content.py  # 26 verified corporate routes & deep topic datasets
│   │   ├── advisory_service.py   # SLA dispatch & SHA-256 tamper verification
│   │   ├── clean_core_service.py # Clean Core 5-tier evaluation logic
│   │   ├── pipeline_service.py   # 7-stage sovereign reasoning pipeline engine
│   │   ├── solutions_service.py  # Enterprise solutions repository
│   │   └── telemetry_service.py  # Node heartbeat & performance metrics
│   └── static/
│       ├── css/                  # sumeru.css & custom.css
│       ├── js/                   # sumeru.js client interactive logic
│       └── images/               # Content imagery, logos, SVG diagrams
├── templates/
│   ├── base.html                 # Master layout with mega-menus & footer
│   ├── index.html                # Enterprise homepage
│   └── inner.html                # Enriched capability page & floating card modal
├── scripts/                      # Compilation and route validation utilities
├── requirements.txt              # Production Python dependencies
├── run.py                        # Local development runner
└── .gitignore                    # Enterprise git exclusions
```

---

## 🚀 Quickstart

### 1. Prerequisites
- Python 3.10+ (Recommended Python 3.11 or 3.12)
- Git

### 2. Environment Setup
```bash
# Clone the repository
git clone https://github.com/praveeenyalla/sumeru.git
cd sumeru

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Development Server
```bash
python run.py
```
Open **http://127.0.0.1:8000** in your browser.
API documentation is available at **http://127.0.0.1:8000/docs**.

---

## 🔒 Security & Quality Standards

- **Strict Input Validation**: All user-submitted payloads (e.g. contact forms, advisory dispatches) are validated using Pydantic bounded models and escaped against Cross-Site Scripting (XSS).
- **Security Headers**: Automatic injection of `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`.
- **Clean Core & Enterprise Practices**: Distinguishes verified corporate capabilities from general vendor offerings.
- **Zero Hallucination Attribution**: All operational and industry insights provide verified external references with ISO retrieval timestamps.

---

## 📄 License
© 1994–2026 Sumeru Technologies LLC. All rights reserved.
