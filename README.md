<h1 align="center">🤖 AI Resume Intelligence Platform</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"/>
</p>

<p align="center">
  A production-ready, Dockerized AI-powered resume analysis platform built with FastAPI, Streamlit, and OpenRouter LLM APIs. Performs intelligent resume evaluation, ATS scoring, job-description matching, resume optimization, and automated cover letter generation.
</p>

---

## ✨ Core Features

### 📋 ATS Resume Analysis
Upload a resume PDF and receive:
- **ATS Score** (0–100)
- Strength analysis & improvement suggestions
- Missing skills detection
- Professional summary evaluation

### 🎯 Resume vs Job Description Matching
Paste a job description to receive:
- **Match Score** (0–100)
- Matched & missing skills breakdown
- Skill coverage percentage
- High-priority missing skills highlighting

### ✏️ Resume Optimization
Generate a fully rewritten, ATS-friendly resume with:
- Strong action verbs & measurable impact statements
- Improved bullet structure & modern formatting
- Export as **DOCX** or **PDF**

### 💌 AI Cover Letter Generator
Generate a professional, job-specific cover letter using your resume + job description context. Export as **DOCX**.

### 🖥️ UI Features
- 📊 Skill Coverage Heatmap
- 🌙 Dark Mode Toggle
- 🔒 Basic Password Authentication
- 📥 Downloadable Reports (PDF + DOCX)
- 🔢 Session Usage Counter

---

## 🏗️ Architecture

```
Streamlit Frontend (port 8501)
        │
        ▼
FastAPI Backend (port 8000) — Dockerized
        │
        ▼
OpenRouter LLM API (Mistral-7B Instruct)
```

Docker Compose orchestrates:
- `resume_frontend` — Streamlit UI
- `resume_backend` — FastAPI service

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
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
- OpenRouter API key (free tier available at [openrouter.ai](https://openrouter.ai))

### Run With Docker

1. **Clone the repository**

```bash
git clone https://github.com/AMIREDDYSHIVANI/AI-Resume-Analyzer-Microservice.git
cd AI-Resume-Analyzer-Microservice
```

2. **Create `.env` file in root**

```env
OPENROUTER_API_KEY=your_api_key_here
```

3. **Start the application**

```bash
docker-compose up --build
```

4. **Access the app**

| Service | URL |
|---------|-----|
| Frontend (Streamlit) | http://localhost:8501 |
| Backend API Docs | http://localhost:8000/docs |

---

## 🔧 Engineering Practices

- ✅ JSON sanitization for LLM responses
- ✅ Markdown stripping before JSON parsing
- ✅ API failure fallback handling
- ✅ Safe session-state rendering in Streamlit
- ✅ Docker internal service routing
- ✅ Secure environment variable loading

---

## 🗺️ Roadmap

- [x] ATS resume scoring
- [x] JD matching & skill gap analysis
- [x] Resume optimization & rewrite
- [x] AI cover letter generation
- [x] Docker containerization
- [ ] OAuth user authentication
- [ ] Resume history & version tracking
- [ ] Cloud deployment (AWS/GCP)

---

## 📄 Version

**v1.0** — Initial Production Release

---

## 👩‍💻 Author

**Shivani Amireddy** — AI & Backend Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shivani-reddy-458600400)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/AMIREDDYSHIVANI)
