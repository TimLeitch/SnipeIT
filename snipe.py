import requests
import configparser
#create a snipe class

config = configparser.ConfigParser()
config.read('config.ini')
token = config['snipe']['token']


class Snipe:
    
    url = 'https://terrafirma.snipe-it.io/api/v1'
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
        
    def get_users(self):
        url = self.url + '/users'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
        
    