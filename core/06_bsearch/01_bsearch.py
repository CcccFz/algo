def bsearch(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + ((r-l)>>1)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1

def bsearch_recursion(nums, target):
    def bsearch_idx(l, r):
        if l > r:
            return -1
        mid = l + ((r-l)>>1)
        if nums[mid] < target:
            return bsearch_idx(mid+1, r)
        elif nums[mid] > target:
            return bsearch_idx(l, mid-1)
        else:
            return mid
    
    return bsearch_idx(0, len(nums)-1)

print(bsearch([-1,0,3,5,9,12], target = 9))
print(bsearch_recursion([-1,0,3,5,9,12], target = 9))
