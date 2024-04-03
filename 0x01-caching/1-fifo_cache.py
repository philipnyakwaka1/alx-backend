#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching
from typing import Any, Union


class FIFOCache(BaseCaching):
    """This is a FIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """Adds an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            keys_list = sorted(list(self.cache_data.keys()))
            if len(keys_list) > self.MAX_ITEMS:
                del self.cache_data[keys_list[0]]
                print(f'DISCARD: {keys_list[0]}')

    def get(self, key: Any) -> Union[None, Any]:
        """Get item by key"""
        return self.cache_data.get(key)
