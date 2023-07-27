# Endpoints associated with requests to MusixMatch API.
class Endpoints:

    # Top charts endpoints
    class Chart:
        """
        Get the list of the top artists of a given country.

        TODO: implement params: country, page, page_size, format
        """
        ARTISTS = "/chart.artists.get?page=1&page_size=5"

        """
        Get the list of the top songs of a given country.

        TODO: implement params: country, page, page_size, chart_name, f_has_lyrics
        """
        SONGS = "/chart.tracks.get?chart_name=top&page=1&page_size=5"