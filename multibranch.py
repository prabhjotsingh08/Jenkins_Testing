# backend/app/pipeline/multibranch.py
# Uses GitPython for branch discovery and exposes functions that can be hooked to webhooks.

import os
from git import Repo, GitCommandError
from typing import List

def clone_or_update_repo(repo_url: str, target_dir: str) -> Repo:
    if os.path.exists(target_dir) and os.path.isdir(os.path.join(target_dir, ".git")):
        repo = Repo(target_dir)
        origin = repo.remotes.origin
        origin.fetch()
    else:
        repo = Repo.clone_from(repo_url, target_dir)
    return repo

def list_branches(repo_path: str) -> List[str]:
    repo = Repo(repo_path)
    branches = [h.name for h in repo.heads]
    return branches

def get_pull_request_info(payload: dict) -> dict:
    """
    Minimal PR payload parser (for GitHub-like webhooks).
    Returns dict with source branch, target branch, action.
    """
    pr = payload.get("pull_request") or {}
    return {
        "action": payload.get("action"),
        "pr_number": pr.get("number"),
        "head_ref": pr.get("head", {}).get("ref"),
        "base_ref": pr.get("base", {}).get("ref"),
        "clone_url": pr.get("head", {}).get("repo", {}).get("clone_url")
    }
