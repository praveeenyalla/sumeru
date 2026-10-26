from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from app.config import settings
from app.database import init_db
from app.routers import (
    contact,
    web_pages,
    telemetry,
    pipeline,
    solutions,
    sap_clean_core,
    global_ops,
    advisory,
    portal
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize Database
    init_db()
    yield
    # Shutdown logic if any

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTP Security Headers Middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    return response

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))

if not os.path.exists(static_dir):
    os.makedirs(static_dir, exist_ok=True)

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

# Register Web Pages Router (HTML routes for all corporate pages, sitemap, robots)
app.include_router(web_pages.router)

# Register API Routers
app.include_router(contact.router, prefix=settings.API_PREFIX)
app.include_router(telemetry.router, prefix=settings.API_PREFIX)
app.include_router(pipeline.router, prefix=settings.API_PREFIX)
app.include_router(solutions.router, prefix=settings.API_PREFIX)
app.include_router(sap_clean_core.router, prefix=settings.API_PREFIX)
app.include_router(global_ops.router, prefix=settings.API_PREFIX)
app.include_router(advisory.router, prefix=settings.API_PREFIX)
app.include_router(portal.router, prefix=settings.API_PREFIX)

from fastapi.responses import FileResponse

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    icon_path = os.path.join(static_dir, "images", "sumeru", "SUMERU_New-mobile.png")
    if os.path.exists(icon_path):
        return FileResponse(icon_path)
    return {"status": "none"}

@app.get("/healthz")
async def health_check():
    """Health check probe."""
    return {"status": "HEALTHY", "company": "Sumeru Technologies LLC", "version": settings.APP_VERSION}
