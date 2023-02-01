from typing import List

def bubble_sort(nums: List[int]):
    size = len(nums)
    if size <= 1:
        return nums
    for i in range(size-1):
        is_flag = False
        for j in range(size-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_flag = True
        if not is_flag:
            break

def insert_sort(nums: List[int]):
    size = len(nums)
    if size <= 1:
        return nums
    for i in range(1, size):
        j = i - 1
        num = nums[i]
        while j >= 0 and nums[j] > num:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = num

def select_sort(nums: List[int]):
    size = len(nums)
    if size <= 1:
        return nums
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

nums = [3,2,1,5,4,6,7]
bubble_sort(nums)
print(nums)
nums = [3,2,1,5,4,6,7]
insert_sort(nums)
print(nums)
nums = [3,2,1,5,4,6,7]
select_sort(nums)
print(nums)