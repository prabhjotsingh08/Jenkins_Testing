# backend/app/pipeline/engine.py
# Executes stages sequentially; returns structured result. Uses subprocess but with timeout and environment control.
import subprocess
import shlex
import asyncio
from typing import Dict, Any, List
from .dsl_parser import DSLParseError
from ..models import PipelineSpec, Stage
import time

class StageResult(dict):
    pass

async def run_stage(stage: Stage, workdir: str, params: Dict[str, str] = None, timeout: int = 600) -> StageResult:
    env = {}
    if stage.env:
        env.update(stage.env)
    if params:
        env.update(params)
    cmd = stage.run
    # Use shell=True for convenience; in production prefer shlex splitting with proper args.
    start = time.time()
    proc = await asyncio.create_subprocess_shell(cmd,
                                                 cwd=workdir,
                                                 stdout=asyncio.subprocess.PIPE,
                                                 stderr=asyncio.subprocess.STDOUT,
                                                 env={**env},
                                                 )
    try:
        stdout, _ = await asyncio.wait_for(proc.communicate(), timeout=timeout)
    except asyncio.TimeoutError:
        proc.kill()
        return StageResult(name=stage.name, status="TIMED_OUT", duration=time.time()-start, output="(timeout)")
    rc = proc.returncode
    status = "SUCCESS" if rc == 0 else "FAILED"
    text = stdout.decode(errors="ignore") if stdout else ""
    return StageResult(name=stage.name, status=status, duration=time.time()-start, output=text, rc=rc)

async def run_pipeline(pipeline: PipelineSpec, repo_path: str, params: Dict[str,str]=None) -> Dict[str, Any]:
    results: List[Dict[str,Any]] = []
    overall = "SUCCESS"
    for stage in pipeline.stages:
        r = await run_stage(stage, repo_path, params=params)
        results.append(r)
        if r.get("status") != "SUCCESS":
            overall = "FAILED"
            break
    return {"pipeline": pipeline.name, "status": overall, "stages": results}
