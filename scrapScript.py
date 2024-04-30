import requests
from bs4 import BeautifulSoup

def get_lyrics(song_url):
    # Faire une requête HTTP GET à l'URL de la chanson
    response = requests.get(song_url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trouver l'élément HTML contenant les paroles de la chanson
        lyrics_element = soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')

        # Vérifier si les paroles ont été trouvées
        if lyrics_element:
            # Extraire le texte des paroles et le nettoyer
            lyrics = lyrics_element.get_text(separator='\n')
            cleaned_lyrics = '\n'.join(line.strip() for line in lyrics.split('\n') if line.strip())
            return cleaned_lyrics
        else:
            return "Paroles non trouvées."
    else:
        return "Erreur lors de la récupération des paroles."

# URL de la chanson sur Genius
song_url = "https://genius.com/Eminem-mockingbird-lyrics"

# Appel de la fonction pour obtenir les paroles
lyrics = get_lyrics(song_url)

# Affichage des paroles
print(lyrics)
