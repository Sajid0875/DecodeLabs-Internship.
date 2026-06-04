# Rule-Based AI Chatbot

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    

    if user_input in ["hello", "hi", "hey"]:
        print("🤖 Chatbot: Hello! How can I help you?")
        print ("you can say "
              "hello, hi, hey, how are you, what is your name, bye, exit, quit")
    
    elif user_input == "how are you":
        print("🤖 Chatbot: I'm doing great! Thanks for asking.")
        print ("you can say "
              "hello, hi, hey, how are you, what is your name, bye, exit, quit")
    
    elif user_input == "what is your name":
        print("🤖 Chatbot: I am a simple rule-based chatbot.")
        print ("you can say "
              "hello, hi, hey, how are you, what is your name, bye, exit, quit")

    elif user_input in ["bye", "exit", "quit"]:
        print("🤖 Chatbot: Goodbye! Have a nice day.")
        break
    
    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")
        print ("you can say "
              "hello, hi, hey, how are you, what is your name, bye, exit, quit")
