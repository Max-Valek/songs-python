import requests
import os
from dotenv import load_dotenv
from networking.status_code import StatusCode

# load environment variables from .env file
load_dotenv()

class ApiClient:

    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")
        self.base_url = os.getenv("BASE_URL")
        if not self.api_key or not self.base_url:
            raise ValueError("Could not get environment variables.")
        
    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}&apikey={self.api_key}"
        response = requests.get(url)
        
        message = StatusCode(response.status_code).value
        print(message)

        if response.ok:
            return response.json()
        else:
            response.raise_for_status()