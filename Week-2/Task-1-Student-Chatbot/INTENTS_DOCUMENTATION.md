# Intents Documentation — Student Success Assistant

> WeIntern Pvt Ltd · AI Internship · Week 2, Task 1
>
> **61 intents · 597 patterns · 1 Gemini AI fallback**

---

## How to Read This Table

Each row is one intent. The **Tag** is its internal identifier used by the matching engine, **Triggers when user says** shows an example phrase that activates it, and **Covers** summarizes what the response addresses.

When no intent scores >= 0.5 confidence, the **Gemini AI fallback** handles the query automatically.

---

## General Conversation

| Tag | Triggers when user says | Covers |
|---|---|---|
| `greeting` | "hi there" | Opening the conversation |
| `goodbye` | "bye see you later" | Ending the session |
| `how_are_you` | "how are you doing today" | Asking about the bot's status |
| `thank_you` | "thank you so much" | Expressing gratitude |
| `who_are_you` | "who are you exactly" | Asking about the bot's identity |
| `what_can_you_do` | "what can you help me with" | Asking what topics the bot handles |
| `compliment_bot` | "you are really amazing" | Complimenting the bot |

---

## Career Guidance

| Tag | Triggers when user says | Covers |
|---|---|---|
| `career_after_btech` | "what are my career options after completing btech" | Career paths available after B.Tech graduation |
| `choose_career_field` | "which field should i choose for my career" | Choosing the right tech domain or career field |
| `career_assessment` | "can you help me find the right career for my personality" | Finding a career based on interests and personality |
| `career_interest_coding` | "i really enjoy coding and programming" | Career paths for students who love coding |
| `career_interest_design` | "i love visual design and creativity above all" | Career paths for students interested in UI/UX design |
| `career_interest_business` | "i enjoy business strategy and management more than tech" | Career paths for business and management-oriented students |
| `ai_vs_webdev` | "should i choose ai or web development as a career" | Comparing AI/ML vs Web Development as a career |
| `non_tech_careers` | "what are careers without any coding at all" | Non-coding career options for engineers |
| `govt_jobs` | "what government jobs can i get after engineering" | Government jobs and PSU opportunities after engineering |
| `mba_guidance` | "should i do mba after engineering" | Whether to pursue MBA after engineering and how |
| `higher_studies_abroad` | "how do i apply for higher studies abroad" | MS and higher studies in USA, Germany, etc. |
| `competitive_exams` | "what competitive exams should i give after engineering" | GATE, GRE, CAT and other post-graduation exams |

---

## Internships

| Tag | Triggers when user says | Covers |
|---|---|---|
| `find_internships` | "how do i find internships as a student" | Where and how to search for internships |
| `internship_resume` | "how do i make a resume for internship application" | Building a resume for internship applications |
| `internship_preparation` | "how do i prepare for an internship interview" | Preparing for internship interviews |
| `internship_platforms` | "tell me about internshala for finding internships" | Internshala, LinkedIn, Unstop and similar platforms |
| `first_internship_tips` | "give me tips for surviving my first internship" | Making the most of your first internship |

---

## Placement Preparation

| Tag | Triggers when user says | Covers |
|---|---|---|
| `aptitude_round` | "tell me about the aptitude round in placements" | Quantitative, logical, and verbal aptitude preparation |
| `technical_round` | "how do i prepare for the technical interview round" | Technical interview preparation strategy |
| `hr_interview` | "how do i prepare for the hr interview round" | HR round questions and self-introduction tips |
| `group_discussion` | "how do i perform well in a group discussion" | GD tips and strategies for placement rounds |
| `coding_round` | "how do i prepare for the coding round in placements" | Online coding tests — HackerRank, LeetCode preparation |
| `placement_timeline` | "how do i prepare for campus placements in general" | Month-wise placement preparation roadmap |
| `product_based_companies` | "how do i get into product based companies" | Preparing for Google, Microsoft, Amazon, FAANG |
| `service_based_companies` | "how do i prepare for service based companies" | Preparing for TCS, Infosys, Wipro, Accenture |
| `non_tech_company_prep` | "how do i prepare for non technical company placements" | Consulting and management company hiring process |

---

## Learning Resources

| Tag | Triggers when user says | Covers |
|---|---|---|
| `learn_python` | "how do i learn python from scratch" | Python learning roadmap and best resources |
| `learn_dsa` | "how do i learn data structures and algorithms" | Data Structures and Algorithms roadmap for placements |
| `learn_ai_ml` | "how do i learn artificial intelligence from scratch" | AI/ML learning path from scratch |
| `learn_web_dev` | "how do i learn web development from scratch" | Web development roadmap — frontend to backend |
| `learn_sql` | "how do i learn sql from scratch" | SQL and database fundamentals for data roles |
| `learning_general` | "what can i learn from you today" | General guidance on what to learn as a student |
| `free_learning_platforms` | "what are the best free learning platforms for students" | Free courses — Coursera, YouTube, edX, etc. |

---

## Soft Skills

| Tag | Triggers when user says | Covers |
|---|---|---|
| `self_introduction` | "how do i introduce myself in an interview" | Introducing yourself in interviews and networking |
| `improve_communication` | "how do i improve my communication skills as a student" | Building English communication and public speaking |
| `start_conversation` | "how do i start a conversation with someone new professionally" | Starting professional conversations at events |
| `networking_tips` | "give me professional networking tips for students" | Building a professional network as a student |
| `linkedin_tips` | "give me linkedin profile tips" | Optimizing LinkedIn profile for recruiters |
| `email_etiquette` | "how do i write a professional email properly" | Writing formal emails to professors or companies |

---

## Student Life & Motivation

| Tag | Triggers when user says | Covers |
|---|---|---|
| `exam_stress` | "i am feeling very stressed about my upcoming exams" | Managing exam anxiety and academic pressure |
| `low_cgpa` | "my cgpa is very low will it affect my placement chances" | Career options and strategies with a low CGPA |
| `no_skills_yet` | "i feel like i have no skills at all to offer" | Where to start when you feel you have no skills |
| `imposter_syndrome` | "i feel like a fraud among my peers" | Dealing with self-doubt among peers |
| `motivation` | "i am feeling very demotivated right now" | Encouragement when feeling lost or demotivated |
| `time_management` | "how do i manage my time better as a student" | Productivity tips and beating procrastination |
| `backlog_guidance` | "i have backlogs in my college subjects what do i do" | Clearing backlogs before placements |
| `project_ideas` | "give me some project ideas to put on my resume" | Portfolio project ideas for resume and GitHub |
| `choose_electives` | "how do i choose the right electives in college" | Picking college electives aligned with career goals |
| `salary_expectation` | "what is the salary after btech for freshers in india" | Fresher salary ranges across IT roles in India |

---

## Specialized Career Tracks

| Tag | Triggers when user says | Covers |
|---|---|---|
| `cybersecurity_career` | "how do i start a career in cybersecurity" | Cybersecurity and ethical hacking career roadmap |
| `cloud_computing` | "tell me about a career in cloud computing" | Cloud computing and DevOps career path |
| `data_science_career` | "how do i start a career in data science" | Data Science and Analytics career roadmap |
| `startup_vs_mnc` | "should i join a startup or an mnc for my first job" | Comparing startup vs MNC for first job |
| `choose_programming_language` | "which programming language should i learn first" | Picking the right programming language to learn first |

---

## Fallback — Gemini AI

| Trigger | Behavior |
|---|---|
| No intent scores >= 0.5 | Query sent to Gemini `gemini-3.1-flash-lite` with last 4 turns of conversation as context |
| CLI mode | Built-in fallback message returned (Gemini not active in CLI) |

The Gemini system prompt defines the bot persona: warm and encouraging tone like a helpful senior, responses under 150 words, always ends with one actionable tip.

---

## Matching Logic

```
Jaccard Score = |user tokens ∩ pattern tokens| / max(|user tokens|, |pattern tokens|)

Boosters:
  +0.30  → all pattern tokens found in user input (subset match)
  +0.01  → per overlapping token (rewards specificity)

Threshold: 0.5
  >= 0.5  → return intent response
  <  0.5  → Gemini AI fallback
```

---

*Week 2 · Task 1 · Student Success Chatbot · WeIntern AI Internship*