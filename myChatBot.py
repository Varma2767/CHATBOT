import random
import re
import json
from datetime import datetime
from typing import Dict, List, Tuple

class SimpleChatbot:
    """
    A simple rule-based AI chatbot with learning capabilities
    """
    
    def __init__(self):
        self.name = "PyBot"
        self.conversation_history = []
        self.user_data = {}
        self.response_patterns = self._initialize_patterns()
        self.learning_responses = {}
        
    def _initialize_patterns(self) -> Dict[str, List[str]]:
        """Initialize predefined response patterns"""
        return {
            'greeting': {
                'patterns': [r'hello', r'hi', r'hey', r'good morning', r'good afternoon'],
                'responses': [
                    "Hello! How can I help you today?",
                    "Hi there! What's on your mind?",
                    "Hey! Nice to meet you!",
                    "Hello! I'm PyBot, ready to chat!"
                ]
            },
            'goodbye': {
                'patterns': [r'bye', r'goodbye', r'see you', r'farewell'],
                'responses': [
                    "Goodbye! Have a great day!",
                    "See you later! Take care!",
                    "Bye! It was nice talking with you!",
                    "Farewell! Come back anytime!"
                ]
            },
            'how_are_you': {
                'patterns': [r'how are you', r'how do you feel', r'are you okay'],
                'responses': [
                    "I'm doing well, thank you for asking!",
                    "I'm great! How about you?",
                    "I'm functioning perfectly! How are you?",
                    "All systems running smoothly! What about you?"
                ]
            },
            'name_question': {
                'patterns': [r'what is your name', r'who are you', r'your name'],
                'responses': [
                    f"I'm {self.name}, your AI assistant!",
                    f"My name is {self.name}. What's yours?",
                    f"I go by {self.name}. Nice to meet you!"
                ]
            },
            'age_question': {
                'patterns': [r'how old are you', r'your age', r'age'],
                'responses': [
                    "I was just created, so I'm brand new!",
                    "Age is just a number for an AI like me!",
                    "I exist in the eternal now of computing!"
                ]
            },
            'help': {
                'patterns': [r'help', r'what can you do', r'commands'],
                'responses': [
                    "I can chat with you, remember our conversation, learn from you, and answer questions!",
                    "Try asking me about myself, tell me about you, or just have a normal conversation!",
                    "I'm here to chat! Ask me anything or tell me about your day!"
                ]
            },
            'thanks': {
                'patterns': [r'thank you', r'thanks', r'thx'],
                'responses': [
                    "You're welcome! Happy to help!",
                    "No problem at all!",
                    "Glad I could help!",
                    "Anytime! That's what I'm here for!"
                ]
            },
            'weather': {
                'patterns': [r'weather', r'temperature', r'sunny', r'rain'],
                'responses': [
                    "I wish I could check the weather for you! Try looking outside or checking a weather app.",
                    "I don't have access to current weather data, but I hope it's nice where you are!",
                    "Weather is always interesting to talk about! What's it like outside?"
                ]
            }
        }
    
    def _preprocess_input(self, user_input: str) -> str:
        """Clean and normalize user input"""
        return user_input.lower().strip()
    
    def _find_pattern_match(self, user_input: str) -> Tuple[str, str]:
        """Find matching pattern and return category and response"""
        processed_input = self._preprocess_input(user_input)
        
        for category, data in self.response_patterns.items():
            for pattern in data['patterns']:
                if re.search(pattern, processed_input):
                    response = random.choice(data['responses'])
                    return category, response
        
        return None, None
    
    def _generate_fallback_response(self, user_input: str) -> str:
        """Generate response when no pattern matches"""
        fallback_responses = [
            "That's interesting! Tell me more about that.",
            "I'm not sure I understand completely. Can you elaborate?",
            "Hmm, that's something new for me. What do you think about it?",
            "I'd love to learn more about what you just said!",
            "That's a unique perspective! Can you explain further?",
            f"You mentioned '{user_input}' - that sounds intriguing!",
        ]
        return random.choice(fallback_responses)
    
    def learn_from_user(self, user_input: str, expected_response: str):
        """Allow the bot to learn new responses from user feedback"""
        key = self._preprocess_input(user_input)
        if key not in self.learning_responses:
            self.learning_responses[key] = []
        self.learning_responses[key].append(expected_response)
    
    def _check_learned_responses(self, user_input: str) -> str:
        """Check if we have a learned response for this input"""
        key = self._preprocess_input(user_input)
        if key in self.learning_responses:
            return random.choice(self.learning_responses[key])
        return None
    
    def remember_user_info(self, key: str, value: str):
        """Store information about the user"""
        self.user_data[key] = value
    
    def recall_user_info(self, key: str) -> str:
        """Recall stored information about the user"""
        return self.user_data.get(key, None)
    
    def _extract_user_name(self, user_input: str):
        """Try to extract user's name from input"""
        patterns = [
            r"my name is (\w+)",
            r"i'm (\w+)",
            r"i am (\w+)",
            r"call me (\w+)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                name = match.group(1).capitalize()
                self.remember_user_info('name', name)
                return f"Nice to meet you, {name}! I'll remember your name."
        return None
    
    def get_response(self, user_input: str) -> str:
        """Main method to get chatbot response"""
        if not user_input.strip():
            return "I didn't catch that. Could you say something?"
        
        # Store conversation
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conversation_history.append({
            'timestamp': timestamp,
            'user': user_input,
            'bot_response': None  # Will be filled after generating response
        })
        
        # Check for name extraction
        name_response = self._extract_user_name(user_input)
        if name_response:
            self.conversation_history[-1]['bot_response'] = name_response
            return name_response
        
        # Check learned responses first
        learned_response = self._check_learned_responses(user_input)
        if learned_response:
            self.conversation_history[-1]['bot_response'] = learned_response
            return learned_response
        
        # Check predefined patterns
        category, response = self._find_pattern_match(user_input)
        
        if response:
            # Personalize response if we know the user's name
            user_name = self.recall_user_info('name')
            if user_name and category in ['greeting', 'how_are_you']:
                response = f"{response.split('!')[0]}, {user_name}!"
        else:
            response = self._generate_fallback_response(user_input)
        
        # Store the bot's response
        self.conversation_history[-1]['bot_response'] = response
        return response
    
    def get_conversation_summary(self) -> Dict:
        """Get summary of the conversation"""
        return {
            'total_exchanges': len(self.conversation_history),
            'user_name': self.recall_user_info('name'),
            'learned_responses': len(self.learning_responses),
            'conversation_start': self.conversation_history[0]['timestamp'] if self.conversation_history else None
        }
    
    def save_conversation(self, filename: str = 'chatbot_conversation.json'):
        """Save conversation history to file"""
        data = {
            'conversation_history': self.conversation_history,
            'user_data': self.user_data,
            'learning_responses': self.learning_responses
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Conversation saved to {filename}")
    
    def load_conversation(self, filename: str = 'chatbot_conversation.json'):
        """Load conversation history from file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.conversation_history = data.get('conversation_history', [])
            self.user_data = data.get('user_data', {})
            self.learning_responses = data.get('learning_responses', {})
            print(f"Conversation loaded from {filename}")
        except FileNotFoundError:
            print(f"No saved conversation found at {filename}")

def main():
    """Main function to run the chatbot"""
    chatbot = SimpleChatbot()
    
    print(f"🤖 {chatbot.name}: Hello! I'm your AI chatbot. Type 'quit', 'exit', or 'bye' to end our conversation.")
    print("💡 You can teach me new responses by typing 'learn:' followed by what I should respond to.")
    print("📊 Type 'summary' to see conversation statistics.")
    print("💾 Type 'save' to save our conversation.\n")
    
    # Try to load previous conversation
    chatbot.load_conversation()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit']:
                print(f"🤖 {chatbot.name}: {chatbot.get_response('goodbye')}")
                break
            elif user_input.lower() == 'summary':
                summary = chatbot.get_conversation_summary()
                print(f"📊 Conversation Summary:")
                print(f"   - Total exchanges: {summary['total_exchanges']}")
                print(f"   - Your name: {summary['user_name'] or 'Not provided'}")
                print(f"   - Learned responses: {summary['learned_responses']}")
                print(f"   - Started: {summary['conversation_start'] or 'Just now'}")
                continue
            elif user_input.lower() == 'save':
                chatbot.save_conversation()
                continue
            elif user_input.lower().startswith('learn:'):
                # Teaching mode: learn:question|response
                try:
                    parts = user_input[6:].split('|')
                    if len(parts) == 2:
                        question, response = parts[0].strip(), parts[1].strip()
                        chatbot.learn_from_user(question, response)
                        print(f"🤖 {chatbot.name}: Got it! I learned that when you say '{question}', I should respond with '{response}'")
                    else:
                        print(f"🤖 {chatbot.name}: To teach me, use format: learn:question|response")
                except Exception as e:
                    print(f"🤖 {chatbot.name}: I had trouble learning that. Please try again!")
                continue
            
            # Get and display response
            if user_input:
                response = chatbot.get_response(user_input)
                print(f"🤖 {chatbot.name}: {response}")
            
        except KeyboardInterrupt:
            print(f"\n🤖 {chatbot.name}: Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"🤖 {chatbot.name}: Oops! Something went wrong. Let's keep chatting!")

if __name__ == "__main__":
    main()
