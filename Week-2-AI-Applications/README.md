# Week 2 — AI Application Development

**Intern:** Vratika Kumawat  
**Organization:** WeIntern Pvt Ltd  
**Program:** AI Internship — 2026

This week covers building three production-ready AI applications using Python, NLP, and Google Gemini — each with a Streamlit or Flask interface, consistent dark theme UI, and full documentation.

---

## Tasks

| Task | Project | Tech Stack | Status |
|---|---|---|---|
| Task 1 | Student Success Chatbot | NLTK · Flask · Gemini AI | Complete |
| Task 2 | Resume Screening AI | Sentence-BERT · Streamlit · pdfplumber | Complete |
| Task 3 | AI Content Generator | Google Gemini · Streamlit · pyperclip | Complete |

---

## Task 1 — Student Success Chatbot

A hybrid AI chatbot for Indian college students covering careers, internships, placements, learning resources, and student life. Uses Jaccard similarity for intent matching with Google Gemini as a fallback for unrecognized queries.

- 61 intents · 597 patterns
- Flask web app + CLI interface
- Context-aware multi-turn conversation
- Full session logging

[View Task 1 →](Task-1-Student-Chatbot/)

---

## Task 2 — Resume Screening AI

An intelligent candidate ranking system that scores resumes against a job description using Sentence-BERT semantic similarity. Supports CSV datasets and PDF resume uploads.

- Sentence-BERT (`all-MiniLM-L6-v2`) + cosine similarity
- Leaderboard-style results with stat cards
- Downloadable CSV ranking report
- Sample datasets included (100 candidates, 25 job roles)

[View Task 2 →](Task-2-Resume-Screening/)

---

## Task 3 — AI Content Generator

A multi-tone AI content generator that produces 3 simultaneous variations across 9 content types and 12 tones, powered by Google Gemini.

- 9 content types — Blog Post, LinkedIn Post, Tweet Thread, and more
- 12 tones — Professional, Humorous, Poetic, and more
- Role-specific prompt templates in `prompts.py`
- Copy to clipboard + regenerate functionality

[View Task 3 →](Task-3-Content-Generator/)

---

*Week 2 · WeIntern AI Internship — 2026*
