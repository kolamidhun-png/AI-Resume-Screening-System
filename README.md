# 🤖 AI Resume Screening System

An AI-powered resume screening and job matching system that analyzes a candidate's resume against job requirements using Natural Language Processing (NLP), skill matching, TF-IDF similarity, and BERT-based semantic similarity.

## 🌐 Live Demo

[AI Resume Screening System · Streamlit](https://ai-resume-screening-system-hggfaqwwi2cxxdkhqd3nbz.streamlit.app/)

## 📌 Project Overview

Recruiters often need to evaluate large numbers of resumes against different job descriptions. This project automates the initial screening process by extracting information from a candidate's resume and comparing it with job requirements.

The system combines multiple matching techniques to calculate an overall compatibility score and provide a candidate recommendation.

## ✨ Features

- 📄 Upload and extract text from PDF resumes
- 🧹 Text preprocessing and normalization
- 🛠️ Automatic resume skill extraction
- 📚 TF-IDF-based text similarity
- 🤖 BERT-based semantic similarity
- 🎯 Skill matching score
- ⭐ Combined final compatibility score
- 📊 Screening results visualization
- ⚠️ Matched and missing skills analysis
- 🖥️ Interactive Streamlit web interface
- 🧪 Automated unit testing with pytest

## 🧠 How It Works

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Text Preprocessing
    ↓
Skill Extraction
    ↓
┌─────────────────────────────┐
│     Matching Techniques     │
│                             │
│  Skill Matching             │
│  TF-IDF Similarity          │
│  BERT Semantic Similarity   │
└─────────────────────────────┘
    ↓
Score Calculation
    ↓
Final Compatibility Score
    ↓
Candidate Recommendation