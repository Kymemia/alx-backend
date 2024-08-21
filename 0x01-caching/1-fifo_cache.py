#!/usr/bin/env python3

"""
class, FIFOCache, that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class definition that inherits from BaseCaching
    and impplements the First-In, First-Out caching system
    """
    def __init__(self):
        """
        method definition to initialize the cache
        and call the parent class' init
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        method definition to add an item
        to the cache using FIFO method
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                top_key = self.order.pop(0)
                del self.cache_data[top_key]
                print(f"DISCARD: {top_key}")

            self.cache_data[key] = item
            self.order.append(key)
