#main.py
#Author: Ronnie Young
#A test of using built-in data structures.
# https://hackernoon.com/4-ways-to-manage-the-configuration-in-python-4623049e841b

import pymysql
import config

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