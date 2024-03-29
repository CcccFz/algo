import random

def merge_sort(nums):
    def merge_sort_idx(l, r):
        if l < r:
            mid = l + ((r-l)>>1)
            merge_sort_idx(l, mid)
            merge_sort_idx(mid+1, r)
            merge(l, mid, r)

    def merge(l, mid, r):
        i, j = l, mid+1
        tmp = []
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        start, end = (i, mid) if i <= mid else (j, r)
        tmp.extend(nums[start:end+1])
        nums[l:r+1] = tmp

    return merge_sort_idx(0, len(nums)-1)

def quick_sort(nums):
    cnt = 0

    def quick_sort_idx(l, r):
        if l < r:
            mid = partition(l, r)
            quick_sort_idx(l, mid-1)
            quick_sort_idx(mid+1, r)

    def partition(l, r):
        mid = random.randint(l, r)
        nums[mid], nums[r] = nums[r], nums[mid]

        nonlocal cnt
        if cnt % 2:
            i = l
            for j in range(l, r):
                if nums[j] <= nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
        else:
            pivot = nums[r]
            i, j = l, r
            while i < j:
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
                while i < j and nums[j] > pivot:
                    j -= 1
                nums[i] = nums[j]
            nums[i] = pivot

        cnt += 1
        return i

    return quick_sort_idx(0, len(nums)-1)

def top_k(nums, k):
    def partition(l, r):
        mid = random.randint(l, r)
        nums[mid], nums[r] = nums[r], nums[mid]
        i = l
        for j in range(l, r):
            if nums[j] > nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        
        if i+1 < k:
            return partition(i+1, r)
        elif i+1 > k:
            return partition(l, mid-1)
        else:
            return nums[i]

    return partition(0, len(nums)-1)

if __name__ == '__main__':
    nums = [3,2,1,5,4,6,7]
    merge_sort(nums)
    print(nums)
    
    nums = [3,2,1,5,4,6,7]
    quick_sort(nums)
    print(nums)

    nums = [3,2,1,5,4,6,7]
    print(top_k(nums, 3))
