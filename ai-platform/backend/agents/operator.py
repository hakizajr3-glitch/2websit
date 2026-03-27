def run_operator(change_instruction: str) -> dict:
    return {
        "change_instruction": change_instruction,
        "detected_category": "feature",
        "summary": "Applied change to spec and rebuilt preview.",
        "rollback_available": True,
    }
