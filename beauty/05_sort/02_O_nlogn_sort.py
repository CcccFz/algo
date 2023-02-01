from typing import List
import random

def merge_sort(nums: List[int]):
    def merge_sort_idx(nums, low, high):
        if low < high:
            mid = low + ((high-low)>>1)
            merge_sort_idx(nums, low, mid)
            merge_sort_idx(nums, mid+1, high)
            merge(nums, low, mid, high)

    def merge(nums, low, mid, high):
        i, j = low, mid+1
        tmp = []
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        start, end = (i, mid) if i <= mid else (j, high)
        tmp.extend(nums[start:end+1])
        nums[low:high+1] = tmp
    
    merge_sort_idx(nums, 0, len(nums)-1)

def quick_sort(nums: List[int]):
    def quick_sort_idx(nums, low, high):
        if low < high:
            mid = partition(nums, low, high)
            quick_sort_idx(nums, low, mid-1)
            quick_sort_idx(nums, mid+1, high)

    def partition(nums, low, high):
        idx = random.randint(low, high)
        nums[idx], nums[high] = nums[high], nums[idx]

        i = low
        for j in range(low, high):
            if nums[j] < nums[high]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
    
    def partition2(nums, low, high):
        idx = random.randint(low, high)
        nums[idx], nums[high] = nums[high], nums[idx]
        pivot = nums[high]

        i, j = low, high
        while i < j:
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
            while i < j and nums[j] > pivot:
                j -= 1
            nums[i] = nums[j]
        nums[i] = pivot
        return i

    quick_sort_idx(nums, 0, len(nums)-1)

if __name__ == '__main__':
    nums = [3,2,1,5,4,6,7]
    merge_sort(nums)
    print(nums)
    nums = [3,2,1,5,4,6,7]
    quick_sort(nums)
    print(nums)