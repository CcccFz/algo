def bsearch_first(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == 0 or nums[mid-1] != target:
                return mid
            high = mid - 1
    return -1

def bsearch_last(nums, target):
    low, high = 0, len(nums)-1
    last = high
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == last or nums[mid+1] != target:
                return mid
            low = mid + 1
    return -1

def bsearch_first_not_less(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] < target:
            low = mid + 1
        else:
            if mid == 0 or nums[mid-1] < target:
                return mid
            high = mid - 1
    return -1

def bsearch_last_not_greater(nums, target):
    low, high = 0, len(nums)-1
    last = high
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] > target:
            high = mid - 1
        else:
            if mid == last or nums[mid+1] > target:
                return mid
            low = mid + 1
    return -1

def my_sqrt(x):
    low, high = 0, x
    while low <= high:
        mid = low + (high-low)/2
        ret = mid * mid
        if ret > x:
            high = mid
        else:
            if x - ret <= 0.000001:
                return round(mid, 6)
            else:
                low = mid
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

print(my_sqrt(4))
print(my_sqrt(8))