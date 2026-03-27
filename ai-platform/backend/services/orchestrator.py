from agents.builder import run_builder
from agents.deployer import run_deployer
from agents.designer import run_designer
from agents.operator import run_operator
from agents.planner import run_planner


def describe_pipeline(user_input: dict) -> dict:
    spec = run_planner(user_input)
    design = run_designer(spec)
    return {"spec": spec, "design": design}


def run_full_pipeline(user_input: dict, provider: str = "preview") -> dict:
    spec = run_planner(user_input)
    design = run_designer(spec)
    build_result = run_builder(spec, design)
    deploy_url = run_deployer(build_result, provider)

    return {
        "spec": spec,
        "design": design,
        "build_status": build_result.get("status", "completed"),
        "deploy_url": deploy_url,
        "notes": [
            "Preview branch recommended before production promotion.",
            "Human approval required for major updates.",
        ],
    }


def apply_change(instruction: str) -> dict:
    return run_operator(instruction)
