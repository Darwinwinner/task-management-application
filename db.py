import pymongo
import configparser

# Connects to a MongoDB database using configuration settings from a file.
config = configparser.ConfigParser()
config.read('config.ini')

# Gt the MongoDB collection based on configuration settings
def get_db_collection():
    client = pymongo.MongoClient(config['mongodb']['uri'])
    db = client[config['mongodb']['database']]
    return db[config['mongodb']['collection']]  

