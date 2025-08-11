# backend/app/maven_runner.py
# Executes Maven builds and parses pom.xml dependencies (simple).

import subprocess
import xml.etree.ElementTree as ET
import os
from typing import List, Dict

def run_maven_build(repo_path: str, mvn_args: List[str] = None) -> Dict:
    args = ["mvn"]
    if mvn_args:
        args.extend(mvn_args)
    proc = subprocess.run(args, cwd=repo_path, capture_output=True, text=True)
    return {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}

def parse_dependencies_from_pom(pom_path: str) -> List[Dict]:
    if not os.path.exists(pom_path):
        return []
    tree = ET.parse(pom_path)
    root = tree.getroot()
    ns = {'m': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}
    deps = []
    for dep in root.findall('.//{*}dependency'):
        group = dep.find('{*}groupId').text if dep.find('{*}groupId') is not None else None
        artifact = dep.find('{*}artifactId').text if dep.find('{*}artifactId') is not None else None
        version = dep.find('{*}version').text if dep.find('{*}version') is not None else None
        deps.append({"group": group, "artifact": artifact, "version": version})
    return deps
