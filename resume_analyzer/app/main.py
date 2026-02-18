from fastapi import FastAPI
from resume_analyzer.app.routes.resume_routes import router as resume_router

app = FastAPI(title="AI Resume Analyzer")

app.include_router(resume_router)

@app.get("/")
def home():
    return {"message": "AI Resume Analyzer Running 🚀"}

