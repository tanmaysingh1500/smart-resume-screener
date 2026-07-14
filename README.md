# 🧠 Smart Resume Screener

> An AI-powered resume screening platform that intelligently evaluates candidates against a Job Description using **Large Language Models (Gemini)** and **Semantic Embeddings**.

Instead of relying on simple keyword matching, Smart Resume Screener understands both the **meaning** and **context** of resumes, producing recruiter-friendly insights, explainable scores, and hiring recommendations.

---

# ✨ Features

- 📄 Upload one Job Description and multiple resumes
- 🔍 Automatic PDF text extraction
- 🤖 AI-powered document structuring using Gemini
- 🧠 Recruiter-style candidate evaluation
- 🔗 Semantic similarity scoring using Gemini Embeddings
- ⚖️ Fusion scoring combining LLM reasoning with embeddings
- 📊 Candidate ranking
- 💡 Strengths & weaknesses analysis
- 📈 Explainable scoring for every evaluation dimension

---

# Demo Pipeline

```
                PDFs

                   │
                   ▼

          Document Extraction

                   │
                   ▼

             Raw Text

                   │
                   ▼

          Gemini 3.5 Flash

                   │

      ┌────────────┴────────────┐

      ▼                         ▼

Structured Output         Recruiter Evaluation

      │                         │

      └────────────┬────────────┘

                   ▼

        Gemini Embeddings

                   ▼

        Semantic Similarity

                   ▼

          Fusion Engine

                   ▼

        Final Candidate Score

                   ▼

          Recruiter Dashboard
```

---

# Motivation

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching.

Example:

**Job Description**

> Experience with backend API development using Python and FastAPI.

Resume

> Built scalable REST services using FastAPI.

Although both refer to the same skill, keyword-based systems may assign a poor score.

This project solves that by combining:

- LLM reasoning
- Semantic embeddings
- Explainable scoring

---

# Tech Stack

## Frontend

- React
- TypeScript
- TailwindCSS
- Base UI
- Vite

---

## Backend

- FastAPI
- Python
- PyMuPDF
- Google Gemini API
- Gemini Embeddings API
- Pydantic

---

## AI Models

### LLM

Gemini 3.5 Flash

Used for:

- Structuring documents
- Identifying relevant comparison dimensions
- Recruiter evaluation
- Candidate recommendations
- Strengths & weaknesses

---

### Embeddings

Gemini Embedding 2

Used for:

- Semantic similarity
- Meaning-based comparison
- Technical skill matching
- Context-aware evaluation

---

# Project Structure

```
backend/

│
├── app/
│
├── extractor/
│     document_extractor.py
│
├── embeddings/
│     client.py
│     similarity.py
│     scorer.py
│
├── llm/
│     client.py
│     prompts.py
│     schemas.py
│     structure.py
│
├── scorer/
│     fusion.py
│     weights.py
│
├── processor/
│
├── utils/
│
└── main.py


frontend/

src/

components/

services/

types/

App.tsx
```

---

# AI Pipeline

## 1. PDF Extraction

Uploaded PDFs are converted into raw text using PyMuPDF.

```
Resume PDF

↓

Raw Text
```

---

## 2. LLM Structuring

Gemini receives:

- Job Description
- Resume

and returns structured JSON.

Example:

```json
{
  "comparison_dimensions": [
    "programming_languages",
    "frameworks",
    "databases",
    "experience"
  ],

  "job_description": {
    ...
  },

  "candidate_resume": {
    ...
  },

  "llm_evaluation": {
    ...
  }
}
```

Unlike traditional parsers, the LLM dynamically identifies only the relevant comparison dimensions for each role.

---

## 3. LLM Evaluation

Gemini acts as an experienced recruiter.

It provides:

- Overall score
- Recommendation
- Confidence
- Strengths
- Weaknesses
- Dimension-level reasoning

Example

```
Programming Languages

100

Reason

Candidate has extensive Python experience.
```

---

## 4. Semantic Embeddings

Every comparison dimension is embedded separately.

Instead of comparing entire resumes,

we compare:

```
Python

↓

Python

Similarity
```

```
AWS

↓

AWS Cloud Deployment

Similarity
```

```
Backend Experience

↓

REST API Development

Similarity
```

This produces far more meaningful scores than keyword matching.

---

## 5. Fusion Engine

The final score combines:

```
70%

LLM Score

+

30%

Embedding Score
```

Result:

```
Final Candidate Score
```

This approach combines:

Human-like reasoning

+

Objective semantic similarity

---

# Example Output

```
John_Doe.pdf

Overall Score

96.48

Recommendation

Strong Hire

Confidence

100%

Strengths

✔ Python
✔ FastAPI
✔ PostgreSQL
✔ AWS

Weaknesses

• Kubernetes not mentioned
```

---

# Installation

## Clone

```bash
git clone https://github.com/yourusername/smart-resume-screener.git

cd smart-resume-screener
```

---

# Backend

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create

```
.env
```

```
GEMINI_API_KEY=YOUR_API_KEY

GEMINI_MODEL=models/gemini-3.5-flash

EMBEDDING_MODEL=models/gemini-embedding-2
```

Run

```bash
uvicorn app.main:app --reload
```

---

# Frontend

Install

```bash
npm install
```

Run

```bash
npm run dev
```

---

# API

## POST

```
/api/v1/screening
```

FormData

```
jobDescription

resumes
```

Returns

```json
{
    "status":"success",

    "results":[
        ...
    ]
}
```

---

# Scoring Methodology

Each candidate is evaluated across multiple dimensions.

Example

- Programming Languages
- Frameworks
- Databases
- Experience
- Cloud Platforms
- DevOps
- Education

Each dimension receives

- LLM Score
- Embedding Score
- Final Score

Final score

```
70%

LLM

+

30%

Embeddings
```

---

# Why use both LLMs and Embeddings?

LLMs are excellent at:

- reasoning
- summarization
- judging relevance

Embeddings are excellent at:

- semantic similarity
- contextual matching
- meaning comparison

Combining both provides:

✔ Explainability

✔ Better accuracy

✔ Less keyword dependence

✔ Human-like evaluation

---

# Future Improvements

- Candidate ranking dashboard
- Resume comparison view
- ATS score visualization
- Interview question generation
- Resume improvement suggestions
- Skill gap analysis
- Recruiter notes
- Export PDF reports
- CSV export
- Authentication
- Database integration
- Job history
- Multi-company support
- Email notifications
- Vector database caching
- Batch processing
- Background workers
- Docker deployment
- Kubernetes deployment

---

# Roadmap

## Phase 1

- Upload UI
- PDF extraction

✅ Completed

---

## Phase 2

- Gemini structuring
- Recruiter evaluation

✅ Completed

---

## Phase 3

- Gemini embeddings
- Semantic similarity
- Fusion scoring

✅ Completed

---

## Phase 4

- Recruiter dashboard

🚧 In Progress

---

# License

MIT License

---

# Author

**Tanmay Singh**

AI Engineer | Full Stack Developer

Built with ❤️ using FastAPI, React and Google Gemini.