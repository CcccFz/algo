from typing import List
import random

def merge_sort(items: List[int]):
    merge_sort_by_idx(items, 0, len(items)-1)

def merge_sort_by_idx(items: List[int], start, end: int):
    if start < end:
         mid = start + (end - start) // 2
         merge_sort_by_idx(items, start, mid)
         merge_sort_by_idx(items, mid+1, end)
         merge(items, start, mid, end)

def merge(items: List[int], start, mid, end: int):
    tmp = []
    i, j = start, mid+1
    while i <= mid and j <= end:
        if items[i] <= items[j]:
            tmp.append(items[i])
            i += 1
        else:
            tmp.append(items[j])
            j += 1
    head, tail = (i, mid) if i <= mid else (j, end)
    tmp.extend(items[head:tail+1])
    items[start:end+1] = tmp



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

    i = start
    for j in range(start, end):
        if items[j] < items[end]:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[end] = items[end], items[i]
    return i
    


items = [3,2,1,5,4,6,7]
merge_sort(items)
print(items)
items = [3,2,1,5,4,6,7]
quick_sort(items)
print(items)