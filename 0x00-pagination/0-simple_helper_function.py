#!/usr/bin/env python3

"""
This function takes two integer arguments, page and page_size
It returns a tuple of sixe two containing a start index
and an end index correspoinding to the range of indexes
to return in a list for those particular pagination parameters
"""


def index_range(page, page_size):
    """
    method definition
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
