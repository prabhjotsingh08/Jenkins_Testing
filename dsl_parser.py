#A small DSL: we accept YAML pipeline descriptions (simple, declarative). This parser validates and converts into PipelineSpec.
# backend/app/pipeline/dsl_parser.py
import yaml
from ..models import PipelineSpec, Stage
from typing import Any, Dict, List

class DSLParseError(Exception):
    pass

def parse_pipeline_yaml(yaml_text: str) -> PipelineSpec:
    """
    Parse a declarative pipeline YAML into PipelineSpec.
    Expected format:
    name: my-pipeline
    agent: local
    stages:
      - name: build
        run: mvn -B -DskipTests package
      - name: test
        run: mvn test
    """
    try:
        raw = yaml.safe_load(yaml_text)
    except Exception as e:
        raise DSLParseError(f"YAML parse failed: {e}")
    if not raw or "stages" not in raw or "name" not in raw:
        raise DSLParseError("Pipeline YAML must contain 'name' and 'stages' fields.")
    stages_raw: List[Dict[str, Any]] = raw.get("stages", [])
    stages: List[Stage] = []
    for s in stages_raw:
        if "name" not in s or "run" not in s:
            raise DSLParseError("Each stage must have 'name' and 'run'.")
        stages.append(Stage(name=s["name"], run=s["run"], env=s.get("env")))
    pipeline = PipelineSpec(name=raw["name"], agent=raw.get("agent", "local"), stages=stages)
    return pipeline
