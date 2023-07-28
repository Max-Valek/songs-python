import json
from models.artist import Artist

# Methods relating to search
class Search:

    @staticmethod
    def print_search_artists(data):
        # d = json.loads(data)
        artist_list = data["message"]["body"]["artist_list"]
        artists = []
        for artist_data in artist_list:
            artist = Artist(artist_data["artist"])
            artists.append(artist)

        for artist in artists:
            print(f"Name: {artist.name}")