# Project: Conversational Agent at a Contact Centre
# Console-based Python chatbot without Flask or web backend

# Sample intents and responses
intent_responses = {
    "greeting": ["Hello! How can I assist you today?"],
    "hours": ["Our contact center is open from 9 AM to 6 PM, Monday to Saturday."],
    "billing": ["Please provide your billing ID so I can assist you further."],
    "complaint": ["I'm sorry to hear that. Could you please describe the issue?"],
    "callback": ["Sure, please share your phone number and preferred time."],
    "fallback": ["I'm sorry, I didn't quite understand that. Can you please rephrase?"]
}

# Simple rule-based intent detection
def detect_intent(message):
    message = message.lower()
    if any(kw in message for kw in ["hello", "hi", "hey"]):
        return "greeting"
    elif any(kw in message for kw in ["hours", "open", "timing"]):
        return "hours"
    elif any(kw in message for kw in ["bill", "charge", "payment"]):
        return "billing"
    elif any(kw in message for kw in ["complain", "problem", "issue"]):
        return "complaint"
    elif any(kw in message for kw in ["call back", "phone call", "callback"]):
        return "callback"
    else:
        return "fallback"

# Chat loop
print("Welcome to the Contact Centre Chatbot. Type 'exit' to end.")
while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "quit"]:
        print("Chatbot: Thank you for chatting with us. Goodbye!")
        break
    intent = detect_intent(user_message)
    response = intent_responses.get(intent, intent_responses["fallback"])
    print(f"Chatbot: {response[0]}")
