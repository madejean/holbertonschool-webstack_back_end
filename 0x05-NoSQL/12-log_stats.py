#!/usr/bin/python3
""" script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

def print_stats(mongo_collection):
    """prints count"""
    print("{} logs".format(nginx_collection.count()))
    print("Methods:")
    print("\t method GET: {}".format(
        nginx_collection.count({"method": "GET"})
    ))
    print("\t method POST: {}".format(
        nginx_collection.count({"method": "POST"})
    ))
    print("\t method PUT: {}".format(
        nginx_collection.count({"method": "PUT"})
    ))
    print("\t method PATCH: {}".format(
        nginx_collection.count({"method": "DELETE"})
    ))
    print("{} status check".format(
        nginx_collection.count({"method": "GET", "path": "/status"})
    ))

if __name__ == "__main__":
    """connection to mongo database and print stats"""
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx
    print_stats(nginx_collection)
