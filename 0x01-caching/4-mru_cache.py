#!/usr/bin/env python3

"""
class, MRUCache, that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    class definition that inherits from BaseCaching
    and impplements the Most Recently Used caching system.
    """
    def __init__(self):
        """
        method definition to initialize the cache
        and call the parent class' init method.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method definition that adds an item to the cache using MRU.
        Should the cache exceed MAX_ITEMS limit,
        discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            latest_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {latest_key}")

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
