# 获取逆序度
def merge_sort_counting(nums):
    def merge_sort_counting_by_idx(nums, low, high):
        if low < high:
            mid = low + ((high-low)>>1)
            merge_sort_counting_by_idx(nums, low, mid)
            merge_sort_counting_by_idx(nums, mid+1, high)
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
                nonlocal ans
                ans += mid - i + 1
        start, end = (i, mid) if i <= mid else (j, high)
        tmp.extend(nums[start:end+1])
        nums[low:high+1] = tmp
    
    ans = 0
    merge_sort_counting_by_idx(nums, 0, len(nums)-1)
    return ans

nums = [5, 0, 4, 2, 3, 1, 3, 3, 3, 6, 8, 7]
print(merge_sort_counting(nums)) # 17
print(nums)