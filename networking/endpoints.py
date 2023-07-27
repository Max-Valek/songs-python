class Endpoints:

    BASE_URL = "https://api.musixmatch.com/ws/1.1/"

    class Artists:
        TOP = "/chart.artists.get?page=1&page_size=5"

    class Songs:
        TOP = "chart.tracks.get?chart_name=top&page=1&page_size=5"