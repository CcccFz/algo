import math
from typing import List
O_nlogn_sort = __import__('02_O_nlogn_sort')

def bucket_sort(nums: List[int], bucket_size: int):
    num_max, num_min = max(nums), min(nums)
    bucket_cnt = math.ceil((num_max-num_min+1)/bucket_size)
    buckets = [[] for _ in range(bucket_cnt)]
    for num in nums:
        buckets[(num-num_min)//bucket_size].append(num)
    for bucket in buckets:
        O_nlogn_sort.quick_sort(bucket)
    return [num for bucket in buckets for num in bucket]

def count_sort(nums: List[int]):
    num_max, size = max(nums), len(nums)
    counts = [0] * (num_max+1)
    for num in nums:
        counts[num] += 1
    for i in range(1, num_max+1):
        counts[i] += counts[i-1]
    ret = [0] * size
    for i in range(size-1, -1, -1):
        counts[nums[i]] -= 1
        ret[counts[nums[i]]] = nums[i]
    return ret

def radix_sort(nums: List[int]):
    num_max, k = max(nums), 1
    while num_max >= 10**k:
        k += 1
    for i in range(k):
        buckets = [[] for _ in range(10)]
        for num in nums:
            buckets[num//10**i%10].append(num)
        nums = [num for bucket in buckets for num in bucket]
    return nums

print(bucket_sort([3,2,1,5,4,6,7], 3))
print(count_sort([3,2,1,5,4,6,7]))
print(radix_sort([3,2,1,5,4,6,7]))