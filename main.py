from networking.client import ApiClient
from networking.endpoints import Endpoints
from dataManager.charts import Charts


if __name__ == "__main__":

    api_client = ApiClient()

    #----- TOP CHARTS ENDPOINTS -----

    response = api_client.get(Endpoints.Chart.SONGS)
    # response = api_client.get(Endpoints.Chart.ARTISTS)

    Charts.print_top_songs(response)
    # Charts().print_top_songs(response)

    #----- Debug -----

    # Write response json to file for debugging.
    # with open("response.json", "w") as outfile:
    #     json.dump(response, outfile)

    

    
    