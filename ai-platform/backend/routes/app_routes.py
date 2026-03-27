from fastapi import APIRouter

from models.schemas import BuildRequest, ChangeRequest, DescribeRequest, PipelineResponse
from services.orchestrator import apply_change, describe_pipeline, run_full_pipeline

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/{project_id}/describe")
def describe_project(project_id: str, request: DescribeRequest):
    return {"project_id": project_id, **describe_pipeline(request.model_dump())}


@router.post("/{project_id}/build", response_model=PipelineResponse)
def build_project(project_id: str, request: BuildRequest):
    return run_full_pipeline(request.model_dump(), provider=request.provider)


@router.post("/{project_id}/changes")
def change_project(project_id: str, request: ChangeRequest):
    return {"project_id": project_id, **apply_change(request.instruction)}
