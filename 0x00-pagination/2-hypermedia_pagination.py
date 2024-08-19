#!/usr/bin/env python3

"""
class that paginates a database of popular names
"""
import csv
import math
from typing import List


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []
        return dataset[start:end]

    def index_range(self, page: int, page_size: int) -> tuple[int, int]:
        """
        method definition
        """
        start = (page - 1) * page_size
        end = min(start + page_size, len(self.dataset()))
        return start, end

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        method definition that returns a dictionary
        containing information regarding current page & dataset
        """
        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
                "page_size": page_size,
                "page": page,
                "data": dataset_page,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }
