#!/usr/bin/python3
""" changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """updates a collection by name"""
    mongo_collection.update(
        {"name": name},
        {"$set": {"topics": topics}},
        {multi: true},
    )
