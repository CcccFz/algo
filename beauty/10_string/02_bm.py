# BM算法  Boyer-Moore

def bm(s, sub):
    def gen_bc(sub):
        bc = [-1] * 128
        for i, c in enumerate(sub):
            bc[ord(c)] = i
        return bc
    
    def gen_gs(sub, m):
        suffix, preffix = [-1] * m, [False] * m
        for i in range(m-1):
            j = i
            k = 0
            while j >= 0 and sub[j] == sub[m-1-k]:
                k += 1
                suffix[k] = j
                j -= 1
            if j < 0:
                preffix[k] = True
        return suffix, preffix

    def step_by_gs(suffix, preffix, m, j):
        k = m-1-j
        if suffix[k] != -1:
            return j-suffix[k]+1
        for r in range(j+2, m):
            if preffix[m-r]:
                return r
        return m

    n, m = len(s), len(sub)
    bc = gen_bc(sub)
    suffix, preffix = gen_gs(sub, m)
    i = 0
    while i <= n-m:
        j = m-1
        while j >= 0 and sub[j] == s[i+j]:
            j -= 1
        if j < 0:
            return i
        step_bc = j-bc[ord(s[i+j])]
        step_gs = 0
        if j < m-1:
            step_gs = step_by_gs(suffix, preffix, m, j)
        i += max(step_bc, step_gs)
    return -1

s = 'abckdekgeekffrascd'
print(bm(s, 'geek'))  # 7