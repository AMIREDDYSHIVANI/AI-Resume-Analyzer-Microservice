from fastapi import FastAPI
from resume_analyzer.app.routes.resume_routes import router as resume_router

app = FastAPI(title="AI Resume Analyzer Microservice")

app.include_router(resume_router)

@app.get("/")
def home():
    return {"message": "AI Resume Analyzer is running 🚀"}

@app.get("/test-route")
def test():
    return {"status": "working"}
