from snipe import Snipe as snipe
import pandas as pd
from time import sleep

print('Welcome to Snipe-IT')
def main():
    choice = -1
    while choice != 0:
        print('1. Get Users')
        print('2. Get Users with no assets')
        print('0. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            get_users()
        elif choice == 2:
            get_users_no_assets()
        elif choice == 0:
            print('Goodbye')
        else:
            print('Invalid choice')


def create_csv(data, filename):
    df = data.to_dataframe()
    df.to_csv(filename, index=False)        
        
def get_users():
    users = snipe.get_users(snipe)
    for user in users['rows']:
        print(user['first_name'], user['last_name'])
        print('Title:', user["jobtitle"])      
        if user['assets_count'] > 0:
            assets = snipe.get_assets(snipe,user['id'])
            print('Assets Count:', user['assets_count'])
            for asset in assets['rows']:
                print('\tName:',asset['name'])
                print('\tTag:', asset['asset_tag'])
                print('\tModel:',asset['model']['name'],'\n')
                sleep(0.5)
        print()

def get_users_no_assets():
    users = snipe.get_users(snipe)
    for user in users['rows']:
        if user['assets_count'] == 0:
            print(user['first_name'], user['last_name'])
            print('Title:', user["jobtitle"])
            print('Assets Count:', user['assets_count'])
            print()
        
        
        






if __name__ == '__main__':
    main()
    

