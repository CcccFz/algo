def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        flag = False
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break

def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        j = i - 1
        num = nums[i]
        while j >= 0 and num < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = num

def select_sort(nums):
    n = len(nums)
    for i in range(n):
        min = i
        for j in range(i+1, n):
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