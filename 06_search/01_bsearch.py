from typing import List

def bsearch(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def bsearch_recursion(nums: List[int], target: int) -> int:
    def bsearch_idx(nums, low, high):
        if low > high:
            return -1
        mid = low + ((high-low)>>1)
        if nums[mid] < target:
            return bsearch_idx(nums, mid+1, high)
        elif nums[mid] > target:
            return bsearch_idx(nums, low, mid-1)
        else:
            return mid

    return bsearch_idx(nums, 0, len(nums)-1)

print(bsearch([-1,0,3,5,9,12], target = 9))
print(bsearch_recursion([-1,0,3,5,9,12], target = 9))
