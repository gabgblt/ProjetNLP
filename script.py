import os
import openai
from datetime import datetime

# Load your API key securely from an environment variable
api_key = os.getenv("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")
openai.api_key = api_key

# Mock function for sentiment analysis
def analyze_sentiment(text):
    # Placeholder function for sentiment analysis
    return "Neutral"

# Mock function for summarizing the conversation
def summarize_conversation(messages):
    # Placeholder function for summarizing the conversation
    return "Summary of the conversation."

def main():
    print("Bonjour. N'hésitez pas à me poser des questions. Ou appuyez sur 'exit' pour quitter!")
    messages = [{"role": "system", "content": "Tu es un assistant scientifique précis et formel"}]
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print(summarize_conversation(messages))
            print("Fin de la conversation. Au revoir!")
            break
        timestamp = datetime.now().isoformat()
        messages.append({"role": "user", "content": user_input, "timestamp": timestamp})
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            ).choices[0].message
            print(response['content'])
            print("Sentiment:", analyze_sentiment(response['content']))
            messages.append({"role": "assistant", "content": response['content'], "timestamp": timestamp})
        except Exception as e:
            print(f"An error occurred: {e}")

# To prevent the code from running automatically, the call to main() is commented out.
# main()
