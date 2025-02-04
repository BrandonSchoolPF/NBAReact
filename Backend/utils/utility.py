import requests
import os
from dotenv import load_dotenv

load_dotenv()


class API_Verbs:
    def __init__(self):
        self.url = os.getenv("API_URL")
        self.api_key = os.getenv("API_KEY")
        self.header = {
            'x-rapidapi-key': self.api_key,
            'x-rapidapi-host': self.url
            }
    
    def get(self, endpoint:str, params=None):
        formatted_url = f"{self.url}/{endpoint}"
        response = requests.get(formatted_url, params=params, headers=self.header)
        return response
    
    def post(self, endpoint:str, body:dict,):
        formatted_url = f"{self.url}/{endpoint}"
        response = requests.post(formatted_url, params=params, headers=self.header, json=body)
        return response.json()

if __name__ == "__main__":
    test = API_Verbs()
    print(test)
