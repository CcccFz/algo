def heap_sort(nums):
    def heapify(i, n):
        while True:
            min_i = i
            if i*2+1 <= n and nums[min_i] > nums[i*2+1]:
                min_i = i*2+1
            if i*2+2 <= n and nums[min_i] > nums[i*2+2]:
                min_i = i*2+2
            if min_i == i: break
            nums[min_i], nums[i] = nums[i], nums[min_i]
            i = min_i    

    def build_heap():
        for i in range((r-1)//2, -1, -1):
            heapify(i, r)
    
    r = len(nums)-1
    build_heap()
    while r:
        nums[0], nums[r] = nums[r], nums[0]
        r -= 1
        heapify(0, r)


nums = [3,2,1,5,4,6,7]
heap_sort(nums)
print(nums)