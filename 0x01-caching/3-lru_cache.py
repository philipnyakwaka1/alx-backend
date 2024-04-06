#!/usr/bin/env python3
"""LRUCache module"""

from base_caching import BaseCaching
from typing import Any, Union


class DoublyLinkedList():
    """created a double linked list node"""
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(BaseCaching):
    """This is an LRU Caching sytem"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.head = None
        self.tail = None
        self.hash = {}
        self.length = 0

    def shift_node(self, node):
        """shifts a node to the end"""
        if node is self.head:
            self.head = node.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def put(self, key: Any, item: Any) -> None:
        """Adds an item in the cache"""
        if key and item:
            if key in self.hash:
                node = self.hash[key]
                node.val = item
                self.shift_node(node)
            else:
                node = DoublyLinkedList(key, item)
                if self.head is None and self.tail is None:
                    self.head = node
                    if self.tail is None:
                        self.tail = self.head
                    self.hash[key] = node
                    self.cache_data[key] = node.val
                    self.length += 1
                else:
                    self.hash[key] = node
                    self.cache_data[key] = node.val
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    self.length += 1

                if self.length >= self.MAX_ITEMS:
                    del self.cache_data[self.head.key]
                    print(f'DISCARD: {self.head.key}')
                    del self.hash[self.head.key]
                    self.head = self.head.next
                    self.head.prev = None
                    self.length -= 1

    def get(self, key: Any) -> Union[None, Any]:
        """Get item by key"""
        val = self.hash.get(key)
        if val is None:
            return None
        node = self.hash[key]
        self.shift_node(node)
        return self.cache_data[key]
