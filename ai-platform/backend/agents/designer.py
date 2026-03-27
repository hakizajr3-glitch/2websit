def run_designer(spec: dict) -> dict:
    """Stub designer: generate a luxury-style design system."""
    return {
        "color_palette": ["#0B0F19", "#2B6CF6", "#E8ECF8", "#FFFFFF"],
        "typography": "Inter",
        "layout_style": "SaaS-premium",
        "component_style": "shadcn-modern",
        "inspiration": ["Stripe", "Linear", "Notion"],
        "app_name": spec.get("app_name", "generated_saas_app"),
    }
