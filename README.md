<<<<<<< HEAD
# Campus Care AI 🌿 - Mental Health Support Portal

A comprehensive, multi-page web application demonstrating an AI-powered, non-clinical mental health support assistant designed for campus environments. Recently upgraded to feature a premium dark-themed, glassmorphism UI.

## ✨ Features
- **AI Chat Support:** Empathetic, real-time conversational interface powered by Google's `gemini-flash-lite-latest` model.
- **Wellness Tools:** Interactive "Box Breathing" exercises and grounding techniques for immediate stress relief.
- **Emergency Helplines:** A dedicated directory of national emergency numbers and campus-specific resources.
- **Maps & Ambulance Locator:** Quick-dial buttons for EMS and simulated maps for nearby student health centers.
- **Crisis Detection:** Hardcoded keyword detection (e.g., "suicide", "hurt myself") immediately bypasses the AI and outputs emergency contact information.
- **Strict Privacy:** Completely stateless sessions. No logins, no tracking, and no databases.

## 🛠️ Technology Stack
- **Frontend:** HTML5, CSS3 (Premium Dark Theme, Glassmorphism, CSS Animations), Vanilla JavaScript
- **Backend:** Python (Flask)
- **AI/NLP:** Google Generative AI SDK, NLTK (VADER Sentiment Analysis Fallback)

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+ installed
- A Google Gemini API Key

### Installation Steps

1. **Clone/Download the repository:**
   Navigate to the project folder in your terminal.

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   
   # Activate on Windows:
   venv\Scripts\activate
   
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Rename the `.env.example` file to `.env` (or create a new `.env` file in the root directory) and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

5. **Run the Application:**
   ```bash
   python app.py
   ```

6. **Access the App:**
   Open your web browser and go to `http://127.0.0.1:5000`

## 🛡️ Ethical Safeguards
- **Disclaimer:** Prominently displayed on multiple pages to inform users the AI is not a medical professional.
- **Data Protection:** Chat sessions exist only in your browser session memory. Refreshing or closing the tab permanently deletes the conversation.
- **Emergency Priority:** The app is designed to route users to professional human help (counselors, EMS) as quickly as possible during a crisis.
=======
# Mental-Health-AI
>>>>>>> 0c37b7374b37aec67d2349ada8b16d29e367b9a1
