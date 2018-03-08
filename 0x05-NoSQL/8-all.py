#!/usr/bin/python3
def list_all(mongo_collection):
    if mongo_collection.count() is None:
        return []
    else:
        schools = mongo_collection.find()
        s = []
        for school in schools:
            s.append(school)
        return s
