import os
import json
import re
from dotenv import load_dotenv
from pathlib import Path
import pdfplumber
from io import BytesIO
import requests

# -------------------------------------------------
# FORCE LOAD .env FROM PROJECT ROOT
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[3]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")



# ---------------------------------------------------
# ANALYZE RESUME (ATS + JD MATCHING)
# ---------------------------------------------------
async def analyze_resume(file, job_description=None):

    contents = await file.read()
    pdf_stream = BytesIO(contents)

    text = ""
    with pdfplumber.open(pdf_stream) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    if job_description:

        prompt = f"""
        Compare the resume and job description below.

        Respond ONLY in this JSON format:

        {{
          "match_score": number (0-100),
          "matched_skills": "...",
          "missing_skills": "...",
          "improvement_suggestions": "..."
        }}

        Resume:
        {text}

        Job Description:
        {job_description}
        """

    else:
        prompt = f"""
        Analyze this resume and respond ONLY in this JSON format:

        {{
          "score": number (0-100),
          "strengths": "...",
          "missing_skills": "...",
          "improvements": "...",
          "overall_summary": "..."
        }}

        Resume:
        {text}
        """

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "AI Resume Analyzer",
        "Content-Type": "application/json"
    },
    json={
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are an expert technical recruiter and ATS specialist."},
            {"role": "user", "content": prompt}
        ]
    }
)


    if response.status_code != 200:
        return {
            "error": "AI service failed",
            "details": response.text
        }

    data = response.json()

    if "choices" in data:
        content = data["choices"][0]["message"]["content"]

        # Remove markdown formatting
        content_clean = re.sub(r"```json|```", "", content).strip()

        try:
            return json.loads(content_clean)
        except:
            return {"analysis": content}

    return data


# ---------------------------------------------------
# OPTIMIZE RESUME (NEW FEATURE)
# ---------------------------------------------------
async def optimize_resume(file):

    contents = await file.read()
    pdf_stream = BytesIO(contents)

    text = ""
    with pdfplumber.open(pdf_stream) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    prompt = f"""
    Rewrite this resume to:

    - Improve ATS compatibility
    - Use strong action verbs
    - Improve bullet structure
    - Add measurable achievements where possible
    - Make it modern and professional

    Return the full improved resume in clean structured format.

    Resume:
    {text}
    """

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": "You are a professional resume writer and career coach."},
                {"role": "user", "content": prompt}
            ]
        }
    )

    if response.status_code != 200:
        return {
            "error": "Optimization failed",
            "details": response.text
        }

    data = response.json()

    if "choices" in data:
        return {
            "optimized_resume": data["choices"][0]["message"]["content"]
        }
async def generate_cover_letter(resume_text, job_description):

    prompt = f"""
    Write a professional, tailored cover letter based on:

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Keep it concise, professional, and ATS-friendly.
    """

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    return {
        "cover_letter": data["choices"][0]["message"]["content"]
    }

    return data

