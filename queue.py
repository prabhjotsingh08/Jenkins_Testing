# backend/app/queue.py
# In-memory queue + simple worker thread. Queue processing engine picks jobs, executes pipeline using engine.
import threading
import time
import asyncio
from typing import Dict, Any
from .job_manager import get_job
from .pipeline.engine import run_pipeline
from .vcs import ensure_repo
from .notifications import notify_build_result

_queue = []
_lock = threading.Lock()
_stop = False
_worker_thread = None

def enqueue_job(job_id: str, params: Dict[str,str]):
    with _lock:
        _queue.append({"job_id": job_id, "params": params, "enqueued_at": time.time()})

def queue_status():
    with _lock:
        return {"length": len(_queue), "items": list(_queue)}

def _process_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while not _stop:
        item = None
        with _lock:
            if _queue:
                item = _queue.pop(0)
        if item:
            try:
                job = get_job(item["job_id"])
                if not job:
                    continue
                # for demo, ensure repo path points to job name under base path
                repo_path = ensure_repo("https://example.com/some/repo.git", job.name)  # placeholder
                coro = run_pipeline(job.pipeline, repo_path, params=item.get("params"))
                res = loop.run_until_complete(coro)
                # notify
                notify_build_result(job, res)
            except Exception as e:
                print("Queue processing error:", e)
        else:
            time.sleep(1)

def start_worker():
    global _worker_thread
    if _worker_thread and _worker_thread.is_alive():
        return
    _worker_thread = threading.Thread(target=_process_loop, daemon=True)
    _worker_thread.start()

def stop_worker():
    global _stop
    _stop = True
