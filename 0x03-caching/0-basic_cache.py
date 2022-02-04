#!/usr/bin/env python3
""" Module named 0-basic_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A class BasicCache that inherits from
        BaseCaching and is a caching system.

    This caching system doesn’t have limit.

    """
    def put(self, key, item):
        """ Function to assing to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Function to return the value: item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
