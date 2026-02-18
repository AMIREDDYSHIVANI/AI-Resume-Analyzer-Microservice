from fastapi import APIRouter, UploadFile, File, Form
from resume_analyzer.app.services.resume_service import (
    analyze_resume,
    optimize_resume
)
from io import BytesIO
import pdfplumber

router = APIRouter()

@router.post("/analyze-resume")
async def analyze(
    file: UploadFile = File(...),
    job_description: str = Form(None)
):
    return await analyze_resume(file, job_description)


@router.post("/optimize-resume")
async def optimize(file: UploadFile = File(...)):
    return await optimize_resume(file)

@router.post("/generate-cover-letter")
async def cover_letter(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    from resume_analyzer.app.services.resume_service import generate_cover_letter

    contents = await file.read()
    pdf_stream = BytesIO(contents)

    text = ""
    with pdfplumber.open(pdf_stream) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return await generate_cover_letter(text, job_description)
