# backend/app/test_processor.py
import xml.etree.ElementTree as ET
from typing import Dict, Any, List
import os

def parse_junit_reports(report_dir: str) -> Dict[str, Any]:
    results = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0, "cases": []}
    if not os.path.isdir(report_dir):
        return results
    for fname in os.listdir(report_dir):
        if not fname.endswith(".xml"):
            continue
        path = os.path.join(report_dir, fname)
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            # junit xml may have testsuites root or testsuite root
            suites = [root] if root.tag.endswith("testsuite") else root.findall(".//{*}testsuite")
            for s in suites:
                t = int(s.attrib.get("tests", 0))
                f = int(s.attrib.get("failures", 0))
                e = int(s.attrib.get("errors", 0))
                sk = int(s.attrib.get("skipped", 0))
                results["tests"] += t
                results["failures"] += f
                results["errors"] += e
                results["skipped"] += sk
            # extract individual cases
            for case in root.findall(".//{*}testcase"):
                results["cases"].append({
                    "name": case.attrib.get("name"),
                    "classname": case.attrib.get("classname"),
                    "time": case.attrib.get("time"),
                    "failure": case.find("{*}failure") is not None
                })
        except Exception:
            continue
    return results
