import requests
from bs4 import BeautifulSoup

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

# URL of the song on Genius
song_url = "https://genius.com/Eminem-mockingbird-lyrics"

# Call the function to get the lyrics
lyrics = get_lyrics(song_url)

# Display the lyrics
print(lyrics)
