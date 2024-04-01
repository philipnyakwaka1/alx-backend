#!/usr/bin/env python3
"""This module defines index_range function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters.
    """
    last_index = page * page_size
    start_index = last_index - page_size
    return (start_index, last_index)
