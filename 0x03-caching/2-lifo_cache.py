#!/usr/bin/env python3
""" Module named 2-lifo_cache """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A class LIFOCache that inherits from
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
                # LIFO algorithm
                del self.cache_data[self.all_keys[-2]]
                print("DISCARD: {}".format(self.all_keys[-2]))
                self.all_keys.pop(-2)

    def get(self, key):
        """ Function to return the value: item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
