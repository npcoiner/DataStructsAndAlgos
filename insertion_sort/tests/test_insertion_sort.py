from insertion_sort.main import insertion_sort
from insertion_sort.main import insertion_sort_flipped

import random

def test_small():
    assert insertion_sort([3,1,2]) == [1,2,3]

def test_empty():
    assert insertion_sort([]) == []

def test_random():
    data = random.sample(range(1000), 100)
    assert insertion_sort(data) == sorted(data)

def test_small_flipped():
    assert insertion_sort_flipped([3,1,2]) == [1,2,3]

def test_empty_flipped():
    assert insertion_sort_flipped([]) == []

def test_random_flipped():
    data = random.sample(range(1000), 100)
    assert insertion_sort_flipped(data) == sorted(data)


