from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.services.pipeline_service import pipeline_service
from app.models.domain import PipelineStage, PipelineSimulateRequest, PipelineSimulateResponse

router = APIRouter(prefix="/pipeline", tags=["Sovereign Reasoning Pipeline"])

@router.get("/stages", response_model=List[PipelineStage])
async def get_all_stages():
    """Returns the comprehensive 7-stage sovereign reasoning pipeline architecture."""
    return pipeline_service.list_stages()

@router.get("/stages/{stage_num}")
async def get_stage_by_number(stage_num: int):
    """Retrieve detailed specification, telemetry parameters, and capabilities for a specific pipeline stage."""
    if stage_num < 1 or stage_num > 7:
        raise HTTPException(status_code=404, detail="Pipeline stage must be between 1 and 7")
    return pipeline_service.get_stage(stage_num)

@router.post("/simulate", response_model=PipelineSimulateResponse)
async def simulate_pipeline_run(payload: PipelineSimulateRequest):
    """Execute an interactive air-gapped sovereign reasoning simulation across all 7 stages."""
    return pipeline_service.simulate_pipeline(payload)
