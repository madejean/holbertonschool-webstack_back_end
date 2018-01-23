#!/usr/bin/python3
""" LIFOCache
"""
import queue

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
        - caching system with last in last out algorithm
    """

    def __init__(self):
        """ defining overloading method """
        super().__init__()
        self.queue = list()

    def put(self, key, item):
        """ assigns key value to cache_data dictionary
            if cache_data dictionary exceeds its limit
            the last item gets removed
        """
        if key is None or item is None:
            return
        if(len(self.cache_data) >= self.MAX_ITEMS and key not in self.queue):
            p = self.queue.pop()
            self.cache_data.pop(p)
            print("DISCARD", p)
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ retrieves the value linked to the key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
