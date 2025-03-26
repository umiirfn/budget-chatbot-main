
print("💬 BudgetBot (Basic): Hey! Let’s talk money. Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower()

    if any(word in user_input for word in ["exit", "bye", "quit"]):
        print("BudgetBot: Catch you later! 👋")
        break

    elif any(word in user_input for word in ["broke", "skint", "struggling", "overdraft"]):
        print("BudgetBot: Totally get that — want to look at your recent spending? 🧐")

    elif any(word in user_input for word in ["spend", "spent", "expenses"]):
        print("BudgetBot: You’ve had a few outgoing payments lately 💸 Want a summary breakdown?")

    elif any(word in user_input for word in ["afford", "takeaway", "can i buy"]):
        print("BudgetBot: Let’s check if this fits your budget first 🍔🧮")

    else:
        print("BudgetBot: I’m listening — tell me more 💬")
