from networking.client import ApiClient
from networking.endpoints import Endpoints
from dataManager.charts import Charts
from dataManager.files import Files


if __name__ == "__main__":

    # Makes requests to MusixMatch API
    api_client = ApiClient()

    #----- Top Charts Endpoints -----

    response = api_client.get(Endpoints.Chart.SONGS)
    # response = api_client.get(Endpoints.Chart.ARTISTS)

    Charts.print_top_songs(response)
    # Charts.print_top_songs(response)

    #----- Debug -----

    # Write response json to file.
    Files.save_as_json(response, "response.json")

    

    
    