from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
client=MongoClient('localhost',27017)
try:
    client.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: Failed',cf)