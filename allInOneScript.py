import openai
import requests
from bs4 import BeautifulSoup

# Set your OpenAI API key
api_key = 'ApiKey'
openai.api_key = api_key


def get_lyrics(song_url):
    # Define the Brave browser User-Agent header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Brave/98.1.4758.102'
    }

    # Make an HTTP GET request to the song URL with the Brave browser User-Agent header
    response = requests.get(song_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the elements containing the song lyrics
        lyrics_elements = soup.find_all('div', class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL")

        # Iterate over lyrics elements to remove sections with highlights
        for element in lyrics_elements:
            for highlight_element in element.find_all('span', class_="ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw"):
                # Extract the text of the highlight element and remove it from the lyrics
                highlight_text = highlight_element.get_text(separator=' ')
                element.get_text(separator='\n').replace(highlight_text, '')

            # Remove the highlighted sections from the lyrics
            for highlight_element in element.find_all('span', class_="ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw"):
                highlight_element.extract()

        # Get the cleaned lyrics text
        cleaned_lyrics = '\n'.join(line.strip() for element in lyrics_elements for line in element.get_text(separator='\n').split('\n') if line.strip())
        return cleaned_lyrics
    else:
        return "Erreur lors de la récupération des paroles."
    
    

def chat_with_openai():
    print("Bonjour. N'hésitez pas à me poser des questions. Tapez 'exit' pour quitter!")

    # Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are speaking with an assistant. How can I help you today?"}
    ]

    while True:
        
        song_url = str(input("Enter the URL of the song you want to have the meaning of : (type exit to quit)\n"))
        
        # Call the function to get the lyrics
        lyrics = get_lyrics(song_url)
        
        # Display the lyrics
        print(lyrics)
        
        lineChoice = int(input("Which line do you want to have the meaning of ?\n"))
        # Pour afficher une seule ligne spécifique (par exemple, la deuxième ligne)
        line = lyrics.split('\n')[lineChoice]
        print(line)
        
        
        user_input = f"Can you explain me what the author of the song wanted to say on the  line {line} of those lyrics ? " + lyrics
        print(user_input)   
        if song_url.lower() == "exit":
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

chat_with_openai()

