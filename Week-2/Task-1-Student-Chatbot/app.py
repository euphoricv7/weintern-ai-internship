from flask import Flask, render_template, request, jsonify, session
from chatbot import preprocess, match_intent, build_lookup, load_intents
from google import genai
import datetime

app = Flask(__name__)
app.secret_key = "student_success_secret_key"

LOG_FILE = "chat_log.txt"

GEMINI_API_KEY = "your_actual_key_here"
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

intents_data = load_intents("intents.json")
lookup = build_lookup(intents_data)

STUDENT_SYSTEM_PROMPT = """You are a friendly Student Success Assistant for Indian college students.

You help with:
- Career guidance after B.Tech
- Internship finding and tips
- Placement preparation
- Learning resources (Python, DSA, AI/ML, Web Dev)
- LinkedIn and communication tips
- Motivation and student struggles
- Any other student related question

Response style:
- Be warm and encouraging like a helpful senior
- Keep responses under 150 words
- Use dashes for bullet points, not asterisks
- Always include one actionable tip"""

def get_gemini_response(user_message: str, conversation_history: list) -> str:
    try:
        history_text = ""
        if conversation_history:
            history_text = "Previous conversation:\n"
            for msg in conversation_history[-4:]:
                history_text += f"{msg['role']}: {msg['text']}\n"
            history_text += "\n"

        prompt = f"{STUDENT_SYSTEM_PROMPT}\n\n{history_text}Student: {user_message}"

        response = gemini_client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return "I'm having a little trouble right now. Please try again in a moment!"

def log_message(speaker: str, message: str):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {speaker}: {message}\n")

def start_session_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*55}\n")
        f.write(f"  WEB SESSION STARTED: {timestamp}\n")
        f.write(f"{'='*55}\n")

start_session_log()

@app.route("/")
def home():
    session.clear()
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.form.get("msg", "").strip()

    if not user_input:
        return jsonify({"response": "Could you say a bit more? I want to give you the best help I can!"})

    # Step 1 — NLTK preprocessing
    tokens = preprocess(user_input)

    # Step 2 — Try rule-based intent matching
    last_tag = session.get("last_tag", None)
    history = session.get("history", [])

    matched_response = None
    matched_tag = None

    if tokens:
        matched_response, matched_tag = match_intent(tokens, lookup, intents_data, last_tag)

    # Step 3 — If intent matched confidently, use it
    if matched_tag is not None:
        response = matched_response
        session["last_tag"] = matched_tag
    else:
        # Step 4 — Fallback to Gemini
        response = get_gemini_response(user_input, history)

    # Update history
    history.append({"role": "Student", "text": user_input})
    history.append({"role": "Assistant", "text": response})
    if len(history) > 10:
        history = history[-10:]
    session["history"] = history

    log_message("You", user_input)
    log_message("Bot", response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
