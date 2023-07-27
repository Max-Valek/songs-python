# Methods relating to top charts data
class Charts:

    # Print the name and artist of the songs returned by chart.tracks.get API endpoint.
    @staticmethod
    def print_top_songs(data):
        for track in data['message']['body']['track_list']:
            name = track['track']["track_name"]
            artist = track['track']["artist_name"]
            print(f"{name} by {artist}")

    # Print the names artists returned by chart.artists.get API endpoint.
    @staticmethod
    def print_top_artists(data):
        for artist in data['message']['body']['artist_list']:
            name = artist['artist']["artist_name"]
            print(name)