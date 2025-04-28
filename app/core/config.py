import requests
import os
from dotenv import load_dotenv
from typing import Dict

load_dotenv()


class GoogleMapsAPI:
    API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    
    def get_route(self, origin: str, destination: str) -> Dict:
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={self.API_KEY}'
        response = requests.get(url)
        return response.json()
