import math

def heap_sort(nums):
    def heapify(nums, high, i):
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
            heapify(nums, high, i)
    
    high = len(nums)-1
    build_heap(nums, high)
    while high:
        nums[high], nums[0] = nums[0], nums[high]
        high -= 1
        heapify(nums, high, 0)


nums = [3,2,1,5,4,6,7]
heap_sort(nums)
print(nums)