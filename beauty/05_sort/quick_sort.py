import random
from typing import List

def quick_sort(items: List[int]):
    quick_sort_by_idx(items, 0, len(items)-1)

def quick_sort_by_idx(items: List[int], start, end: int):
    if start < end:
        mid = partition(items, start, end)
        quick_sort_by_idx(items, start, mid-1)
        quick_sort_by_idx(items, mid+1, end)

def partition(items: List[int], start, end: int):
    idx = random.randint(start, end)   
    items[end], items[idx] = items[idx], items[end]
    pivot = items[end]

    left, right = start, end
    while left < right:
        while left < right and items[left] <= pivot:
            left += 1
        items[right] = items[left]

        while left < right and items[right] > pivot:
            right -= 1
        items[left] = items[right]

    items[left] = pivot
    return left
    
    
# items = [3,2,1,5,4,6,7]
# quick_sort(items)
# print(items)