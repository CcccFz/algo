def bsearch_first(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + ((r-l)>>1)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            if mid == 0 or nums[mid-1] != target:
                return mid
            r = mid - 1
    return -1

def bsearch_last(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + ((r-l)>>1)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            if mid == len(nums)-1 or nums[mid+1] != target:
                return mid
            l = mid + 1
    return -1

def bsearch_first_not_less(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + ((r-l)>>1)
        if nums[mid] < target:
            l = mid + 1
        else:
            if mid == 0 or nums[mid-1] < target:
                return mid
            r = mid - 1
    return -1

def bsearch_last_not_greater(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + ((r-l)>>1)
        if nums[mid] > target:
            r = mid - 1
        else:
            if mid == len(nums)-1 or nums[mid+1] > target:
                return mid
            l = mid + 1
    return -1

def my_sqrt(x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)/2
        ret = mid * mid
        if ret > x:
            r = mid
        else:
            if x-ret < 0.000001:
                return round(mid, 6)
            else:
                l = mid
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