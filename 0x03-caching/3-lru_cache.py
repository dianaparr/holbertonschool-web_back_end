#!/usr/bin/env python3
""" Module named 3-lru_cache """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ A class LRUCache that inherits from
        BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initialize a new FIFOCache. """
        super().__init__()
        self.all_keys = []

    def put(self, key, item):
        """ Function to assing to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.all_keys:
                self.all_keys.append(key)
            else:
                self.all_keys.append(self.all_keys.pop(
                    self.all_keys.index(key)))
            if len(self.all_keys) > BaseCaching.MAX_ITEMS:
                # LRU algorithm
                least_recently_used = self.all_keys.pop(0)
                del self.cache_data[least_recently_used]
                print("DISCARD: {}".format(least_recently_used))

    def get(self, key):
        """ Function to return the value: item by key """
        if key is not None and key in self.cache_data:
            self.all_keys.append(self.all_keys.pop(
                self.all_keys.index(key)))
            return self.cache_data[key]
        return None
