# Methods relating to top charts data
class Charts:

    @staticmethod
    def print_top_songs(data):
        """Print top songs list.

        endpoint: chart.tracks.get
        """

        for track in data['message']['body']['track_list']:
            name = track['track']["track_name"]
            artist = track['track']["artist_name"]
            print(f"{name} by {artist}")

    @staticmethod
    def print_top_artists(data):
        """Print top artists list.

        endpoint: chart.artists.get
        """
        
        for artist in data['message']['body']['artist_list']:
            name = artist['artist']["artist_name"]
            print(name)