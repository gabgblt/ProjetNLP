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
        lyrics_element = soup.find('div', class_='PageGriddesktop-a6v82w-0 SongPageGriddesktop-sc-1px5b71-0 Lyrics__Root-sc-1ynbvzw-0 iEyyHq')

        # Vérifier si les paroles ont été trouvées
        if lyrics_element:
            # Extraire le texte des paroles et le nettoyer
            lyrics = lyrics_element.get_text('\n')
            cleaned_lyrics = '\n'.join(line.strip() for line in lyrics.split('\n') if line.strip())
            
            # Supprimer les 11 premières lignes et les 2 dernières lignes
            lines = cleaned_lyrics.split('\n')
            #lines = lines[3:]
            #lines = lines[:-1]
            cleaned_lyrics = '\n'.join(lines)
            
            return cleaned_lyrics
        else:
            return "Paroles non trouvées."
    else:
        return "Erreur lors de la récupération des paroles."

# URL de la chanson sur Genius
song_url = "https://genius.com/Raplume-9-lyrics"

# Appel de la fonction pour obtenir les paroles
lyrics = get_lyrics(song_url)

# Affichage des paroles
print(lyrics)
