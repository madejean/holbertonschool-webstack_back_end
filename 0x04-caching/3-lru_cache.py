#!/usr/bin/python3
""" LRUCache
"""
import queue

BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.tm = 0
        self.lru = {}

    def put(self, key, item):
        if key is None or item is None:
            pass
        if(len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data):
            p = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache_data.pop(p)
            self.lru.pop(p)
            print("DISCARD", p)
        self.cache_data[key] = item
        self.lru[key] = self.tm
        self.tm += 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.lru[key] = self.tm
        self.tm += 1
        return self.cache_data[key]
