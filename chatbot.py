def chatbot_response(user):
    if user == "hello":
        return "Hi! How are you?"

    elif user == "how are you":
        return "I am fine! Thanks for asking."

    elif user == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand."


print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    response = chatbot_response(user)
    print("Chatbot:", response)

    if user == "bye":
        break