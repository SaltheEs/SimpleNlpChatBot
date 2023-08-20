import spacy
from spacy.matcher import Matcher

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define response templates
response_templates = {
    "track_order": "Your order with order number {} is on its way.",
    "return": "To initiate a return, please contact our customer support.",
    "product_info": "The product {} is a popular choice among customers.",
    "fallback": "I'm sorry, I couldn't understand your query. Can you please provide more details?",
}

# Define intent patterns using spaCy's Matcher
matcher = Matcher(nlp.vocab)
matcher.add("TrackOrder", [{"LOWER": "track"}, {"LOWER": "order"}])
matcher.add("Return", [{"LOWER": "return"}])
matcher.add("ProductInfo", [{"LOWER": "product"}, {"LOWER": "information"}])


# Function to process user input and generate response
def process_input(input_text):
    doc = nlp(input_text)
    matches = matcher(doc)

    for match_id, start, end in matches:
        if nlp.vocab.strings[match_id] == "TrackOrder":
            # Implement order tracking logic
            order_number = extract_order_number(doc, start, end)
            return response_templates["track_order"].format(order_number)

        elif nlp.vocab.strings[match_id] == "Return":
            # Implement return logic
            return response_templates["return"]

        elif nlp.vocab.strings[match_id] == "ProductInfo":
            # Implement product information logic
            product_name = extract_product_name(doc, start, end)
            return response_templates["product_info"].format(product_name)

    return response_templates["fallback"]


# Function to simulate chatbot interaction
def chatbot_simulation():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = process_input(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chatbot_simulation()
