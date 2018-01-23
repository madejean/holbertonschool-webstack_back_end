#!/usr/bin/python3
""" MRUCache
"""
import queue

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.tm = 0
        self.mru = {}

    def put(self, key, item):
        if key is None or item is None:
            pass
        if(len(self.cache_data) >= self.MAX_ITEMS):
            p = max(self.mru.keys(), key=lambda k: self.mru[k])
            self.cache_data.pop(p)
            self.mru.pop(p)
            print("DISCARD", p)
        self.cache_data[key] = item
        self.mru[key] = self.tm
        self.tm += 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.mru[key] = self.tm
        self.tm += 1
        return self.cache_data[key]
