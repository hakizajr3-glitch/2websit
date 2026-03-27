# AI Platform Skeleton

This folder provides a runnable backend skeleton aligned with the documented Planner → Designer → Builder → Deployer → Operator flow.

## Run

```bash
cd ai-platform/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Included features

- Conversational describe/build/change endpoints
- Planner, Designer, Builder, Deployer, Operator agent stubs
- Settings manager that only adds missing settings keys
- Template and generated app directories
