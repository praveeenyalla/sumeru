from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.services.solutions_service import solutions_service
from app.models.domain import SolutionSpecification

router = APIRouter(prefix="/solutions", tags=["Architectural Suites"])

@router.get("", response_model=List[SolutionSpecification])
async def list_solutions(category: Optional[str] = Query(None, description="Filter category: 'all', 'ai-data', 'sap', 'infra-sec'")):
    """List architectural suites optionally filtered by domain category."""
    return solutions_service.list_solutions(category)

@router.get("/{solution_id}", response_model=SolutionSpecification)
async def get_solution_specification(solution_id: str):
    """Retrieve full engineering whitepaper, compliance frameworks, and SLAs for a solution."""
    sol = solutions_service.get_solution(solution_id)
    if not sol:
        raise HTTPException(status_code=404, detail="Solution specification not found")
    return sol
