# AI Content Generator

**An AI-powered content generation tool** — produce high-quality written content across 9 content types and 12 tones, with 3 simultaneous variations, powered by Google Gemini.

> WeIntern Pvt Ltd · AI Internship · Week 2, Task 3

---

## Demo

![AI Content Generator - Main UI](responses/screenshot1.png)
*Select content type, tone, enter your topic and generate*

![Generated Variations - LinkedIn Post](responses/screenshot2.png)
*3 variations in tabs with word count, character count, copy and regenerate options*

---

## How It Works

1. User enters their **Gemini API key**, selects a **content type** and **tone**, and describes their **topic**
2. The app calls a role-specific prompt template from `prompts.py`, tailored to the chosen content type and tone
3. Google Gemini (`gemini-3.1-flash-lite`) generates **3 independent variations** simultaneously
4. Results are displayed in tabs with word count, character count, a copy-to-clipboard button, and a regenerate option

---

## Features

- 9 content types — Blog Post, Social Media Caption, LinkedIn Post, Email Subject Line, Text Summary, YouTube Video Description, Product Description, Tweet Thread, Newsletter Intro
- 12 tones — Professional, Casual, Friendly, Persuasive, Humorous, Inspirational, Formal, Storytelling, Minimalist, Empathetic, Bold & Edgy, Poetic
- 3 variations generated per request — displayed in switchable tabs
- Word count and character count for each variation
- Copy to clipboard via `pyperclip`
- Regenerate all variations with one click
- Role-specific prompt templates in `prompts.py` — each content type has a dedicated, structured prompt
- Deep purple and gold dark theme with Poppins font

---

## Project Structure

```
Task-3-Content-Generator/
│
├── app.py               # Main Streamlit application
├── prompts.py           # Role-specific prompt templates for all 9 content types
├── requirements.txt     # Python dependencies
│
├── responses/           # Demo outputs
│   ├── screenshot1.png  # Main UI
│   ├── screenshot2.png  # Generated variations
│   └── ...
│
└── README.md
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| UI Framework | Streamlit |
| AI Backend | Google Gemini `gemini-3.1-flash-lite` via `google-genai` |
| Clipboard | pyperclip |
| Prompt Engineering | Custom role-specific templates in `prompts.py` |

---

## Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/euphoricv7/weintern-ai-internship.git
cd weintern-ai-internship/Week-2/Task-3-Content-Generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get a Gemini API key

Get a free key at [Google AI Studio](https://aistudio.google.com/) and paste it into the app when prompted.

---

## Running the App

```bash
streamlit run app.py
```

Open → `http://localhost:8501`

---

## How to Use

1. Paste your **Gemini API key** in the authentication field
2. Select a **Content Type** from the dropdown (e.g. Blog Post, LinkedIn Post)
3. Select a **Tone** (e.g. Professional, Humorous, Poetic)
4. Enter your **topic or description** in the text area
5. Click **Generate Content**
6. Browse the 3 variations across tabs
7. Copy your preferred variation or click **Regenerate All Variations** for fresh outputs

---

## Content Types & Prompt Design

Each content type in `prompts.py` has a dedicated prompt with specific requirements:

| Content Type | Output Format | Length |
|---|---|---|
| Blog Post | Title + intro + 3-4 subheadings + conclusion | 300-400 words |
| Social Media Caption | Hook + hashtags + emojis | 50-80 words |
| LinkedIn Post | Strong opening + insight + question + hashtags | 150-200 words |
| Email Subject Line | 5 varied subject lines under 60 characters | — |
| Text Summary | Key points, easy to read | 100-150 words |
| YouTube Video Description | Hook + bullet points + CTA + SEO hashtags | 150-200 words |
| Product Description | Headline + benefits + features + CTA | 100-150 words |
| Tweet Thread | 5-7 tweets, numbered, under 280 chars each | — |
| Newsletter Intro | Greeting + hook + preview + transition | 80-120 words |

---

## Requirements

```
streamlit
google-genai
pyperclip
```

---

## Author

**Vratika Kumawat** · AI Intern, WeIntern Pvt Ltd
GitHub: [@euphoricv7](https://github.com/euphoricv7)

---

*Week 2 · Task 3 · AI Content Generator · WeIntern AI Internship*
