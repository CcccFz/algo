from typing import List

def bubble_sort(nums: List[int]):
    size = len(nums)
    if size <= 1:
        return
    for i in range(size-1):
        flag = False
        for j in range(size-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break

def insert_sort(nums: List[int]):
    size = len(nums)
    if size <= 1:
        return
    for i in range(1, size):
        j = i - 1
        num = nums[i]
        while j >= 0 and num < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = num

def select_sort(nums: List[int]):
    size = len(nums)
    if size <= 1:
        return
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