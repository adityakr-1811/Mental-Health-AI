# AI Mental Health Support Assistant 🌿

A college project demonstrating an AI-powered, non-clinical mental health support assistant designed for campus environments. 

## 🎯 Objectives
- Provide an empathetic conversational interface.
- Detect stress using sentiment analysis.
- Identify crisis keywords and immediately provide emergency helplines.
- Ensure user privacy (no database, no tracking).

## 🛠️ Technology Stack
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Python (Flask)
- **AI/NLP:** NLTK (VADER Sentiment Analysis), Google Generative AI (Optional/Configurable)
- **Styling:** Custom CSS with modern UI principles.

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+ installed
- pip (Python package manager)

### Installation Steps

1. **Clone/Download the repository:**
   Navigate to the project folder.

2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables (Optional for Generative AI):**
   Create a `.env` file in the root directory and add your Gemini API key if you want to use the generative model instead of the fallback logic:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the Application:**
   ```bash
   python app.py
   ```

6. **Access the App:**
   Open your web browser and go to `http://127.0.0.1:5000`

## 🛡️ Ethical Safeguards
- **Disclaimer:** Prominently displayed to inform users the AI is not a medical professional.
- **Privacy:** Chat sessions are completely stateless.
- **Crisis Detection:** Hardcoded keyword detection (e.g., "suicide", "hurt myself") immediately bypasses the AI and outputs emergency contact information.
