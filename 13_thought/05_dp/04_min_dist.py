import math

MIN_DIST = math.inf
def min_dist_back_tracking(matrix, n, i, j, dist):
    if (i == n and j == n-1) or (i == n-1 and j == n):
        global MIN_DIST
        if dist < MIN_DIST:
            MIN_DIST = dist
        return
    if i < n and j < n:
        min_dist_back_tracking(matrix, n, i+1, j, dist+matrix[i][j])
        min_dist_back_tracking(matrix, n, i, j+1, dist+matrix[i][j])

def min_dist_dp_table(matrix):
    n = len(matrix)
    states = [0] * n
    for j in range(n):
        states[j] = matrix[0][j] + (states[j-1] if j > 0 else 0)
    for i in range(1, n):
        for j in range(n):
            states[j] = matrix[i][j] + (min(states[j-1], states[j]) if j > 0 else states[j])
    return states[n-1]

def min_dist_formula(matrix, memo, i, j):
    if i == 0 and j == 0:
        return matrix[0][0]
    if memo[i][j] > 0:
        return memo[i][j]
    left = min_dist_formula(matrix, memo, i, j-1) if j > 0 else math.inf
    top = min_dist_formula(matrix, memo, i-1, j) if i > 0 else math.inf
    memo[i][j] = matrix[i][j] + min(left, top)
    return memo[i][j]

if __name__ == "__main__":
    matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    min_dist_back_tracking(matrix, 4, 0, 0, 0)
    print(MIN_DIST)
    print(min_dist_dp_table(matrix))
    print(min_dist_formula(matrix, [[0]*4 for _ in range(4)], 3, 3))
