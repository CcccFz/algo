from typing import List

def bsearch(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + ((right-left) >> 1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


def bsearch2(nums: List[int], target: int) -> int:
    return bsearch_recursion(nums, 0, len(nums)-1, target)

def bsearch_recursion(nums: List[int], left: int, right: int, target: int) -> int:
    if left > right:
        return -1
    mid = left + ((right-left) >> 1)
    if nums[mid] < target:
        return bsearch_recursion(nums, mid+1, right, target)
    elif nums[mid] > target:
        return bsearch_recursion(nums, left, mid-1, target)
    else:
        return mid

print(bsearch([-1, 0,3,5,9,12], target = 9))
print(bsearch2([-1, 0,3,5,9,12], target = 9))
