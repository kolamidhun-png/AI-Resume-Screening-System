# 🤖 AI Resume Screening System

An intelligent resume screening and job-matching system that uses Natural Language Processing, TF-IDF, and BERT-based semantic similarity to evaluate how well a candidate's resume matches a job description.

---

## 📌 Project Overview

Recruiters often need to review a large number of resumes for a single job position. Manual screening can be time-consuming and may lead to inconsistent evaluation.

This project automates the initial resume screening process by extracting information from PDF resumes, identifying technical skills, comparing resume content with job descriptions, and generating a final matching score.

The system combines three major approaches:

- Skill-based matching
- TF-IDF text similarity
- BERT semantic similarity

---

## 🎯 Objectives

- Automatically extract text from PDF resumes.
- Identify relevant technical skills.
- Compare resumes with job descriptions.
- Calculate TF-IDF similarity.
- Calculate semantic similarity using BERT.
- Generate a weighted final matching score.
- Recommend candidates based on the final score.
- Display matched and missing skills.
- Provide an easy-to-use web interface.

---

## 🚀 Features

- 📄 PDF Resume Upload
- 🧹 Automatic Text Preprocessing
- 🧠 Technical Skill Extraction
- 📚 TF-IDF Matching
- 🤖 BERT Semantic Matching
- 📊 Weighted Resume Score
- ✅ Matched Skills
- ❌ Missing Skills
- 🎯 Candidate Recommendation
- 📈 Score Visualization
- 🌐 Streamlit Web Interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application |
| Pandas | Dataset handling |
| Scikit-learn | TF-IDF and cosine similarity |
| Sentence Transformers | BERT-based semantic similarity |
| PyTorch | Deep learning backend |
| PDFPlumber | PDF text extraction |
| Matplotlib | Data visualization |
| Jupyter Notebook | ML/NLP experimentation |

---

## 🧠 System Architecture

```text
Resume PDF
    │
    ▼
PDF Text Extraction
    │
    ▼
Text Preprocessing
    │
    ▼
Skill Extraction
    │
    ├───────────────┐
    ▼               ▼
TF-IDF          BERT
Matching        Semantic Matching
    │               │
    └───────┬───────┘
            ▼
      Weighted Scoring
            │
            ▼
      Candidate Ranking
            │
            ▼
   Recommendation Result