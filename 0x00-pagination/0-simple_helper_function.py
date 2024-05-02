#!/usr/bin/env python3
"""index_range module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """return a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
