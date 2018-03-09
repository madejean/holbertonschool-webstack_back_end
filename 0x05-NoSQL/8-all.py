#!/usr/bin/python3
""" returns list of documents in a collection """


def list_all(mongo_collection):
    """checks if collection in empty"""
    if mongo_collection.count() is None:
        return []
    else:
        schools = mongo_collection.find()
        s = []
        for school in schools:
            s.append(school)
        return s
