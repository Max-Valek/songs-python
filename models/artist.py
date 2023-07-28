import json

# Artist object class.
class Artist:

    def __init__(self, data):
        self.id = data["artist_id"]
        self.name = data["artist_name"]
        self.country = data["artist_country"]
        self.alias_list = [alias["artist_alias"] for alias in data["artist_alias_list"]]
        self.rating = data["artist_rating"]