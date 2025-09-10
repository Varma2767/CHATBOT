PyBot 🤖

A simple rule-based chatbot built in Python with basic learning, memory, and conversation history features. PyBot can handle greetings, questions, fallback responses, and even learn new replies from user input. It’s a beginner-friendly project to explore Python, regex, and basic AI concepts without needing machine learning models.

✨ Features

👋 Greets and responds to common phrases

📚 Learns new responses (teach using learn:question|response)

📝 Remembers your name during the chat

💾 Saves & loads conversations (save command)

📊 Conversation summary (summary command)

🔄 Fallback responses when no match is found

🛠️ Tech Stack

Python 3.x

Built with core libraries:

re → Regex pattern matching

json → Save/load conversations

datetime → Timestamps

random → Randomized responses

🚀 How to Run

Clone this repository:

git clone https://github.com/your-username/PyBot.git
cd PyBot


Run the chatbot:

python chatbot.py

💡 Usage

When you start PyBot, try:

Greet it → hello / hi

Ask questions → what is your name? / how are you?

Teach new response →

learn:how is life?|Life is great, thanks for asking!  


See conversation summary → type summary

Save chat history → type save

Exit chatbot → type quit / exit / bye

📂 Example Chat
🤖 PyBot: Hello! I'm your AI chatbot. Type 'quit', 'exit', or 'bye' to end our conversation.  

You: hi  
🤖 PyBot: Hello! How can I help you today?  

You: my name is Alex  
🤖 PyBot: Nice to meet you, Alex! I'll remember your name.  

You: summary  
📊 Conversation Summary:  
   - Total exchanges: 3  
   - Your name: Alex  
   - Learned responses: 0  
   - Started: 2025-09-10 20:55:32  

🔮 Future Improvements

Add GUI (Tkinter/Streamlit)

Connect with APIs (Weather, News, etc.)

Improve memory for long conversations

Expand response patterns

👨‍💻 Author

Developed by Sandeep Datla
