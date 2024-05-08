#!/usr/bin/python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Define MRUCache"""

    def __init__(self):
        """constructor"""
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                idx_del = self.stack.pop()
                self.cache_data.pop(idx_del)
                print(f'DISCARD: {idx_del}')

            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.stack:
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data[key]
