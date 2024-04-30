pip install openai==0.28

import openai

# Set your OpenAI API key
api_key = 'API_Key'
openai.api_key = api_key

def chat_with_openai():
    print("Bonjour. N'hésitez pas à me poser des questions. Tapez 'exit' pour quitter!")

    # Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are speaking with an assistant. How can I help you today?"}
    ]

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("Fin de la conversation. Au revoir!")
            break

        # Add user message to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Request completion from OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history
            )
            # Add AI response to conversation history
            conversation_history.append(response['choices'][0]['message'])
            # Print the AI response
            print(response['choices'][0]['message']['content'])
        except Exception as e:
            print(f"An error occurred: {e}")

# Uncomment the line below to run the function when all setup is done
chat_with_openai()
