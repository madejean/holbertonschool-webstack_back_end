#!/usr/bin/python3
def schools_by_topic(mongo_collection, topic):
        result =  mongo_collection.find({"topics": topic })
        return result
