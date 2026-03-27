from fastapi import FastAPI

from routes.app_routes import router

app = FastAPI(title="AI SaaS Builder + Operator")
app.include_router(router)


@app.get("/")
def root():
    return {"status": "AI Platform Running"}
