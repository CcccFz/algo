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


def heap_sort(nums: List[int]):
    def heapify(nums, i, high):
        while True:
            max_i = i
            if i*2+1 <= high and nums[i*2+1] > nums[max_i]:
                max_i = i*2+1
            if i*2+2 <= high and nums[i*2+2] > nums[max_i]:
                max_i = i*2+2
            if max_i == i:
                break
            nums[max_i], nums[i] = nums[i], nums[max_i]
            i = max_i

    def build_heap(nums, high):
        for i in range((high-1)//2, -1, -1):
            heapify(nums, i, high)

    high = len(nums)-1
    build_heap(nums, high)
    while high:
        nums[0], nums[high] = nums[high], nums[0]
        high -= 1
        heapify(nums, 0, high)

if __name__ == '__main__':
    nums = [3,2,1,5,4,6,7]
    merge_sort(nums)
    print(nums)
    
    nums = [3,2,1,5,4,6,7]
    quick_sort(nums)
    print(nums)

    nums = [3,2,1,5,4,6,7]
    heap_sort(nums)
    print(nums)