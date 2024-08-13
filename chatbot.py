from datetime import datetime

def chatbot_response(user_input):
    # Convert the input to lowercase to handle case insensitivity
    user_input = user_input.lower()

    # Basic responses based on predefined rules
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here and ready to help you!"
    elif "what is your name" in user_input:
        return "I am a chatbot created to help you with simple queries."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what time is it" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "what is the date" in user_input:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."
    elif "what is the weather" in user_input:
        return "I can't check the weather right now, but you can use a weather app for current conditions."
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "what is your favorite color" in user_input:
        return "I don't have preferences, but I think blue is a nice color!"
    elif "how old are you" in user_input:
        return "I'm a bot, so I don't age. But I've been here to help for as long as you need!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
