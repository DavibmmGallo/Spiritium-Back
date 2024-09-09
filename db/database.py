from pymongo import MongoClient
from pymongo.database import Database

def get_database(config: dict) -> Database:
    db = config['db']
    host = config.get('host', 'localhost')
    port = config.get('port', '27017')

    uri = f'{host}:{port}'
    username = config['user']
    password = config['pass']
    uri = f'{username}:{password}@{uri}/?authSource=admin'

    client = MongoClient(f'mongodb://{uri}')
    return client[db]
