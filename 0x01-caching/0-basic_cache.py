#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching
from typing import Any, Union


class BasicCache(BaseCaching):
    """This is a caching system that doesn't have any limits"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """Add item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: Any) -> Union[None, Any]:
        """Get item by key"""
        return self.cache_data.get(key)
