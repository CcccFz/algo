import math
from quick_sort import quick_sort
from typing import List

def bucket_sort(items: List[int], bucket_size: int):
    item_max, item_min = max(items), min(items)
    bucket_count = math.ceil((item_max-item_min+1) / bucket_size)
    buckets = [[] for _ in range(bucket_count)]
    for item in items:
        bucket_idx = (item-item_min) // bucket_size
        buckets[bucket_idx].append(item)
    items = []
    for bucket in buckets:
        quick_sort(bucket)
        items.extend(bucket)
    return items

def count_sort(items: List[int]):
    size = len(items)
    if size <= 1:
        return
    counts = [0] * (max(items) + 1)
    for item in items:
        counts[item] += 1
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]
    ret = [0] * size
    for i in range(size-1, -1, -1):
        counts[items[i]] -= 1 
        ret[counts[items[i]]] = items[i]
    return ret

def radix_sort(items: List[int]):
    item_max = max(items)
    k = 1
    while item_max >= 10**k:
        k += 1
    for i in range(k):
        buckets = [[] for _ in range(10)]
        for item in items:
            buckets[item//(10**i)%10].append(item)
        items = [item for bucket in buckets for item in bucket]
    return items

print(bucket_sort([3,2,1,5,4,6,7], 3))
print(count_sort([3,2,1,5,4,6,7]))
print(radix_sort([3,2,1,5,4,6,7]))