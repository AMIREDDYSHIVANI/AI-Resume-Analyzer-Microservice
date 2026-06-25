# 🤖 AI Resume Intelligence Platform

[![CI](https://github.com/AMIREDDYSHIVANI/AI-Resume-Analyzer-Microservice/actions/workflows/ci.yml/badge.svg)](https://github.com/AMIREDDYSHIVANI/AI-Resume-Analyzer-Microservice/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready, Dockerized AI-powered resume analysis platform built with FastAPI, Streamlit, and OpenRouter LLM APIs.

---

## ✨ Core Features

### 📋 ATS Resume Analysis
Upload a resume PDF and receive:
- ATS Score (0–100)
- Strength analysis & improvement suggestions
- Missing skills detection
- Professional summary evaluation

### 🎯 Resume vs Job Description Matching
Paste a job description to receive:
- Match Score (0–100)
- Matched & missing skills breakdown
- Skill coverage percentage
- High-priority missing skills highlighting

### ✏️ Resume Optimization
Generate a fully rewritten, ATS-friendly resume with:
- Strong action verbs & measurable impact statements
- Improved bullet structure & modern formatting
- Export as DOCX or PDF

### 💌 AI Cover Letter Generator
Generate a professional, job-specific cover letter using your resume + job description context. Export as DOCX.

### 🖥️ UI Features
- 📊 Skill Coverage Heatmap
- 🌙 Dark Mode Toggle
- 🔒 Basic Password Authentication
- 📥 Downloadable Reports (PDF + DOCX)
- 🔢 Session Usage Counter

---

## 🔄 How It Works

```
User Uploads Resume PDF
        |
        v
Streamlit Frontend (port 8501)
  - PDF upload UI
  - Job description input
  - Results dashboard
  - Export buttons
        |  HTTP REST
        v
FastAPI Backend (port 8000)
  - PDF text extraction (pdfplumber)
  - Prompt engineering & LLM request
  - JSON sanitization & response parsing
        |  API Call
        v
OpenRouter LLM API (Mistral-7B Instruct)
  - ATS scoring & skill gap analysis
  - Resume rewrite & cover letter generation
```

---

## 🏗️ Architecture

Docker Compose orchestrates two services:

| Service | Description | Port |
|---|---|---|
| `resume_frontend` | Streamlit UI | 8501 |
| `resume_backend` | FastAPI service | 8000 |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| Frontend | Streamlit |
| AI Model | OpenRouter (Mistral-7B Instruct) |
| Containerization | Docker & Docker Compose |
| PDF Parsing | pdfplumber |
| Document Generation | ReportLab, python-docx |
| Config | python-dotenv |

---

## 📁 Project Structure

```
AI-Resume-Analyzer-Microservice/
├── .github/
│   └── workflows/
│       └── ci.yml
├── resume_analyzer/
│   └── app/
│       ├── main.py
│       ├── routes/
│       └── services/
├── frontend.py
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose installed
- OpenRouter API key (free tier at [openrouter.ai](https://openrouter.ai))

### Run With Docker

1. Clone the repository
```bash
git clone https://github.com/AMIREDDYSHIVANI/AI-Resume-Analyzer-Microservice.git
cd AI-Resume-Analyzer-Microservice
```

2. Create `.env` file
```env
OPENROUTER_API_KEY=your_api_key_here
```

3. Start the app
```bash
docker-compose up --build
```

4. Access the app

| Service | URL |
|---|---|
| Frontend (Streamlit) | http://localhost:8501 |
| Backend API Docs (Swagger) | http://localhost:8000/docs |
| Backend API (ReDoc) | http://localhost:8000/redoc |

---

## 📖 API Documentation

- **Swagger UI** → `http://localhost:8000/docs` — Try endpoints live
- **ReDoc** → `http://localhost:8000/redoc` — Readable API reference

| Method | Endpoint | Description |
|---|---|---|
| POST | `/analyze` | ATS score + feedback |
| POST | `/match` | JD match scoring |
| POST | `/optimize` | Rewrite resume |
| POST | `/cover-letter` | Generate cover letter |

---

## 🔧 Engineering Practices

- ✅ JSON sanitization for LLM responses
- ✅ Markdown stripping before JSON parsing
- ✅ API failure fallback handling
- ✅ Safe session-state rendering in Streamlit
- ✅ Docker internal service routing
- ✅ Secure environment variable loading
- ✅ GitHub Actions CI on every push

---

## 🗺️ Roadmap

- [x] ATS resume scoring
- [x] JD matching & skill gap analysis
- [x] Resume optimization & rewrite
- [x] AI cover letter generation
- [x] Docker containerization
- [x] GitHub Actions CI
- [ ] OAuth user authentication
- [ ] Resume history & version tracking
- [ ] Cloud deployment (AWS/GCP)

---

## 📄 Version

v1.0 — Initial Production Release

---

## 👩‍💻 Author

**Shivani Amireddy** — AI & Backend Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/shivani-reddy-458600400)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/AMIREDDYSHIVANI)
