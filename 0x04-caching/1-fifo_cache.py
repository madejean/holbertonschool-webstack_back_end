#!/usr/bin/python3
""" FIFOCache
"""
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super(FIFOCache, self).__init__()

    def put(self, key, item):
        if not key or not item:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_item = list(self.cache_data)[0];
            self.cache_data.pop(first_item)
            print("DISCARD: {}".format(first_item))

    def get(self, key):
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
