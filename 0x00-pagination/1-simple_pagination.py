#!/usr/bin/env python3
"""class Server """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """return a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        """ """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        (start, end) = index_range(page, page_size)
        list_data = []
        count = 0
        for line in self.dataset():
            if count >= start and count < end:
                list_data.append(line)
            count += 1
        return list_data
