import streamlit as st
import pdfplumber
import nltk
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("punkt_tab", quiet=True)

st.set_page_config(page_title="Resume Screening AI", page_icon="📄", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* { font-family: 'Poppins', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0d0015 0%, #1a0030 40%, #0d0020 100%);
    min-height: 100vh;
}

.hero {
    background: rgba(139,92,246,0.08);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    backdrop-filter: blur(10px);
}
.hero-title {
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #bf80ff, #ffcc00, #bf80ff);
    background-size: 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s infinite linear;
    margin: 0;
}
@keyframes shimmer {
    0% { background-position: 0% }
    100% { background-position: 200% }
}
.hero-sub { color: #c084fc; font-size: 0.9rem; margin-top: 0.3rem; }
.hero-badge {
    background: rgba(255,204,0,0.1);
    border: 1px solid rgba(255,204,0,0.3);
    color: #ffcc00;
    padding: 0.5rem 1.2rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}

.section-header {
    font-size: 0.75rem;
    font-weight: 600;
    color: #a78bfa;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(139,92,246,0.2);
}

.stat-card {
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.25);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}
.stat-number { font-size: 1.8rem; font-weight: 800; color: #ffcc00; }
.stat-label { font-size: 0.75rem; color: #c084fc; margin-top: 0.2rem; }

.top-card {
    background: linear-gradient(135deg, rgba(124,58,237,0.3), rgba(109,40,217,0.2));
    border: 1px solid rgba(167,139,250,0.4);
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.top-label { font-size: 0.7rem; color: #a78bfa; letter-spacing: 0.1em; text-transform: uppercase; }
.top-name { font-size: 1.3rem; font-weight: 700; color: #f3e8ff; margin-top: 0.2rem; }
.top-skills { font-size: 0.75rem; color: #c084fc; margin-top: 0.2rem; }
.top-score { font-size: 2.8rem; font-weight: 800; color: #ffcc00; }

.row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0.65rem 1rem;
    border-radius: 10px;
    margin-bottom: 0.35rem;
    background: rgba(139,92,246,0.07);
    border: 1px solid rgba(139,92,246,0.15);
    transition: all 0.2s;
}
.row:hover { background: rgba(139,92,246,0.14); border-color: rgba(167,139,250,0.35); }
.rank { font-size: 0.95rem; font-weight: 700; min-width: 32px; text-align: center; }
.rank.gold { color: #ffcc00; }
.rank.silver { color: #c0c0c0; }
.rank.bronze { color: #cd7f32; }
.rank.other { color: #a78bfa; font-size: 0.8rem; }
.cname { font-weight: 600; color: #f3e8ff; font-size: 0.88rem; min-width: 130px; }
.skills { font-size: 0.72rem; color: #a78bfa; flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.bar-wrap { min-width: 90px; }
.bar-bg { background: rgba(139,92,246,0.2); border-radius: 999px; height: 5px; }
.bar-fill { height: 5px; border-radius: 999px; }
.bar-fill.green { background: linear-gradient(90deg, #48bb78, #38a169); }
.bar-fill.yellow { background: linear-gradient(90deg, #ffcc00, #ff9900); }
.bar-fill.red { background: linear-gradient(90deg, #fc8181, #e53e3e); }
.score { font-weight: 700; font-size: 0.82rem; min-width: 48px; text-align: right; }
.score.green { color: #68d391; }
.score.yellow { color: #ffcc00; }
.score.red { color: #fc8181; }
.verdict { font-size: 0.72rem; min-width: 80px; text-align: right; font-weight: 500; color: #e9d5ff; }

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: rgba(139,92,246,0.1) !important;
    border: 1px solid rgba(139,92,246,0.4) !important;
    border-radius: 12px !important;
    color: #f3e8ff !important;
    font-family: 'Poppins', sans-serif !important;
}
label { color: #c084fc !important; font-weight: 500 !important; }

div.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #9333ea);
    color: white;
    border: none;
    border-radius: 12px;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    box-shadow: 0 4px 20px rgba(124,58,237,0.4);
    transition: all 0.3s ease;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #ffcc00, #ff9900);
    color: #1a0030;
    box-shadow: 0 4px 20px rgba(255,204,0,0.4);
}
div.stButton > button[kind="primary"]:hover {
    box-shadow: 0 6px 25px rgba(255,204,0,0.6);
    transform: translateY(-2px);
}

.footer {
    text-align: center;
    margin-top: 3rem;
    padding: 1.5rem;
    border-top: 1px solid rgba(139,92,246,0.2);
    font-size: 0.8rem;
    color: #7c3aed;
}
</style>
""", unsafe_allow_html=True)

# ─── Hero ──────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div>
        <div class="hero-title">📄 Resume Screening AI</div>
        <div class="hero-sub">Intelligent candidate ranking powered by Sentence-BERT semantic similarity</div>
    </div>
    <div class="hero-badge">🎓 WeIntern AI Internship </div>
</div>
""", unsafe_allow_html=True)

# ─── Load Model ────────────────────────────────────────────
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

SKILL_KEYWORDS = [
    "python", "machine learning", "data analysis", "pandas", "numpy",
    "scikit-learn", "sql", "flask", "deep learning", "tensorflow",
    "keras", "pytorch", "data science", "statistics", "r programming",
    "matplotlib", "seaborn", "jupyter", "colab", "bigquery",
    "java", "javascript", "html", "css", "c++", "c#", "php",
    "linux", "aws", "azure", "docker", "git", "rest api", "mongodb",
    "mysql", "postgresql", "networking", "cybersecurity", "cloud",
    "excel", "powerpoint", "project management", "agile", "scrum",
    "figma", "photoshop", "illustrator", "ui design", "canva",
    "communication", "leadership", "teamwork", "management",
    "recruitment", "seo", "content writing", "accounting", "budgeting",
    "selenium", "testing", "crm", "digital marketing", "social media",
    "node.js", "react", "spring boot", "kubernetes", "docker", "ci/cd"
]

# ─── Functions ─────────────────────────────────────────────
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILL_KEYWORDS if skill in text_lower]

def compute_similarity_sbert(job_desc, resumes_dict):
    names = list(resumes_dict.keys())
    texts = list(resumes_dict.values())
    jd_embedding = model.encode([job_desc])
    resume_embeddings = model.encode(texts)
    similarities = cosine_similarity(jd_embedding, resume_embeddings)[0]
    results = []
    for i, name in enumerate(names):
        skills = extract_skills(texts[i])
        score = round(float(similarities[i]) * 100, 2)
        if score >= 50:
            verdict = "✅ Strong"
            color = "green"
        elif score >= 35:
            verdict = "⚠️ Maybe"
            color = "yellow"
        else:
            verdict = "❌ No"
            color = "red"
        results.append({
            "Candidate": name,
            "Match Score (%)": score,
            "Top Skills": ", ".join(skills) if skills else "None found",
            "Verdict": verdict,
            "color": color
        })
    return sorted(results, key=lambda x: x["Match Score (%)"], reverse=True)

def display_results(results):
    strong = sum(1 for r in results if r["color"] == "green")
    maybe  = sum(1 for r in results if r["color"] == "yellow")
    no     = sum(1 for r in results if r["color"] == "red")

    st.markdown('<div class="section-header">📊 Screening Summary</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="stat-card"><div class="stat-number">{len(results)}</div><div class="stat-label">Total Screened</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-card"><div class="stat-number" style="color:#68d391">{strong}</div><div class="stat-label">✅ Recommended</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-card"><div class="stat-number" style="color:#ffcc00">{maybe}</div><div class="stat-label">⚠️ Maybe</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="stat-card"><div class="stat-number" style="color:#fc8181">{no}</div><div class="stat-label">❌ Not Recommended</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Top candidate
    top = results[0]
    st.markdown(f"""
    <div class="top-card">
        <div>
            <div class="top-label">🏆 Top Candidate</div>
            <div class="top-name">{top['Candidate']}</div>
            <div class="top-skills">🛠 {top['Top Skills']}</div>
        </div>
        <div class="top-score">{top['Match Score (%)']}%</div>
    </div>
    """, unsafe_allow_html=True)

    # Download at top
    st.markdown('<div class="section-header">📥 Export Results</div>', unsafe_allow_html=True)
    df_download = pd.DataFrame([{k: v for k, v in r.items() if k != "color"} for r in results])
    df_download.index = range(1, len(df_download) + 1)
    df_download.index.name = "Rank"
    csv = df_download.to_csv().encode("utf-8")
    st.download_button("⬇️ Download Ranking Report (CSV)", csv, "candidate_ranking_report.csv", "text/csv")

    st.markdown("<br>", unsafe_allow_html=True)

    # Rankings
    st.markdown('<div class="section-header">🏅 Full Rankings</div>', unsafe_allow_html=True)
    for i, r in enumerate(results):
        rank = i + 1
        color = r["color"]
        score = r["Match Score (%)"]
        bar_width = min(score, 100)

        if rank == 1: rank_icon, rank_class = "🥇", "gold"
        elif rank == 2: rank_icon, rank_class = "🥈", "silver"
        elif rank == 3: rank_icon, rank_class = "🥉", "bronze"
        else: rank_icon, rank_class = f"#{rank}", "other"

        st.markdown(f"""
        <div class="row">
            <div class="rank {rank_class}">{rank_icon}</div>
            <div class="cname">{r['Candidate']}</div>
            <div class="skills">{r['Top Skills']}</div>
            <div class="bar-wrap">
                <div class="bar-bg"><div class="bar-fill {color}" style="width:{bar_width}%"></div></div>
            </div>
            <div class="score {color}">{score}%</div>
            <div class="verdict">{r['Verdict']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
         Crafted with 💜 by <span style="color:#ffcc00;font-weight:700">Vratika Kumawat</span> &nbsp;|&nbsp; AI Internship @ <span style="color:#c084fc;font-weight:700">WeIntern Pvt Ltd</span>
    </div>
    """, unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────────────
st.sidebar.header("⚙️ Configuration")
mode = st.sidebar.radio("Choose Input Mode", ["📊 Use Sample Dataset (CSV)", "📄 Upload PDF Resumes"])

# ─── Job Description ───────────────────────────────────────
st.markdown('<div class="section-header">📝 Job Description</div>', unsafe_allow_html=True)

jd_source = st.radio(
    "Choose Job Description Source:",
    ["📂 Upload JD Dataset (CSV)", "✏️ Write Custom JD"],
    horizontal=True
)

job_description = ""

if jd_source == "📂 Upload JD Dataset (CSV)":
    uploaded_jd = st.file_uploader("Upload your JD CSV file", type=["csv"], key="jd_upload")
    if uploaded_jd:
        df_jd = pd.read_csv(uploaded_jd)
        jd_options = {
            f"{row['Job_ID']} - {row['Role']}": f"""
We are looking for a {row['Role']}.
Required Skills: {row['Required_Skills']}.
Preferred Skills: {row['Preferred_Skills']}.
Experience: {row['Experience']}.
"""
            for _, row in df_jd.iterrows()
        }
        selected_jd = st.selectbox("Select a Job Role to screen against:", list(jd_options.keys()))
        job_description = jd_options[selected_jd]
        st.text_area("Selected Job Description:", value=job_description, height=120, disabled=True)
else:
    job_description = st.text_area(
        "Write your own job description:",
        value="""Looking for a Data Scientist with strong Python skills.
Must have experience in Machine Learning, data analysis, and working with datasets.
Knowledge of Pandas, NumPy, Scikit-learn is required.
SQL knowledge and data visualization experience is a plus.""",
        height=150
    )

st.divider()

# ─── Mode 1: CSV ───────────────────────────────────────────
if mode == "📊 Use Sample Dataset (CSV)":
    st.markdown('<div class="section-header">📊 Resume Dataset</div>', unsafe_allow_html=True)
    uploaded_csv = st.file_uploader("Upload your resume CSV file", type=["csv"], key="resume_upload")

    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)
        st.success(f"✅ {len(df)} candidates loaded successfully!")

        with st.expander("👀 Preview Dataset"):
            st.dataframe(df, use_container_width=True)

        resumes_dict = {}
        for _, row in df.iterrows():
            resume_text = f"""
Name: {row.get("Name", "")}
Education: {row.get("Education", "")}
Skills: {row.get("Skills", "")}
Projects: {row.get("Projects", "")}
Experience: {row.get("Experience", "")}
"""
            resumes_dict[row["Name"]] = resume_text

        if st.button("🚀 Screen Resumes", type="primary"):
            if not job_description.strip():
                st.error("⚠️ Please select or write a job description first!")
            else:
                with st.spinner("🤖 Analyzing resumes with Sentence-BERT..."):
                    results = compute_similarity_sbert(job_description, resumes_dict)
                st.divider()
                display_results(results)

# ─── Mode 2: PDF ───────────────────────────────────────────
elif mode == "📄 Upload PDF Resumes":
    st.markdown('<div class="section-header">📄 PDF Resume Upload</div>', unsafe_allow_html=True)
    uploaded_pdfs = st.file_uploader(
        "Upload resume PDFs",
        type=["pdf"],
        accept_multiple_files=True,
        key="pdf_upload"
    )

    if uploaded_pdfs:
        st.success(f"✅ {len(uploaded_pdfs)} PDF(s) uploaded!")
        resumes_dict = {}
        for pdf in uploaded_pdfs:
            text = extract_text_from_pdf(pdf)
            name = pdf.name.replace(".pdf", "")
            resumes_dict[name] = text
            st.write(f"✅ Extracted: {pdf.name}")

        if st.button("🚀 Screen Resumes", type="primary"):
            if not job_description.strip():
                st.error("⚠️ Please select or write a job description first!")
            else:
                with st.spinner("🤖 Analyzing resumes with Sentence-BERT..."):
                    results = compute_similarity_sbert(job_description, resumes_dict)
                st.divider()
                display_results(results)
