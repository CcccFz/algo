def bsearch_first(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + ((right-left)>>1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if (mid == 0) or (nums[mid-1] != target):
                return mid
            else:
                right = mid - 1
    return -1

def bsearch_last(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + ((right-left)>>1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if (mid == len(nums)-1) or (nums[mid+1] != target):
                return mid
            else:
                left = mid + 1
    return -1

def bsearch_first_not_less(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + ((right-left)>>1)
        if nums[mid] < target:
            left = mid + 1
        else:
            if (mid == 0) or (nums[mid-1] < target):
                return mid
            else:
                right = mid - 1
    return -1

def bsearch_last_not_greater(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + ((right-left)>>1)
        if nums[mid] > target:
            right = mid - 1
        else:
            if (mid == len(nums)-1) or (nums[mid+1] > target):
                return mid
            else:
                left = mid + 1
    return -1

a = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22]
print(bsearch_first(a, 0) == -1)
print(bsearch_first(a, 7) == 6)
print(bsearch_first(a, 6) == 5)
print(bsearch_first(a, 30) == -1)

print(bsearch_last(a, 0) == -1)
print(bsearch_last(a, 7) == 9)
print(bsearch_last(a, 6) == 5)
print(bsearch_last(a, 30) == -1)

print(bsearch_first_not_less(a, 0) == 0)
print(bsearch_first_not_less(a, 5) == 5)
print(bsearch_first_not_less(a, 6) == 5)
print(bsearch_first_not_less(a, 7) == 6)
print(bsearch_first_not_less(a, 30) == -1)

print(bsearch_last_not_greater(a, 0) == -1)
print(bsearch_last_not_greater(a, 6) == 5)
print(bsearch_last_not_greater(a, 7) == 9)
print(bsearch_last_not_greater(a, 8) == 9)
print(bsearch_last_not_greater(a, 30) == 11)