#!/usr/bin/env python3

"""
class, BasicCache, that inherits from BaseCaching
that's caching a sysem
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class definition
    """
    def put(self, key, item):
        """
        method definition that assigns the item value
        for the key in cache_data.
        If key/ item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        method definition that returns the value associated
        with they key in cache_data.
        If the key is None or doesn't exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
