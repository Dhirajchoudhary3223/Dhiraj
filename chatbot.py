# Define a simple chatbot

def get_response(user_input):
    """
    Returns a response based on user input.
    """
    # Predefined responses
    responses = {
        "hello": "Hello! I'm your educational chatbot. How can I assist you today?",
        "what is photosynthesis": (
            "Photosynthesis is the process by which plants use sunlight, water, "
            "and carbon dioxide to produce oxygen and glucose."
        ),
        "what is gravity": (
            "Gravity is the force that attracts objects toward one another. "
            "It was famously explained by Sir Isaac Newton."
        ),
        "what is the capital of france": "The capital of France is Paris.",
        "what is pi": (
            "Pi (π) is a mathematical constant approximately equal to 3.14159. "
            "It represents the ratio of a circle's circumference to its diameter."
        ),
        "goodbye": "Goodbye! Have a great day of learning!",
    }
    
    # Return appropriate response or default message
    return responses.get(user_input.lower(), 
                         "I'm not sure I understand. Can you try rephrasing or asking something else?")

def chatbot():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Educational Chatbot!")
    print("Type 'goodbye' to end the chat.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Exit condition
        if user_input.lower() == "goodbye":
            print("Chatbot: Goodbye! Have a great day of learning!")
            break
        
        # Get chatbot response
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
