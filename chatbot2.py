# Project: Conversational Agent at a Contact Centre
# Console-based Python chatbot for Checkpoint 2

# Sample intents and responses
intent_responses = {
    "greeting": ["Hello! How can I assist you today?"],
    "hours": ["Our contact center is open from 9 AM to 6 PM, Monday to Saturday."],
    "billing": ["Please provide your billing ID so I can assist you further."],
    "complaint": ["I'm sorry to hear that. Could you please describe the issue?"],
    "callback": ["Sure, please share your phone number and preferred time."],
    "product": ["We offer broadband, mobile, and cable TV services."],
    "location": ["Our office is located in Hyderabad, near the Tech Park."],
    "feedback": ["We appreciate your feedback. Please type your message."],
    "fallback": ["I'm sorry, I didn't quite understand that. Can you please rephrase?"]
}

# Rule-based intent detection
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
    elif any(kw in message for kw in ["product", "services", "plans"]):
        return "product"
    elif any(kw in message for kw in ["location", "address", "where"]):
        return "location"
    elif any(kw in message for kw in ["feedback", "suggestion", "review"]):
        return "feedback"
    else:
        return "fallback"

# Chat loop with logging and query count
query_count = 0
print("Welcome to the Contact Centre Chatbot. Type 'exit' to end.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "quit"]:
        print(f"Chatbot: Thank you for chatting with us. You asked {query_count} questions. Goodbye!")
        break

    intent = detect_intent(user_message)
    response = intent_responses.get(intent, intent_responses["fallback"])
    print(f"Chatbot: {response[0]}")

    query_count += 1

    # Log the conversation to a file
    with open("chat_log.txt", "a") as log:
        log.write(f"User: {user_message}\n")
        log.write(f"Bot: {response[0]}\n\n")
