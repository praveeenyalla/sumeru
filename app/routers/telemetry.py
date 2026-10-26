from fastapi import APIRouter, HTTPException
from app.services.telemetry_service import telemetry_service
from app.models.domain import ClusterTelemetryResponse, NodeTelemetry

router = APIRouter(prefix="/telemetry", tags=["Synapse Telemetry"])

@router.get("/cluster", response_model=ClusterTelemetryResponse)
async def get_cluster_telemetry():
    """Retrieve realtime cluster telemetry and all nodes metrics."""
    return telemetry_service.get_cluster_telemetry()

@router.get("/nodes/{node_id}", response_model=NodeTelemetry)
async def get_node_telemetry(node_id: str):
    """Retrieve realtime state and performance telemetry for an individual node."""
    node = telemetry_service.get_single_node(node_id)
    if not node:
        raise HTTPException(status_code=404, detail=f"Node '{node_id}' not found in cluster.")
    return node
