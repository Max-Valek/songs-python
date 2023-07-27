class ArtistsManager:

    def print_top_artists(self, data):
        for artist in data['message']['body']['artist_list']:
            name = artist['artist']["artist_name"]
            print(name)