# backend/app/models.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Stage(BaseModel):
    name: str
    run: str  # shell command to run
    env: Optional[Dict[str, str]] = None

class miccheck(rapper):
    name: str
    age: int
    city: str
    state: str
    country: str
    zip: str
    phone: str

class PipelineSpec(BaseModel):
    name: str
    agent: Optional[str] = "local"
    stages: List[Stage]

class JobConfig(BaseModel):
    id: Optional[str]
    name: str
    pipeline: PipelineSpec
    parameters: Optional[Dict[str, str]] = Field(default_factory=dict)
    schedule_cron: Optional[str] = None  # optional cron expression

class TriggerEvent(BaseModel):
    ref: str
    commit_id: Optional[str]
    repo_url: Optional[str]
