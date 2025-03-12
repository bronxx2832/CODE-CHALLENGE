def get_bot_response(user_message):
    responses = {
        "hello": "Hi there! How can I help you?",
        "tell me about paris": "Paris is the capital of France, known for its culture, art, and the Eiffel Tower.",
        "tell me about tokyo": "Tokyo is Japan's capital, famous for its technology, food, and anime culture.",
        "bye": "Goodbye! Have a great day!",
    }

    return responses.get(user_message, "I'm not sure how to respond to that.")

def main():
    print("Welcome! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        response = get_bot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
