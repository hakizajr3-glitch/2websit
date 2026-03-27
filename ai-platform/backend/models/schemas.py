from typing import Any

from pydantic import BaseModel, Field


class DescribeRequest(BaseModel):
    idea: str = Field(..., min_length=3)
    features: list[str] = Field(default_factory=list)


class BuildRequest(BaseModel):
    idea: str = Field(..., min_length=3)
    features: list[str] = Field(default_factory=list)
    provider: str = "preview"


class ChangeRequest(BaseModel):
    instruction: str = Field(..., min_length=3)


class PipelineResponse(BaseModel):
    spec: dict[str, Any]
    design: dict[str, Any]
    build_status: str
    deploy_url: str | None = None
    notes: list[str] = Field(default_factory=list)
