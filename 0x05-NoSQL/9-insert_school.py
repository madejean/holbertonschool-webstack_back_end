#!/usr/bin/python3
""" inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """returns newly inserted school id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
