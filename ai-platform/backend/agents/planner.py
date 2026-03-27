def run_planner(user_input: dict) -> dict:
    """Stub planner: convert free text to structured spec."""
    idea = user_input.get("idea", "Generated SaaS")
    features = user_input.get("features", [])
    return {
        "app_name": "generated_saas_app",
        "idea": idea,
        "pages": ["login", "dashboard", "settings"],
        "features": features,
        "database_schema": {
            "users": ["id", "email", "password_hash"],
            "events": ["id", "user_id", "event_name", "created_at"],
        },
    }
