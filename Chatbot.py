# Maritime Crew Assistant
# A simple virtual assistant for ship crew safety queries

print("⚓ Maritime Crew Assistant Ready! (type 'exit' to quit)")

# Function to decide what the user is asking about
def get_intent(user_input):
    text = user_input.lower()

    if "fire drill" in text:
        return "fire_drill"
    elif "safety" in text:
        return "safety"
    elif "evacuation" in text:
        return "evacuation"
    elif "exit" in text or "quit" in text:
        return "exit"
    else:
        return "unknown"

# Function to reply based on intent
def respond(intent):
    if intent == "fire_drill":
        return "🚨 A fire drill is a practice to prepare the crew for fire emergencies. Everyone must gather at their muster station."
    elif intent == "safety":
        return "🦺 Safety on board means wearing protective gear, following instructions, and being alert during operations."
    elif intent == "evacuation":
        return "🛟 During evacuation, follow the captain’s instructions, move calmly to lifeboats, and don’t carry luggage."
    elif intent == "exit":
        return "Goodbye! Stay safe at sea. 🌊"
    else:
        return "❓ Sorry, I don’t know that yet. Try asking about fire drills, safety, or evacuation."

# Main chat loop
while True:
    query = input("You: ")
    intent = get_intent(query)
    reply = respond(intent)
    print("Assistant:", reply)

    if intent == "exit":
        break
