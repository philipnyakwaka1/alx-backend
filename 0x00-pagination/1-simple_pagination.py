#!/usr/bin/env python3
"""This module defines index_range function"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters.
    """
    last_index = page * page_size
    start_index = last_index - page_size
    return (start_index, last_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns paginated page content"""

        assert(isinstance(page, int) and page > 0)
        assert(isinstance(page_size, int) and page_size > 0)
        pages = index_range(page, page_size)
        dataset = self.dataset()
        if (pages[0] > len(dataset) - 1) or (pages[1] > len(dataset) - 1):
            return []
        return dataset[pages[0]: pages[1] + 1]
