
def match(s, p):
    def rmatch(s, p, si, pi):
        nonlocal is_match
        if is_match:
            return
        if pi == len(p):
            if si == len(s):
                is_match = True
            return
        if p[pi] == '*':
            for i in range(si, len(s)+1):
                rmatch(s, p, i, pi+1)    
        elif p[pi] == '?':
            rmatch(s, p, si, pi+1)
            rmatch(s, p, si+1, pi+1)
        elif si < len(s) and p[pi] == s[si]:
            rmatch(s, p, si+1, pi+1)

    is_match = False
    rmatch(s, p, 0, 0)
    return is_match


texts = ['asd', 'aaaasd', 'aaaasdddd', 'aaaaasd', 'aaaaadddd']
for text in texts:
    print(match(text, 'a*s?d*'))