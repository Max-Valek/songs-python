import json
from models.artist import Artist
from models.song import Song

# Methods relating to search
class Search:

    @staticmethod
    def print_search_artists(data):
        """Print the list of artists returned from a search.

        Params:
            data:   The search request response json.
        """

        artist_list = data["message"]["body"]["artist_list"]
        artists = []
        for artist_data in artist_list:
            artist = Artist(artist_data["artist"])
            artists.append(artist)

        for artist in artists:
            print(f"Name: {artist.name}")

    @staticmethod
    def print_search_songs(data):
        """Print the list of songs returned from a search.

        Params:
            data:   The search request response json.
        """
        
        song_list = data["message"]["body"]["track_list"]
        songs = []
        for song_data in song_list:
            song = Song(song_data["track"])
            songs.append(song)
        
        for song in songs:
            print(f"{song.name} by {song.artist_name}")