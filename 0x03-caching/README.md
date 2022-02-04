# 0x03. Caching

## Learning Objectives

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

### Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined below:

    $ cat base_caching.py
    #!/usr/bin/python3
    """ BaseCaching module
    """

    class BaseCaching():
        """ BaseCaching defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        """
        MAX_ITEMS = 4

        def __init__(self):
            """ Initiliaze
            """
            self.cache_data = {}

        def print_cache(self):
            """ Print the cache
            """
            print("Current cache:")
            for key in sorted(self.cache_data.keys()):
                print("{}: {}".format(key, self.cache_data.get(key)))

        def put(self, key, item):
            """ Add an item in the cache
            """
            raise NotImplementedError("put must be implemented in your cache class")

        def get(self, key):
            """ Get an item by key
            """
            raise NotImplementedError("get must be implemented in your cache class")

## Tasks

### Mandatory

[**0. Basic dictionary:**](https://github.com/dianaparr/holbertonschool-web_back_end/blob/main/0x03-caching/0-basic_cache.py)

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- This caching system doesn’t have limit
- `def put(self, key, item):`
    - Must assign to the dictionary self.cache_data the item value for the key key.
    - If key or item is None, this method should not do anything.
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

<br />

[**1. FIFO caching:**](https://github.com/dianaparr/holbertonschool-web_back_end/blob/main/0x03-caching/1-fifo_cache.py)

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - you must discard the first item put in cache (FIFO algorithm)
        - you must print `DISCARD`: with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to key.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

<br />

[**2. LIFO Caching:**](https://github.com/dianaparr/holbertonschool-web_back_end/blob/main/0x03-caching/2-lifo_cache.py)

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - you must discard the last item put in cache (LIFO algorithm)
        - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to key.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

<br />

[**3. LRU Caching:**](https://github.com/dianaparr/holbertonschool-web_back_end/blob/main/0x03-caching/3-lru_cache.py)

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - you must discard the least recently used item (LRU algorithm)
        - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

<br />

[**4. MRU Caching:**](https://github.com/dianaparr/holbertonschool-web_back_end/blob/main/0x03-caching/4-mru_cache.py)

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - you must discard the most recently used item (MRU algorithm)
        - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

<br />

### Advanced

[**5. LFU Caching:**](https://github.com/dianaparr/holbertonschool-web_back_end/blob/main/0x03-caching/100-lfu_cache.py)

Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - you must discard the least frequency used item (LFU algorithm)
        - if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
        - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.
