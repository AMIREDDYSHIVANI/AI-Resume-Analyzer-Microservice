 AI Resume Intelligence Platform

A production-ready, Dockerized AI-powered resume analysis platform built using FastAPI, Streamlit, and OpenRouter LLM APIs.

This platform performs intelligent resume evaluation, ATS scoring, job-description matching, resume optimization, and automated cover letter generation.

---

-- Core Features

###  ATS Resume Analysis
Upload a resume PDF and receive:

- ATS Score (0–100)
- Strength analysis
- Missing skills detection
- Improvement suggestions
- Professional summary evaluation

---

###  Resume vs Job Description Matching

Paste a Job Description to receive:

- Match Score (0–100)
- Matched Skills Breakdown
- Missing Skill Identification
- Skill Coverage Percentage
- High-Priority Missing Skills Highlighting

---

###  Resume Optimization

Generate a fully rewritten, ATS-friendly resume:

- Strong action verbs
- Improved bullet structure
- Measurable impact statements
- Modern formatting

Export as:
- DOCX
- PDF

---

###  AI Cover Letter Generator

Generate a professional, job-specific cover letter using:

- Resume content
- Job description context

Export as:
- DOCX

---

##  UI Features

- Skill Coverage Heatmap
- Dark Mode Toggle
- Session Usage Counter
- Basic Password Authentication
- Downloadable Reports (PDF + DOCX)

---

##  Architecture Overview

Streamlit Frontend  
↓  
FastAPI Backend (Dockerized)  
↓  
OpenRouter LLM API (Mistral-7B Instruct)

Docker Compose orchestrates:

- resume_frontend
- resume_backend

---

##  Technology Stack

Backend: FastAPI  
Frontend: Streamlit  
AI Model: OpenRouter (Mistral-7B Instruct)  
Containerization: Docker & Docker Compose  
PDF Parsing: pdfplumber  
Document Generation: ReportLab, python-docx  
Environment Handling: python-dotenv  

---

##  Project Structure

AI-Resume-Analyzer-Microservice/

resume_analyzer/  
 app/  
  main.py  
  routes/  
  services/  

frontend.py  
Dockerfile.backend  
Dockerfile.frontend  
docker-compose.yml  
requirements.txt  
.env  

---

##  Run With Docker

1. Clone Repository

git clone https://github.com/AMIREDDYSHIVANI/AI-Resume-Analyzer-Microservice.git  
cd AI-Resume-Analyzer-Microservice  

2. Create .env file in root

OPENROUTER_API_KEY=your_api_key_here  

3. Start application

docker-compose up --build  

Access:

Frontend → http://localhost:8501  
Backend Docs → http://localhost:8000/docs  

---

##  Engineering Practices

- JSON sanitization for LLM responses  
- Markdown stripping before JSON parsing  
- API failure fallback handling  
- Safe session-state rendering in Streamlit  
- Docker internal service routing  
- Secure environment variable loading  

---

##  Version

v1.0 – Initial Production Release  

---

##  Author

Shivani  
AI & Backend Engineer
