#!/usr/bin/python3
""" returns list of schools with a specific topic """


def schools_by_topic(mongo_collection, topic):
        """find topic"""
        result = mongo_collection.find({"topics": topic})
        return result
