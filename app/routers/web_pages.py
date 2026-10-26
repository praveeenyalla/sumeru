"""
Sumeru Technologies — Corporate Web Pages Router
Serves all verified static and corporate routes using Jinja2 templates.
"""

from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
import os
import datetime

from app.services.corporate_content import PAGES_DATA, CORPORATE_METADATA

router = APIRouter(include_in_schema=False)

templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
templates = Jinja2Templates(directory=templates_dir)

def render_page(request: Request, path_key: str):
    """Helper to render corporate pages with metadata."""
    page_data = PAGES_DATA.get(path_key, {})
    return templates.TemplateResponse(
        request=request,
        name="inner.html",
        context={
            "page_data": page_data,
            "current_year": datetime.date.today().year,
            "corporate_meta": CORPORATE_METADATA
        }
    )

@router.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    """Serve the primary Sumeru Technologies enterprise homepage."""
    page_data = PAGES_DATA.get("/", {})
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "page_data": page_data,
            "current_year": datetime.date.today().year,
            "corporate_meta": CORPORATE_METADATA
        }
    )

# ---------------- ABOUT & COMPANY ----------------
@router.get("/about", response_class=HTMLResponse)
async def serve_about(request: Request):
    return render_page(request, "/about")

@router.get("/company", response_class=HTMLResponse)
async def serve_company(request: Request):
    return render_page(request, "/company")

@router.get("/company/team", response_class=HTMLResponse)
async def serve_company_team(request: Request):
    return render_page(request, "/company/team")

@router.get("/company/partners", response_class=HTMLResponse)
async def serve_company_partners(request: Request):
    return render_page(request, "/company/partners")

@router.get("/company/quality", response_class=HTMLResponse)
async def serve_company_quality(request: Request):
    return render_page(request, "/company/quality")

@router.get("/company/about", response_class=HTMLResponse)
async def serve_company_about(request: Request):
    return render_page(request, "/company")

@router.get("/company/leadership", response_class=HTMLResponse)
async def serve_company_leadership(request: Request):
    return render_page(request, "/company/team")

@router.get("/company/approach", response_class=HTMLResponse)
async def serve_company_approach(request: Request):
    return render_page(request, "/about")

@router.get("/company/careers", response_class=HTMLResponse)
async def serve_company_careers(request: Request):
    return render_page(request, "/careers")

@router.get("/company/offices", response_class=HTMLResponse)
async def serve_company_offices(request: Request):
    return render_page(request, "/contact")

# ---------------- SERVICES ----------------
@router.get("/services", response_class=HTMLResponse)
async def serve_services(request: Request):
    return render_page(request, "/services")

@router.get("/services/consulting", response_class=HTMLResponse)
async def serve_services_consulting(request: Request):
    return render_page(request, "/services/consulting")

@router.get("/services/enterprise-solutions", response_class=HTMLResponse)
async def serve_services_enterprise(request: Request):
    return render_page(request, "/services/enterprise-solutions")

@router.get("/services/information-management", response_class=HTMLResponse)
async def serve_services_info_mgmt(request: Request):
    return render_page(request, "/services/information-management")

@router.get("/services/outsourcing", response_class=HTMLResponse)
async def serve_services_outsourcing(request: Request):
    return render_page(request, "/services/outsourcing")

@router.get("/services/professional-services", response_class=HTMLResponse)
async def serve_services_prof_services(request: Request):
    return render_page(request, "/services/professional-services")

# ---------------- SOLUTIONS ----------------
@router.get("/solutions", response_class=HTMLResponse)
async def serve_solutions(request: Request):
    return render_page(request, "/solutions")

@router.get("/solutions/sap", response_class=HTMLResponse)
async def serve_solutions_sap(request: Request):
    return render_page(request, "/solutions/sap")

@router.get("/solutions/business-intelligence", response_class=HTMLResponse)
async def serve_solutions_bi(request: Request):
    return render_page(request, "/solutions/business-intelligence")

@router.get("/solutions/information-security", response_class=HTMLResponse)
async def serve_solutions_info_sec(request: Request):
    return render_page(request, "/solutions/information-security")

@router.get("/solutions/data-governance", response_class=HTMLResponse)
async def serve_solutions_data_governance(request: Request):
    return render_page(request, "/solutions/business-intelligence")

@router.get("/solutions/specialized-suites", response_class=HTMLResponse)
async def serve_solutions_specialized(request: Request):
    return render_page(request, "/solutions/sap")

# ---------------- INDUSTRIES ----------------
@router.get("/industries", response_class=HTMLResponse)
async def serve_industries(request: Request):
    return render_page(request, "/industries")

@router.get("/industries/healthcare", response_class=HTMLResponse)
async def serve_industries_healthcare(request: Request):
    return render_page(request, "/industries/healthcare")

@router.get("/industries/oil-gas", response_class=HTMLResponse)
async def serve_industries_oil_gas(request: Request):
    return render_page(request, "/industries/oil-gas")

@router.get("/industries/manufacturing", response_class=HTMLResponse)
async def serve_industries_manufacturing(request: Request):
    return render_page(request, "/industries/manufacturing")

@router.get("/industries/education", response_class=HTMLResponse)
async def serve_industries_education(request: Request):
    return render_page(request, "/industries/education")

@router.get("/industries/textile-apparel", response_class=HTMLResponse)
async def serve_industries_textile(request: Request):
    return render_page(request, "/industries/textile-apparel")

@router.get("/industries/logistics", response_class=HTMLResponse)
async def serve_industries_logistics(request: Request):
    return render_page(request, "/industries/logistics")

# ---------------- RESOURCES, CAREERS, CONTACT ----------------
@router.get("/resources", response_class=HTMLResponse)
async def serve_resources(request: Request):
    return render_page(request, "/resources")

@router.get("/resources/insights", response_class=HTMLResponse)
async def serve_resources_insights(request: Request):
    return render_page(request, "/resources")

@router.get("/resources/perspectives", response_class=HTMLResponse)
async def serve_resources_perspectives(request: Request):
    return render_page(request, "/resources")

@router.get("/resources/faqs", response_class=HTMLResponse)
async def serve_resources_faqs(request: Request):
    return render_page(request, "/resources")

@router.get("/resources/downloads", response_class=HTMLResponse)
async def serve_resources_downloads(request: Request):
    return render_page(request, "/resources")

@router.get("/careers", response_class=HTMLResponse)
async def serve_careers(request: Request):
    return render_page(request, "/careers")

@router.get("/contact", response_class=HTMLResponse)
async def serve_contact(request: Request):
    return render_page(request, "/contact")

# ---------------- SEO: SITEMAP & ROBOTS ----------------
@router.get("/robots.txt", response_class=PlainTextResponse)
async def serve_robots():
    return """User-agent: *
Allow: /
Sitemap: https://sumerutechnologies.com/sitemap.xml
"""

@router.get("/sitemap.xml")
async def serve_sitemap():
    urls = [
        "https://sumerutechnologies.com/",
        "https://sumerutechnologies.com/about",
        "https://sumerutechnologies.com/services",
        "https://sumerutechnologies.com/services/consulting",
        "https://sumerutechnologies.com/services/enterprise-solutions",
        "https://sumerutechnologies.com/services/information-management",
        "https://sumerutechnologies.com/services/outsourcing",
        "https://sumerutechnologies.com/services/professional-services",
        "https://sumerutechnologies.com/solutions",
        "https://sumerutechnologies.com/solutions/sap",
        "https://sumerutechnologies.com/solutions/business-intelligence",
        "https://sumerutechnologies.com/solutions/information-security",
        "https://sumerutechnologies.com/industries",
        "https://sumerutechnologies.com/industries/healthcare",
        "https://sumerutechnologies.com/industries/oil-gas",
        "https://sumerutechnologies.com/industries/manufacturing",
        "https://sumerutechnologies.com/industries/education",
        "https://sumerutechnologies.com/industries/textile-apparel",
        "https://sumerutechnologies.com/industries/logistics",
        "https://sumerutechnologies.com/resources",
        "https://sumerutechnologies.com/company",
        "https://sumerutechnologies.com/company/team",
        "https://sumerutechnologies.com/company/partners",
        "https://sumerutechnologies.com/company/quality",
        "https://sumerutechnologies.com/careers",
        "https://sumerutechnologies.com/contact"
    ]
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        xml_content.append(f'  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    xml_content.append('</urlset>')
    return Response(content="\n".join(xml_content), media_type="application/xml")
