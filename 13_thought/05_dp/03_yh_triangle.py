def yh_triangle(nums):
    n = len(nums)
    states = [0] * n
    states[0] = nums[0][0]
    for i in range(1, n):
        for j in range(i, -1, -1):
            if j == i:
                states[j] = nums[i][j] + states[j-1]
            elif j == 0:
                states[j] = nums[i][j] + states[j]
            else:
                states[j] = nums[i][j] + min(states[j-1], states[j])
    return min(states)


nums = [
    [3],
    [2, 6],
    [5, 4, 2],
    [6, 0, 3, 2],
]
print(yh_triangle(nums))   # 9
