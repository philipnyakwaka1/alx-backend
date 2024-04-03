#!/usr/bin/env python3
"""LIFOCache module"""

from base_caching import BaseCaching
from typing import Any, Union


class LIFOCache(BaseCaching):
    """This is a LIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.last_item_key = None

    def put(self, key: Any, item: Any) -> None:
        """Adds an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            keys_list = sorted(list(self.cache_data.keys()))
            if len(keys_list) > self.MAX_ITEMS:
                if self.last_item_key is None:
                    del self.cache_data[keys_list[-1]]
                    print(f'DISCARDED: {keys_list[-2]}')
                else:
                    idx = keys_list.index(self.last_item_key)
                    del self.cache_data[keys_list[idx]]
                    print(f'DISCARDED: {keys_list[idx]}')
            self.last_item_key = key

    def get(self, key: Any) -> Union[None, Any]:
        """Get item by key"""
        return self.cache_data.get(key)
