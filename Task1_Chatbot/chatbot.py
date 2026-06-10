print("ChatBot: Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("ChatBot: Hi! How can I help you?")

    elif user == "how are you":
        print("ChatBot: I am fine. Thank you!")

    elif user == "what is your name":
        print("ChatBot: My name is CodSoft Bot.")

    elif user == "who created you":
        print("ChatBot: I was created by Bala Karthik.")

    elif user == "college":
        print("ChatBot: I am studying AI internship.")

    elif user == "bye":
        print("ChatBot: Goodbye! Have a great day.")
        break

    else:
        print("ChatBot: Sorry, I don't understand.")
    
