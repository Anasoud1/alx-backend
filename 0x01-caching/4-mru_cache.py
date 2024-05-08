#!/usr/bin/python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Define MRUCache"""

    def __init__(self):
        """constructor"""
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                idx_del = self.queue.pop(-2)
                del self.cache_data[idx_del]

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data[key]
