#!/usr/bin/env python3
""" Module named 1-fifo_cache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A class FIFOCache that inherits from
        BaseCaching and is a caching system.
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
            if len(self.all_keys) > BaseCaching.MAX_ITEMS:
                # FIFO algorithm
                del_first = self.all_keys.pop(0)
                del self.cache_data[del_first]
                print("DISCARD: {}".format(del_first))

    def get(self, key):
        """ Function to return the value: item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
