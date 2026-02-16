from fastapi import APIRouter, UploadFile, File
from resume_analyzer.app.services.resume_service import analyze_resume

router = APIRouter()

@router.post("/analyze-resume")
async def analyze(file: UploadFile = File(...)):
    result = await analyze_resume(file)
    return result
