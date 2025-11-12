import random

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "your name" in user_input:
        return "I’m your AI Chatbot 🤖"
    elif "how are you" in user_input:
        return "I’m just a bot, but I’m doing great! What about you?"
    elif "ai" in user_input:
        return "AI means Artificial Intelligence — making machines smart like humans!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        responses = [
            "That's interesting! Tell me more...",
            "Hmm, I’m not sure about that.",
            "Can you explain it a bit more?",
            "I’ll try to find that out someday!"
        ]
        return random.choice(responses)

