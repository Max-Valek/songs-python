# Endpoints associated with requests to MusixMatch API.
class Endpoints:

    # Top charts endpoints.
    class Chart:
        ARTISTS = "/chart.artists.get?page=1&page_size=5"
        SONGS = "/chart.tracks.get?chart_name=top&page=1&page_size=5"