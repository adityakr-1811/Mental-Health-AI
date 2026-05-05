document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const typingIndicator = document.getElementById('typing-indicator');
    
    let chatHistory = [];

    // Make marked open links in new tab
    const renderer = new marked.Renderer();
    renderer.link = function(href, title, text) {
        return `<a target="_blank" rel="noopener noreferrer" href="${href}" title="${title || ''}">${text}</a>`;
    };
    marked.setOptions({ renderer: renderer });

    function addMessage(text, isUser, isCrisis = false) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message');
        
        if (isUser) {
            msgDiv.classList.add('user-message');
            msgDiv.textContent = text; // user text is plain
        } else {
            msgDiv.classList.add('ai-message');
            if (isCrisis) {
                msgDiv.classList.add('crisis-message');
            }
            // Parse markdown for AI responses
            msgDiv.innerHTML = marked.parse(text);
        }
        
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;

        // Add user message to UI
        addMessage(text, true);
        userInput.value = '';
        
        // Show typing indicator
        typingIndicator.style.display = 'block';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: text, history: chatHistory }),
            });

            const data = await response.json();
            
            // Hide typing indicator
            typingIndicator.style.display = 'none';

            // Add AI message to UI
            addMessage(data.response, false, data.crisis);
            
            // Update history
            chatHistory.push({ role: 'user', content: text });
            chatHistory.push({ role: 'assistant', content: data.response });
            
            // Log sentiment to console for demo purposes (hidden from user)
            console.log(`Sentiment Score: ${data.sentiment}, Crisis Detected: ${data.crisis}`);

        } catch (error) {
            console.error('Error:', error);
            typingIndicator.style.display = 'none';
            addMessage("I'm sorry, I'm having trouble connecting right now. Please try again later. If you are in crisis, please call 112 immediately.", false, true);
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});
