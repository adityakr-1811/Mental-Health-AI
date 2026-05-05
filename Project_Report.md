# Final Project Report: AI Mental Health Support Assistant

**Academic Year:** 2024-2028  
**Project Level:** B.Tech 2nd Year  

---

## 1. Abstract
The "AI Mental Health Support Assistant" is a web-based application designed to provide immediate, non-clinical emotional support to college students. Utilizing Natural Language Processing (NLP) and sentiment analysis, the system engages users in empathetic conversation, detects varying levels of stress, and identifies severe distress. Crucially, the project incorporates strict ethical safeguards, prioritizing user privacy and implementing immediate routing to professional helplines when crisis keywords are detected.

## 2. Introduction
College students frequently experience high levels of stress, anxiety, and academic pressure. While professional counseling is essential, there is often a barrier to seeking immediate, preliminary support. This project aims to bridge that gap by providing an accessible, anonymous, 24/7 AI-driven chat interface. It acts as a supportive listener and a bridge to actual campus resources.

## 3. Objectives
1. **Conversational Support:** Develop an AI that can understand and respond empathetically to student concerns.
2. **Stress Detection:** Implement sentiment analysis to gauge the user's emotional state and provide context-aware suggestions (e.g., relaxation tips).
3. **Resource Routing:** Actively suggest campus-specific resources when high stress is detected.
4. **Ethical Compliance:** Ensure the system does not provide medical advice and protects user anonymity.

## 4. Methodology
The project employs a client-server architecture:
- **Frontend:** Built with HTML, CSS, and JavaScript. It provides a clean, calming UI and handles user input asynchronously.
- **Backend:** Powered by Python and Flask. It serves the web pages and processes API requests from the frontend.
- **NLP Engine:** Utilizes the Natural Language Toolkit (NLTK) and specifically the VADER lexicon for sentiment intensity analysis. 
- **AI Generation:** Integrates with generative AI models (like Google Gemini) to formulate dynamic responses, with a robust fallback system using predefined rules if API access is unavailable.

## 5. Implementation Details
- **Crisis Keyword Interception:** Before any text is processed by the AI or sentiment analyzer, it is checked against a regex-based list of severe distress words (e.g., "harm", "suicide"). If matched, an immediate, hardcoded response containing emergency contact numbers is returned.
- **Sentiment Scoring:** `nltk.sentiment.vader` assigns a compound score from -1.0 (highly negative) to +1.0 (highly positive). Scores below -0.5 trigger supportive, probing responses, while positive scores acknowledge good emotional states.
- **Stateless Architecture:** The Flask backend does not connect to a database. Once the HTTP request is resolved, the data is discarded, ensuring complete anonymity.

## 6. Ethical Considerations
Ethics are the foundation of this project:
- **No Medical Advice:** A persistent disclaimer warns users that the AI is not a therapist.
- **Data Privacy:** Zero data retention policy.
- **Fail-Safe Mechanism:** The hardcoded crisis response ensures that the AI cannot accidentally generate an inappropriate response to a life-threatening input.

## 7. Conclusion
The AI Mental Health Support Assistant successfully demonstrates how basic AI and NLP techniques can be applied to create a helpful, ethical tool for student well-being. It serves as a proof-of-concept that technology can offer preliminary emotional support while responsibly directing users to professional human care when necessary.
