import requests
import os
from dotenv import load_dotenv
from networking.status import Status

load_dotenv()   # load environment variables from .env file

# Responsible for interacting with the MusixMatch API.
class ApiClient:

    def __init__(self) -> None:
        # Environment variables
        self.api_key = os.getenv("API_KEY")
        self.base_url = os.getenv("BASE_URL")
        if not self.api_key or not self.base_url:
            raise ValueError("Could not get environment variables.")
    
    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}&apikey={self.api_key}"
        response = requests.get(url)
        print(Status.get_message(response.status_code))

        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    