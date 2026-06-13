import streamlit as st
from google import genai
from prompts import get_prompt
import pyperclip

# --- Page Config ---
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✍️",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0d0015 0%, #1a0030 40%, #0d0020 100%);
        min-height: 100vh;
    }

    .hero-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #bf80ff, #ffcc00, #bf80ff);
        background-size: 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s infinite linear;
        margin-bottom: 0.2rem;
    }

    @keyframes shimmer {
        0% { background-position: 0% }
        100% { background-position: 200% }
    }

    .hero-sub {
        text-align: center;
        color: #c084fc;
        font-size: 1rem;
        margin-bottom: 2rem;
        font-weight: 300;
        letter-spacing: 0.05em;
    }

    .card {
        background: rgba(139, 92, 246, 0.08);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(10px);
    }

    .card-title {
        color: #e9d5ff;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .output-card {
        background: rgba(109, 40, 217, 0.1);
        border: 1px solid rgba(167, 139, 250, 0.4);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .output-text {
        color: #f3e8ff;
        font-size: 0.95rem;
        line-height: 1.8;
        white-space: pre-wrap;
    }

    .metric-card {
        background: rgba(139, 92, 246, 0.15);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #ffcc00;
    }

    .metric-label {
        font-size: 0.75rem;
        color: #c084fc;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #7c3aed, #9333ea);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4);
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #6d28d9, #7c3aed);
        box-shadow: 0 6px 25px rgba(124, 58, 237, 0.6);
        transform: translateY(-2px);
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ffcc00, #ff9900);
        color: #1a0030;
        font-size: 1rem;
        padding: 0.75rem 2rem;
        box-shadow: 0 4px 20px rgba(255, 204, 0, 0.4);
    }

    div.stButton > button[kind="primary"]:hover {
        box-shadow: 0 6px 30px rgba(255, 204, 0, 0.6);
        transform: translateY(-2px);
    }

    .stTextInput > div > div > input {
        background: rgba(139, 92, 246, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.4) !important;
        border-radius: 12px !important;
        color: #f3e8ff !important;
        font-family: 'Poppins', sans-serif !important;
    }

    .stTextArea > div > div > textarea {
        background: rgba(139, 92, 246, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.4) !important;
        border-radius: 12px !important;
        color: #f3e8ff !important;
        font-family: 'Poppins', sans-serif !important;
    }

    .stSelectbox > div > div {
        background: rgba(139, 92, 246, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.4) !important;
        border-radius: 12px !important;
        color: #f3e8ff !important;
    }

    label, .stTextInput label, .stTextArea label, .stSelectbox label {
        color: #c084fc !important;
        font-weight: 500 !important;
    }

    .stAlert {
        border-radius: 12px !important;
    }

    .stSpinner > div {
        border-top-color: #7c3aed !important;
    }

    div[data-testid="stDivider"] {
        border-color: rgba(139, 92, 246, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown('<div class="hero-title">✍️ AI Content Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Craft stunning content in seconds, powered by Google Gemini AI</div>', unsafe_allow_html=True)

# --- API Key ---
st.markdown('<div class="card"><div class="card-title">🔑 Authentication</div>', unsafe_allow_html=True)
api_key = st.text_input("Gemini API Key", type="password", placeholder="Paste your Gemini API key here...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# --- Inputs ---
st.markdown('<div class="card"><div class="card-title">⚙️ Configure Your Content</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    content_type = st.selectbox("📄 Content Type", [
        "Blog Post",
        "Social Media Caption",
        "LinkedIn Post",
        "Email Subject Line",
        "Text Summary",
        "YouTube Video Description",
        "Product Description",
        "Tweet Thread",
        "Newsletter Intro"
    ])
with col2:
    tone = st.selectbox("🎭 Tone", [
        "Professional",
        "Casual",
        "Friendly",
        "Persuasive",
        "Humorous",
        "Inspirational",
        "Formal",
        "Storytelling",
        "Minimalist",
        "Empathetic",
        "Bold & Edgy",
        "Poetic"
    ])

topic = st.text_area("💡 Topic or Description", placeholder="e.g. The benefits of waking up early every morning", height=100)
st.markdown('</div>', unsafe_allow_html=True)

# --- Generate Button ---
generate_btn = st.button("🚀 Generate Content", use_container_width=True, type="primary")

# --- Generation Logic ---
if generate_btn:
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not topic.strip():
        st.error("Please enter a topic.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            results = []
            with st.spinner("✨ Crafting 3 variations for you..."):
                for i in range(3):
                    prompt = get_prompt(content_type, topic, tone)
                    response = client.models.generate_content(
                        model="gemini-3.1-flash-lite",
                        contents=prompt
                    )
                    results.append(response.text)

            st.session_state["results"] = results
            st.session_state["content_type"] = content_type
            st.session_state["api_key"] = api_key

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# --- Output ---
if "results" in st.session_state:
    st.markdown('<div class="card-title" style="color:#e9d5ff; margin-top:1.5rem;">📝 Generated Variations</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["✨ Variation 1", "✨ Variation 2", "✨ Variation 3"])

    for i, (tab, result) in enumerate(zip([tab1, tab2, tab3], st.session_state["results"])):
        with tab:
            st.markdown(f'<div class="output-card"><div class="output-text">{result}</div></div>', unsafe_allow_html=True)

            word_count = len(result.split())
            char_count = len(result)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<div class="metric-card"><div class="metric-value">{word_count}</div><div class="metric-label">📊 Words</div></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="metric-card"><div class="metric-value">{char_count}</div><div class="metric-label">🔢 Characters</div></div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(f"📋 Copy Variation {i+1}", use_container_width=True, key=f"copy_{i}"):
                pyperclip.copy(result)
                st.success("Copied to clipboard!")

    # Regenerate all
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Regenerate All Variations", use_container_width=True):
        try:
            client = genai.Client(api_key=st.session_state["api_key"])
            results = []
            with st.spinner("✨ Regenerating all variations..."):
                for i in range(3):
                    prompt = get_prompt(st.session_state["content_type"], topic, tone)
                    response = client.models.generate_content(
                        model="gemini-3.1-flash-lite",
                        contents=prompt
                    )
                    results.append(response.text)
            st.session_state["results"] = results
            st.rerun()
        except Exception as e:
            st.error(f"Something went wrong: {e}")

# --- Footer ---
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 1.5rem; border-top: 1px solid rgba(139, 92, 246, 0.2);">
    <p style="color: #7c3aed; font-size: 0.8rem; font-weight: 500; letter-spacing: 0.1em;">
        Crafted with 💜 by <span style="color: #ffcc00; font-weight: 700;">Vratika Kumawat</span> &nbsp;|&nbsp; AI Internship @ <span style="color: #c084fc; font-weight: 700;">WeIntern Pvt Ltd</span>
    </p>
</div>
""", unsafe_allow_html=True)
