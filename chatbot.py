def get_bot_response(user_input):
    """The 'Brain' of the chatbot using if-elif logic."""
    # Convert input to lowercase so 'Hello' and 'hello' both work
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Greetings! How can I help you today?"
    
    elif "your name" in user_input:
        return "I am Gemini-Lite, a simple rule-based Python bot."
    
    elif "weather" in user_input:
        return "I don't have a window, but I hear it's always 72°F in the cloud!"
    
    elif "help" in user_input:
        return "I can answer questions about my name, the weather, or just say hello."
    
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    
    else:
        return "I'm not sure I understand that. Could you try rephrasing?"

def chat():
    """The 'Interface' using a loop and input/output."""
    print("--- Chatbot Active (Type 'quit' or 'bye' to exit) ---")
    
    while True:
        user_text = input("You: ")
        
        # Exit condition
        if user_text.lower() in ["quit", "bye", "exit"]:
            print("Bot: Goodbye! Have a great day.")
            break
        
        # Get response from our function
        response = get_bot_response(user_text)
        print(f"Bot: {response}")

# Run the program
if __name__ == "__main__":
    chat()