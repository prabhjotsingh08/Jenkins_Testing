# backend/app/main.py
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from .config import settings
from .pipeline.dsl_parser import parse_pipeline_yaml, DSLParseError
from .models import JobConfig, PipelineSpec, TriggerEvent
from .job_manager import create_job, list_jobs, trigger_job, get_job
from .queue import queue_status, start_worker
from .vcs import ensure_repo
from .pipeline.multibranch import get_pull_request_info
import os

app = FastAPI(title=settings.APP_NAME)

@app.on_event("startup")
def startup():
    os.makedirs(settings.REPO_BASE_PATH, exist_ok=True)
    start_worker()

@app.post("/pipelines/parse")
async def parse_pipeline(yaml_text: str):
    try:
        pipeline = parse_pipeline_yaml(yaml_text)
        return {"ok": True, "pipeline": pipeline.dict()}
    except DSLParseError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/jobs")
async def create_job_endpoint(cfg: JobConfig):
    job = create_job(cfg)
    return {"ok": True, "job": job}

@app.get("/jobs")
async def list_jobs_endpoint():
    return {"jobs": [j.dict() for j in list_jobs()]}

@app.post("/jobs/{job_id}/trigger")
async def trigger_job_endpoint(job_id: str, params: dict = {}):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    trigger_job(job_id, params)
    return {"ok": True}

@app.get("/queue")
async def queue_status_endpoint():
    return queue_status()

@app.post("/webhook")
async def webhook_listener(request: Request):
    data = await request.json()
    # naive auth
    token = request.headers.get("X-Webhook-Token")
    if token != settings.SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    # parse PR info
    pr_info = get_pull_request_info(data)
    # enqueue a PR-based job — for demo we simply print
    return {"ok": True, "pr": pr_info}
