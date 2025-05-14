#!/usr/bin/env python3
"""
0-basic_cache module
Provides a basic dictionary-based caching system.
"""

from base_caching import BaseCaching # type: ignore


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements
    a caching system with no limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache using the given key.

        Args:
            key: The key for the cache.
            item: The value to be cached.

        This method does nothing if key or item is None.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache using the given key.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The cached item, or None if not found or key is None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
