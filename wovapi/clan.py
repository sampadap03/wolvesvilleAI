import requests
import json

class ClanApi:
    def __init__(self):
        self.set_config()

    def set_config(self):
        with open('config.json', 'r') as myfile:
            data=myfile.read()
        response = json.loads(data)

        self.endpoint = response["endpoint"]
        self.headers = response["headers"]

        try:
            self.clan_id = response["clan_id"]
        except:
            self.clan_id = ""

    
    def get_clan_info(self):
        try:
            response = requests.get(f'{self.endpoint}/clans/{self.clan_id}/info', headers=self.headers)
            return response.json()
        except Exception as e:
            print(e)
            return False
        
# capi = ClanApi()
# print(capi.get_clan_info())