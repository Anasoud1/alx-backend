#!/usr/bin/python3
""" FIFOCache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Define FIFOCache"""

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = list(self.cache_data)[0]
                del self.cache_data[first_item]
                print(f"DISCARD: {first_item}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
