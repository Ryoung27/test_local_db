#main.py
#Author: Ronnie Young
#A test of using built-in data structures.
# https://hackernoon.com/4-ways-to-manage-the-configuration-in-python-4623049e841b

import pymysql
import config
import player_info_two

def player_name():
    if player_info_two.player_info.Player_one['name'] == 'Random':
        print(player_info_two.player_info.Player_one['name'])
    else:
        print("No thanks")

    if player_info_two.player_info.Player_one['name'] != 'Ranom':
        print("Sorry Charlie")

def connect_db(dbname):
    print("Test")
    # if dbname != config.DATABASE_CONFIG['dbname']:
    #     raise ValueError("Couldn't find DB with given name.")
    # conn = pymysql.connect(host=config.DATABASE_CONFIG['host'],
    #                        user=config.DATABASE_CONFIG['user'],
    #                        password=config.DATABASE_CONFIG['password'],
    #                        db=config.DATABASE_CONFIG['dbname'])

    # return conn

connect_db('company')
player_name()
# count()