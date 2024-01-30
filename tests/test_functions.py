import pytest
from solutions.two_d_lists import *

def test_sum_each_row():
    assert sum_each_row([[1, 2], [3, 4], [5, 6]]) == [3, 7, 11]
    assert sum_each_row([[1], [2], [3]]) == [1, 2, 3]
    assert sum_each_row([[]]) == [0]

def test_count_non_zero():
    assert count_non_zero([[1, 2, 0], [0, 4, 5], [6, 0, 0]]) == 5
    assert count_non_zero([[0], [0], [0]]) == 0
    assert count_non_zero([[]]) == 0

def test_last_elements():
    assert last_elements([[1, 2], [3, 4], [5, 6]]) == [2, 4, 6]
    assert last_elements([[1], [2], [3]]) == [1, 2, 3]
    assert last_elements([[]]) == []

def test_count_occurrences():
    assert count_occurrences([[1, 2], [2, 3], [4, 2]], 2) == 3
    assert count_occurrences([[1, 2], [3, 4]], 5) == 0
    assert count_occurrences([[]], 1) == 0
