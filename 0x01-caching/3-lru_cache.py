#!/usr/bin/env python3

"""
class, LRUCache, that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    class definition that inherits from BaseCaching
    and impplements the Least Recently Used caching system.
    """
    def __init__(self):
        """
        method definition to initialize the cache
        by calling the parent init method.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method definition that adds an item to the cache using LRU.
        Should the cache exceed MAX_ITEMS limit,
        discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            top_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {top_key}")

    def get(self, key):
        """
        method definition that retrieves an item from the cache.
        If key is None/not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        x = self.cache_data.pop(key)
        self.cache_data[key] = x
        return x
