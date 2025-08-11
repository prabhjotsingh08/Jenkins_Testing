# backend/app/vcs.py
# This file wires clone/discovery and a webhook endpoint (see main.py later).

import os
from .pipeline.multibranch import clone_or_update_repo, list_branches, get_pull_request_info
from ..config import settings
from typing import Optional

REPO_BASE = settings.REPO_BASE_PATH

def ensure_repo(repo_url: str, repo_name: str) -> str:
    target_dir = os.path.join(REPO_BASE, repo_name)
    os.makedirs(REPO_BASE, exist_ok=True)
    clone_or_update_repo(repo_url, target_dir)
    return target_dir
