import os
from dotenv import load_dotenv
import pdfplumber
from openai import OpenAI

load_dotenv(dotenv_path=".env")

print("LOADED KEY:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def analyze_resume(file):

    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(await file.read())

    # Extract text from PDF
    text = ""
    with pdfplumber.open("temp_resume.pdf") as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    prompt = f"""
    Analyze this resume and provide:
    1. Key strengths
    2. Missing skills
    3. Suggested improvements
    4. Overall rating out of 10
    
    Resume:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert HR recruiter."},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "analysis": response.choices[0].message.content
    }
