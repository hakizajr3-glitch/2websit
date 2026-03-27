def run_deployer(build_result: dict, provider: str = "preview") -> str:
    app_name = build_result.get("app_name", "generated-saas-app").replace("_", "-")
    return f"https://{app_name}.{provider}.example.app"
