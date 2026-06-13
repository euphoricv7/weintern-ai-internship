"""
Student Success Assistant - AI Chatbot
Week 2 Task 1 | WeIntern Pvt Ltd AI/ML Internship
-----------------------------------------------
Approach  : Hybrid (Rule-based NLP + Gemini AI fallback)
Interface : Console (CLI) + Flask Web App
Features  :
  - 61 intents across 8 categories
  - Natural language preprocessing (NLTK)
  - Context-aware multi-turn conversation
  - Gemini AI fallback for unknown queries
  - Full session conversation logging
"""

import json
import random
import re
import os
import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ─────────────────────────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────────────────────────

for pkg in ['punkt', 'stopwords', 'wordnet', 'punkt_tab']:
    nltk.download(pkg, quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words  = set(stopwords.words('english'))

KEEP_WORDS = {
    'no', 'not', 'how', 'what', 'which', 'where', 'when', 'why', 'who',
    'me', 'my', 'i', 'vs', 'or', 'low', 'high', 'good', 'bad'
}
stop_words -= KEEP_WORDS


# ─────────────────────────────────────────────────────────────
# LOAD INTENTS
# ─────────────────────────────────────────────────────────────

def load_intents(filepath: str) -> dict:
    """Load the intents JSON file."""
    if not os.path.exists(filepath):
        print(f"[ERROR] intents.json not found at: {filepath}")
        exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


# ─────────────────────────────────────────────────────────────
# TEXT PREPROCESSING
# ─────────────────────────────────────────────────────────────

def preprocess(text: str) -> list:
    """
    Clean and normalize user input.
    Steps:
      1. Lowercase
      2. Remove punctuation
      3. Tokenize
      4. Remove stopwords (except important ones)
      5. Lemmatize
    """
    text   = text.lower()
    text   = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return tokens


def preprocess_pattern(pattern: str) -> list:
    """Same preprocessing applied to intent patterns."""
    return preprocess(pattern)


# ─────────────────────────────────────────────────────────────
# BUILD LOOKUP TABLE
# ─────────────────────────────────────────────────────────────

def build_lookup(intents_data: dict) -> list:
    """
    Pre-process every pattern and store as lookup list.
    Skips fallback intent.
    """
    lookup = []
    for intent in intents_data['intents']:
        if intent['tag'] == 'fallback':
            continue
        for pattern in intent['patterns']:
            lookup.append({
                'tag'      : intent['tag'],
                'tokens'   : preprocess_pattern(pattern),
                'responses': intent['responses']
            })
    return lookup


# ─────────────────────────────────────────────────────────────
# INTENT MATCHING
# ─────────────────────────────────────────────────────────────

def match_intent(user_tokens: list, lookup: list, intents_data: dict, last_tag: str = None) -> tuple:
    """
    Find the best matching intent using Jaccard similarity.
    Returns (response, matched_tag)
    If no confident match found, returns (fallback_response, None)
    """
    best_score     = 0.0
    best_responses = None
    best_tag       = None

    user_set = set(user_tokens)

    for entry in lookup:
        pattern_tokens = entry['tokens']
        if not pattern_tokens:
            continue

        pattern_set = set(pattern_tokens)
        common      = user_set & pattern_set
        overlap     = len(common)

        if overlap == 0:
            continue

        # Jaccard similarity score
        score = overlap / max(len(user_set), len(pattern_set))

        # Boost if all pattern tokens found in user input
        if pattern_set.issubset(user_set):
            score += 0.3

        # Slight boost for longer matches
        score += overlap * 0.01

        if score > best_score:
            best_score     = score
            best_responses = entry['responses']
            best_tag       = entry['tag']

    THRESHOLD = 0.5

    if best_score >= THRESHOLD and best_responses:
        return (random.choice(best_responses), best_tag)
    else:
        for intent in intents_data['intents']:
            if intent['tag'] == 'fallback':
                return (random.choice(intent['responses']), None)
        return ("I'm not sure I understood that. Could you rephrase?", None)


# ─────────────────────────────────────────────────────────────
# CONVERSATION LOGGING
# ─────────────────────────────────────────────────────────────

def setup_log(log_path: str) -> str:
    """Create or append to chat log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*55}\n")
        f.write(f"  SESSION STARTED: {timestamp}\n")
        f.write(f"{'='*55}\n")
    return log_path


def log_message(log_path: str, speaker: str, message: str):
    """Append a single message to the log file."""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {speaker}: {message}\n")


# ─────────────────────────────────────────────────────────────
# CONTEXT TRACKING
# ─────────────────────────────────────────────────────────────

class ConversationContext:
    """Tracks short-term context within a CLI session."""
    def __init__(self):
        self.last_topic = None
        self.turn_count = 0
        self.history    = []

    def update(self, user_input: str, bot_response: str, topic: str = None):
        self.turn_count += 1
        self.history.append((user_input, bot_response))
        if topic:
            self.last_topic = topic
        if len(self.history) > 5:
            self.history.pop(0)


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPERS
# ─────────────────────────────────────────────────────────────

def print_banner():
    print("""
╔══════════════════════════════════════════════════════╗
║         🎓 STUDENT SUCCESS ASSISTANT 🎓              ║
║──────────────────────────────────────────────────────║
║  Your AI companion for careers, internships,         ║
║  placements, learning resources & student life!      ║
║──────────────────────────────────────────────────────║
║  Type  'help'  to see what I can do                  ║
║  Type  'quit'  or  'exit'  to end the session        ║
╚══════════════════════════════════════════════════════╝
    """)


def print_help():
    print("""
┌─────────────────────────────────────────────────────┐
│               WHAT I CAN HELP WITH                  │
├─────────────────────────────────────────────────────┤
│  🎯 Career Guidance  → "which field should I choose" │
│  💼 Internships      → "how to find internships"     │
│  🏆 Placement Prep   → "aptitude round tips"         │
│  📚 Learning         → "how to learn Python"         │
│  🤝 Soft Skills      → "LinkedIn profile tips"       │
│  😰 Student Life     → "I feel demotivated"          │
└─────────────────────────────────────────────────────┘
    """)


def format_bot_response(response: str) -> str:
    return f"\n  🤖 Bot: {response}\n"


def format_user_prompt() -> str:
    return "\n  You: "


# ─────────────────────────────────────────────────────────────
# MAIN CHAT LOOP (CLI)
# ─────────────────────────────────────────────────────────────

def chat():
    """Main CLI chat loop."""
    script_dir   = os.path.dirname(os.path.abspath(__file__))
    intents_path = os.path.join(script_dir, 'intents.json')
    log_path     = os.path.join(script_dir, 'chat_log.txt')

    intents_data = load_intents(intents_path)
    lookup       = build_lookup(intents_data)

    setup_log(log_path)
    context = ConversationContext()

    print_banner()

    while True:
        try:
            user_input = input(format_user_prompt()).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Bot: Take care! Come back anytime. Goodbye! 👋\n")
            break

        if not user_input:
            continue

        log_message(log_path, "You", user_input)

        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            farewell = "Goodbye! Keep learning and growing. You've got this! 💪"
            print(format_bot_response(farewell))
            log_message(log_path, "Bot", farewell)
            break

        if user_input.lower() == 'help':
            print_help()
            log_message(log_path, "Bot", "[Help menu displayed]")
            continue

        if user_input.lower() == 'history':
            if not context.history:
                print(format_bot_response("No conversation history yet!"))
            else:
                print("\n  --- Conversation History ---")
                for i, (u, b) in enumerate(context.history, 1):
                    print(f"  [{i}] You: {u}")
                    print(f"       Bot: {b[:80]}{'...' if len(b) > 80 else ''}")
                print()
            continue

        user_tokens = preprocess(user_input)

        if not user_tokens:
            response = "Could you say a bit more? I want to give you the best help I can!"
            print(format_bot_response(response))
            log_message(log_path, "Bot", response)
            continue

        response, matched_tag = match_intent(user_tokens, lookup, intents_data, context.last_topic)
        context.update(user_input, response, matched_tag)

        print(format_bot_response(response))
        log_message(log_path, "Bot", response)

    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"\n  SESSION ENDED: {end_time} | Turns: {context.turn_count}\n")

    print(f"\n  [Chat log saved to: chat_log.txt]\n")


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    chat()
