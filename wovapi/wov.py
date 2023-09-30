import requests
import json

class WovApi:
    def __init__(self):
        self.set_config()

    def set_config(self):
        with open('config.json', 'r') as myfile:
            data=myfile.read()
        response = json.loads(data)

        self.endpoint = response["endpoint"]
        self.headers = response["headers"]

    def get_seasons(self):
        try:
            response = requests.get(self.endpoint + "/battlePass/season", headers=self.headers)
            return response.json()
        except Exception as e:
            print(e)
            return False


wapi = WovApi()
