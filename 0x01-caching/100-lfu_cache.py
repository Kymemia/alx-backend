#!/usr/bin/env python3

"""
class, LFUCache, that inherits from BaseConfig and is a caching system.
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    class definition that inherits from BaseCaching
    and impplements the Least Frequently Used caching system.
    """
    def __init__(self):
        """
        method definition to initialize the cache
        by calling the parent init method.

        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)
        self.use_order = OrderedDict()

    def put(self, key, item):
        """
        method definition that adds an item to the cache using LRU.
        Should the cache exceed MAX_ITEMS limit,
        discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.use_order.pop(key)
            self.use_order[key] = self.frequency[key]
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                least_frequent = [
                        i for i, j in self.frequency.items()
                        if j == min_frequency
                        ]

                if len(least_frequent) > 1:
                    lru_key = min(
                            least_frequent, key=lambda k: self.use_order[k]
                            )
                else:
                    lru_key = least_frequent[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                self.use_order.pop(lru_key)
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.use_order[key] = 1

    def get(self, key):
        """
        method definition that retrieves an item from the cache.
        If key is None/not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.use_order.pop(key)
        self.use_order[key] = self.frequency[key]

        return self.cache_data[key]
