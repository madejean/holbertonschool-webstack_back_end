#!/usr/bin/python3
""" LIFOCache
"""
import queue

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.queue = list()

    def put(self, key, item):
        if key is None or item is None:
            pass
        if(len(self.cache_data) >= self.MAX_ITEMS and key not in self.queue):
            p = self.queue.pop()
            self.cache_data.pop(p)
            print("DISCARD", p)
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
