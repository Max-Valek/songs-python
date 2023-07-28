import requests
import os
from dotenv import load_dotenv
from networking.status import Status

load_dotenv()                                                       # load environment variables from .env file

# Responsible for interacting with the MusixMatch API.
class ApiClient:

    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")                         # API key from environment
        self.base_url = os.getenv("BASE_URL")                       # base URL from environment

        if not self.api_key or not self.base_url:
            raise ValueError("Could not load environment variables.")
    
    def get(self, endpoint):
        """Execute a GET request to a specified endpoint.

        Parameters:
            endpoint:
                MusixMatch API endpoint to combine with the base URL.

        Returns:
            The response JSON
        """

        url = f"{self.base_url}{endpoint}&apikey={self.api_key}"    # request URL
        response = requests.get(url)                                # make GET request
        print(Status.get_message(response.status_code))             # print message for response status code
        if response.ok:
            return response.json()                                  # return response as JSON if successful
        else:
            response.raise_for_status()                             # otherwise raise and error

    