# backend/app/job_manager.py
# Supports job creation, parameterized jobs, schedule (cron via APScheduler), and storing jobs in-memory (for demo). Real system would persist.
import uuid
from typing import Dict, Optional, List
from .models import JobConfig, PipelineSpec
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .queue import enqueue_job
import threading

_jobs: Dict[str, JobConfig] = {}
_scheduler = BackgroundScheduler()
_scheduler.start()

def create_job(config: JobConfig) -> JobConfig:
    if not config.id:
        config.id = str(uuid.uuid4())
    _jobs[config.id] = config
    if config.schedule_cron:
        # schedule it
        trigger = CronTrigger.from_crontab(config.schedule_cron)
        _scheduler.add_job(lambda job_id=config.id: enqueue_job(job_id, {}), id=config.id, trigger=trigger)
    return config

def get_job(job_id: str) -> Optional[JobConfig]:
    return _jobs.get(job_id)

def list_jobs() -> List[JobConfig]:
    return list(_jobs.values())

def trigger_job(job_id: str, params: Dict[str,str] = None):
    """Trigger immediate enqueue"""
    enqueue_job(job_id, params or {})
