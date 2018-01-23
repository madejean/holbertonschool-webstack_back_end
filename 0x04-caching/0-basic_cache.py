#!/usr/bin/python3
""" BasicCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    """ BasicCache defines:
        - caching system
    """

    def put(self, key, item):
        """ assign key value to cache_data dictionary """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ retrieves the value linked to the key """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
