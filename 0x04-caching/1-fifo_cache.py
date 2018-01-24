#!/usr/bin/python3
""" FIFOCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
        - caching system with first in first out algorithm
    """

    def __init__(self):
        """ defining overloading method """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ assigns key value to cache_data dictionary
            if cache_data dictionary exceeds its limit
            the first item gets removed
        """
        if key is None or item is None:
            return
        self.queue.append(key)
        self.cache_data[key] = item
        if(len(self.cache_data) > self.MAX_ITEMS):
            first_item = self.queue[0]
            self.cache_data.pop(first_item)
            self.queue.pop(0)
            print("DISCARD:", first_item)

    def get(self, key):
        """ retrieves the value linked to the key """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
