#!/usr/bin/python3
def update_topics(mongo_collection, name, topics):
    mongo_collection.update(
        { "name": name },
        { "$set": { "topics": topics }}
    )
