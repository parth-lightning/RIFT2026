"""
PharmaGuard — FastAPI application entrypoint.

Run with:
    uvicorn src.main:app --reload --port 8000

Routes
──────
POST /api/analyze   → VCF upload + drug list → PharmaGuardResult[]
GET  /api/health    → liveness probe
GET  /               → serves frontend/index.html
"""

from __future__ import annotations

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.api.routes.analyze import router as analyze_router
from src.core.config import get_settings

# ── Logging ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("pharmaguard")

# ── Settings ─────────────────────────────────────────────────────────────
settings = get_settings()

# ── App ──────────────────────────────────────────────────────────────────
app = FastAPI(
    title=settings.app_name,
    description="Pharmacogenomic Risk Prediction System",
    version=settings.app_version,
)

# ── CORS ─────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ──────────────────────────────────────────────────────────────
app.include_router(analyze_router)

# ── Health check ─────────────────────────────────────────────────────────

@app.get("/api/health", tags=["infra"])
async def health():
    """Liveness probe + configuration summary."""
    return {
        "status": "ok",
        "gemini_configured": bool(settings.gemini_api_key),
        "supported_drugs": settings.supported_drugs,
        "supported_genes": settings.supported_genes,
    }


# ── Serve frontend ──────────────────────────────────────────────────────
# NOTE: Frontend is served by Vercel, backend serves API only
# Removed frontend serving to prevent crashes on Railway
