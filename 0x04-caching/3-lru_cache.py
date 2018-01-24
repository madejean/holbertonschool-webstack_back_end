#!/usr/bin/python3
""" LRUCache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
        - caching system with last recently used algorithm
    """

    def __init__(self):
        """ defines overloading method """
        super().__init__()
        self.count = 0
        self.lru = {}

    def put(self, key, item):
        """ assigns key value to cache_data dictionary
            if cache_data dictionary exceeds its limit
            the last recently used item gets removed
        """
        if key is None or item is None:
            return
        if(len(self.cache_data) >= self.MAX_ITEMS and
                key not in self.cache_data):
            p = min(self.lru.keys(), key=lambda k: self.lru[k])
            self.cache_data.pop(p)
            self.lru.pop(p)
            print("DISCARD:", p)
        self.cache_data[key] = item
        self.lru[key] = self.count
        self.count += 1

    def get(self, key):
        """ retrieves the value linked to the key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
