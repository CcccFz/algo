import math

a, b = "mitcmu", "mtacnu"

n, m = len(a), len(b)
edist_min = math.inf

def lwstBT(i, j, edist):
    if i == n or j == m:
        global edist_min
        if i < n: edist += n-i
        if j < m: edist += m-j
        if edist < edist_min:
            edist_min = edist
        return
    if a[i] == b[j]:
        lwstBT(i+1, j+1, edist)
    else:
        lwstBT(i+1, j, edist+1)
        lwstBT(i, j+1, edist+1)
        lwstBT(i+1, j+1, edist+1)
    

def lwstDP(a, b):
    dp = [[None]*m for _ in range(n)]
    for j in range(m):
        if a[0] == b[j]: dp[0][j] = j
        elif j == 0: dp[0][j] = 1
        else: dp[0][j] = dp[0][j-1] + 1
    for i in range(n):
        if b[0] == a[i]: dp[i][0] = i
        elif i == 0: dp[i][0] = 1
        else: dp[i][0] = dp[i-1][0] + 1
    for i in range(1, n):
        for j in range(1, m):
            if a[i] == b[j]:
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1]
                )
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] + 1,
                )
    return dp[n-1][m-1]
    

def lcs(a, b):
    dp = [[None]*m for _ in range(n)]
    for j in range(m):
        if a[0] == b[j]: dp[0][j] = 1
        elif j == 0: dp[0][j] = 0
        else: dp[0][j] = dp[0][j-1]
    for i in range(n):
        if b[0] == a[i]: dp[i][0] = 1
        elif i == 0: dp[i][0] = 0
        else: dp[i][0] = dp[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            if a[i] == b[j]:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1]+1,
                )
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1],
                )
    return dp[n-1][m-1]


lwstBT(0, 0, 0)
print(edist_min) # 3
print(lwstDP(a, b)) # 3
print(lcs(a, b))  # 4
