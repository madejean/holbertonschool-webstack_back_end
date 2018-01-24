#!/usr/bin/python3
""" MRUCache
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
        - caching system with most recently used algorithm
    """

    def __init__(self):
        """ defines overloading method """
        super().__init__()
        self.count = 0
        self.mru = {}

    def put(self, key, item):
        """ assigns key value to cache_data dictionary
            if cache_data dictionary exceeds its limit
            the most recently used item gets removed
        """
        if key is None or item is None:
            return
        if(len(self.cache_data) >= self.MAX_ITEMS):
            p = max(self.mru.keys(), key=lambda k: self.mru[k])
            self.cache_data.pop(p)
            self.mru.pop(p)
            print("DISCARD:", p)
        self.cache_data[key] = item
        self.mru[key] = self.count
        self.count += 1

    def get(self, key):
        """ retrieves the value linked to the key """
        if key is None or key not in self.cache_data:
            return None
        self.mru[key] = self.count
        self.count += 1
        return self.cache_data[key]
