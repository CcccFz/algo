# Brute-Force 暴力算法
def bf(s, sub):
    n, m = len(s), len(sub)
    if n < m:
        return False
    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] != sub[j]:
                break
            if j == m-1:
                return True
    return False

# Robin-Karp 哈希检索算法
def rk(s, sub):
    def hash(s, start, end):
        ret = 0
        for i in range(start, end):
            ret += ord(s[i])
        return ret

    n, m = len(s), len(sub)
    if n < m:
        return False
    
    hash_sub = hash(sub, 0, m)
    hash_s = hash(s, 0, m)

    for i in range(n-m+1):
        if i > 0:
            hash_s = hash_s-hash(s, i-1, i)+hash(s, i+m-1, i+m)
        if hash_s != hash_s:
            continue
        for j in range(m):
            if s[i+j] != sub[j]:
                break
            if j == m-1:
                return True
    return False

s = 'a'*10000
sub = 'a'*200+'b'
print(bf(s, sub))
print(bf(s, sub[:-1]))

s = 'thequickbrownfoxjumpsoverthelazydog'
sub = 'jump'
print(rk(s, sub+'e'))
print(rk(s, sub))