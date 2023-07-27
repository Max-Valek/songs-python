from networking.api_client import ApiClient
from networking.endpoints import Endpoints
from dataManager.charts import Charts

import json

if __name__ == "__main__":

    api_client = ApiClient()

    # response = api_client.get(Endpoints.Artists.TOP)
    response = api_client.get(Endpoints.Songs.TOP)

    # with open("response.json", "w") as outfile:
    #     json.dump(response, outfile)

    # ArtistsManager().print_top_artists(response)

    Charts().print_top_songs(response)

    
    