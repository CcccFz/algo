def yh_triangle(nums):
    n = len(nums)
    state = [[0]*n for _ in range(n)]
    state[0][0] = nums[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                state[i][j] = nums[i][j] + state[i-1][j]
            elif j == i:
                state[i][j] = nums[i][j] + state[i-1][j-1]
            else:
                state[i][j] = nums[i][j] + min(state[i-1][j-1], state[i-1][j])
    return min(state[-1])

def yh_triangle2(nums):
    n = len(nums)
    state = [0] * n
    state[0] = nums[0][0]

    for i in range(1, n):
        for j in range(i, -1, -1):
            if j == i:
                state[j] = nums[i][j] + state[j-1]
            elif j == 0:
                state[j] = nums[i][j] + state[j]
            else:
                state[j] = nums[i][j] + min(state[j-1], state[j])
    return min(state)

if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle(nums))   # 9
    print(yh_triangle2(nums))  # 9