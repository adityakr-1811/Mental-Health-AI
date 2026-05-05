# Demo Script (3-5 Minutes)

**Title:** AI Mental Health Support Assistant Demo
**Target Audience:** Project Evaluators / Peers

---

### [0:00 - 1:00] Introduction & UI Overview
**Speaker:** 
"Hello everyone. Our project is the 'AI Mental Health Support Assistant', designed specifically for a campus environment. 
As you can see on the screen, we focused on a clean, calming UI. 
Notice the persistent disclaimer at the top: we explicitly state that this AI is not a medical professional and that all sessions are completely anonymous—we do not use a database to store any user data."

*Action: Point out the disclaimer and the 'Quick Campus Resources' panel.*

### [1:00 - 2:00] Standard Interaction & Sentiment Analysis
**Speaker:**
"Let's simulate a standard interaction. I'll type: *'I'm feeling a bit overwhelmed with my upcoming midterms.'*"

*Action: Type the message and send.*

**Speaker:**
"Behind the scenes, our Python Flask backend uses NLTK's VADER sentiment analysis to read this input. It detects a negative sentiment and stress keywords. 
As you can see, the AI responds empathetically, acknowledging the academic stress and gently suggesting that the user might want to reach out to the campus counselor, providing the specific phone number."

### [2:00 - 3:00] The Fallback/Rule-Based System
**Speaker:**
"We built this system to be robust. If our main generative AI model goes offline or if we run out of API quota, the system doesn't break. It falls back on a rule-based NLP approach that can still provide structured, supportive responses based on the sentiment score."

*Action: Type a positive message like: "I finally finished my assignment!" and show the positive acknowledgment.*

### [3:00 - 4:00] Ethical Safeguards & Crisis Detection (Crucial Step)
**Speaker:**
"Now, the most important feature of our project is the Ethical Safeguard. An AI should never try to handle a genuine crisis. 
Watch what happens if I type something alarming, like: *'I want to hurt myself.'*"

*Action: Type "I want to hurt myself" and send.*

**Speaker:**
"Notice how the response is completely different and instantaneous. Our backend uses a regex interception system. Before the AI even sees the message, the system catches the severe distress keyword and immediately overrides the AI to output a hardcoded Emergency Alert block with national helplines and emergency campus contacts. This ensures the highest level of safety for the user."

### [4:00 - 5:00] Conclusion
**Speaker:**
"In conclusion, we've built a functional, stateless, and ethically sound AI assistant that provides immediate emotional support while ensuring that students in actual crisis are immediately directed to human professionals. Thank you."
