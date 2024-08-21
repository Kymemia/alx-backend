#!/usr/bin/env python3

"""
class, LIFOCache, that inherits from BaseCaching
and is a caching system.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class definition that inherits from BaseCaching
    and implements the Last-In, First-Out caching system.
    """
    def __init__(self):
        """
        method definition to initialize the cache
        by calling the parent init method.
        """
        super().__init__()

    def put(self, key, item):
        """
        method definition to add an item to the cache using LIFO.
        Should the cache exceed MAX_ITEMS limit,
        discard the last item added to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        method definition to retrieve an item from the cache.
        If the key is None or not in the cache, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
