def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue is $345 billion."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has increased by 12% over the last year."
    elif user_query == "What is the total cash flow from operations?":
        return "Cash flow from operations is $76 billion."
    elif user_query == "What is the change in total assets?":
        return "Total assets increased by 5% year over year."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Run interaction
while True:
    user_input = input("Ask a financial question: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    print(simple_chatbot(user_input))
