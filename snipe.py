import requests
import configparser

#create a snipe class

config = configparser.ConfigParser()
config.read('config.ini')
token = config['snipe']['token']


class Snipe:
    
    url = config['snipe']['url']
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
        
    def get_users(self):
        url = self.url + '/users'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
        
    def get_assets(self,id):
        url = self.url + '/users/' + str(id) +'/assets'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_assets(self):
        url = self.url + '/hardware'
        response = requests.get(url, headers=self.headers)
        return response.json()