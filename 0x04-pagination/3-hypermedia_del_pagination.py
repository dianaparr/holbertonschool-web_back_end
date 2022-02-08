#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Deletion-resilient hypermedia pagination

        Args:
            page -> integer
            page_size -> integer

        Return: a dictionary
        """
        dataset_csv = list()
        assert type(index) == int and type(page_size) == int
        data_csv = self.indexed_dataset()
        size_data_csv = len(data_csv)
        assert 0 <= index < size_data_csv

        next_index = index
        for _ in range(page_size):
            if not data_csv.get(next_index):
                next_index += 1
            dataset_csv.append(data_csv[next_index])
            next_index += 1

        dict_pages = {
            "index": index,
            "data": dataset_csv,
            "page_size": page_size,
            "next_index": next_index
        }

        return dict_pages
