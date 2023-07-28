import json

# Artist object class.
class Song:

    def __init__(self, data):
        self.id = data["track_id"]
        self.name = data["track_name"]
        self.artist_id = data["artist_id"]
        self.artist_name = data["artist_name"]