import os
import re
from flask import Flask, request, jsonify, render_template
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import google.generativeai as genai


# Initialize Flask App
app = Flask(__name__)

# Ensure NLTK resources are downloaded
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

# Configure Gemini API if available
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("ALL ENV:", dict(os.environ))
print("GEMINI_API_KEY:", os.environ.get("GEMINI_API_KEY"))

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-flash-lite-latest')
else:
    model = None

# ---- CRITICAL ETHICAL SAFEGUARDS ----
# Crisis keywords that trigger immediate hardcoded responses
CRISIS_KEYWORDS = [
    r'\bsuicide\b', r'\bkill myself\b', r'\bdie\b', r'\bharm myself\b', 
    r'\bend it all\b', r'\bhurt myself\b', r'\bgive up\b'
]

CRISIS_RESPONSE = (
    "🚨 **CRITICAL ALERT** 🚨\n\n"
    "It sounds like you are going through a very difficult time. "
    "Please know that you are not alone and there is help available right now.\n\n"
    "**Please reach out immediately:**\n"
    "📞 **National Emergency Number:** 112\n"
    "📞 **AASRA Helpline:** 9820466726\n"
    "💬 **Vandrevala Foundation WhatsApp:** +91 9999 666 555\n"
    "🏥 **Campus Counselor (Emergency):** +91 98765 43210\n\n"
    "This AI cannot provide medical help. Please talk to a professional who can support you."
)

# Stress keywords
STRESS_KEYWORDS = [r'\banxious\b', r'\bpanic\b', r'\bexam\b', r'\bfail\b', r'\boverwhelmed\b', r'\bstressed\b']

# Disclaimer
DISCLAIMER = "Disclaimer: This AI assistant is not a medical professional. It provides non-clinical emotional support only."

def detect_crisis(text):
    text_lower = text.lower()
    for pattern in CRISIS_KEYWORDS:
        if re.search(pattern, text_lower):
            return True
    return False

def get_sentiment(text):
    scores = sia.polarity_scores(text)
    return scores['compound']

def get_fallback_response(text, sentiment_score):
    """Fallback response if no API key is provided."""
    text_lower = text.lower()
    
    # Check for stress keywords
    for pattern in STRESS_KEYWORDS:
        if re.search(pattern, text_lower):
            return (
                "I hear that you're feeling stressed, possibly about academics or life. "
                "It's completely normal to feel overwhelmed. Remember to take deep breaths. "
                "You might find it helpful to speak with our Campus Counselor at 555-0199 or "
                "visit the Student Wellness Center."
            )
            
    if sentiment_score < -0.5:
        return "[Offline Mode - API Key Missing] I'm really sorry you're feeling this way. Have you considered talking to a trusted friend or the campus counselor?"
    elif sentiment_score > 0.5:
        return "[Offline Mode - API Key Missing] That sounds wonderful! I'm glad to hear things are going well."
    else:
        return "[Offline Mode - API Key Missing] I understand. College life can be a mix of emotions. (Note: Please set your GEMINI_API_KEY in a .env file to enable dynamic AI responses)."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/helpline')
def helpline():
    return render_template('helpline.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/wellness')
def wellness():
    return render_template('wellness.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    history = request.json.get('history', [])
    
    if not user_message:
        return jsonify({'response': "Please say something.", 'sentiment': 0, 'crisis': False})
        
    # 1. Check for Crisis (Highest Priority).......
    if detect_crisis(user_message):
        return jsonify({
            'response': CRISIS_RESPONSE,
            'sentiment': -1.0,
            'crisis': True
        })
        
    # 2. Analyze Sentiment
    sentiment_score = get_sentiment(user_message)
    
    # 3. Generate Response
    ai_response = ""
    try:
        if model:
            # Construct a prompt with context
            prompt = f"""
            You are a compassionate, empathetic, and non-clinical AI Mental Health Support Assistant for college students.
            Do not provide medical diagnoses or advice. Simply listen and offer emotional support.
            If the user mentions high stress, suggest college resources like the Campus Counselor (555-0199).
            """
            
            if history:
                prompt += "\nPrevious conversation:\n"
                for msg in history[-10:]:  # Keep last 10 messages for context
                    role = "User" if msg.get("role") == "user" else "Assistant"
                    prompt += f"{role}: {msg.get('content')}\n"
            
            prompt += f'\nUser message: "{user_message}"\nAssistant:'
            
            response = model.generate_content(prompt)
            ai_response = response.text
        else:
            # Fallback if no API key
            ai_response = get_fallback_response(user_message, sentiment_score)
            
    except Exception as e:
        print(f"Error calling AI API: {e}")
        ai_response = get_fallback_response(user_message, sentiment_score)
        
    return jsonify({
        'response': ai_response,
        'sentiment': sentiment_score,
        'crisis': False
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)