class Charts:

    def print_top_songs(self, data):
        for track in data['message']['body']['track_list']:
            name = track['track']["track_name"]
            artist = track['track']["artist_name"]
            print(f"{name} by {artist}")

    def print_top_artists(self, data):
        for artist in data['message']['body']['artist_list']:
            name = artist['artist']["artist_name"]
            print(name)