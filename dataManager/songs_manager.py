class SongsManager:

    def print_top_songs(self, data):
        for track in data['message']['body']['track_list']:
            name = track['track']["track_name"]
            artist = track['track']["artist_name"]
            print(f"{name} by {artist}")