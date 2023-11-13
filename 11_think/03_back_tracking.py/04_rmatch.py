
class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.plen = len(pattern)
        
    def match(self, text):
        self.is_match = False
        tlen = len(text)
        self.rmatch(text, tlen, 0, 0)
        return self.is_match

    def rmatch(self, text, tlen, ti, pi):
        if self.is_match:
            return
        
        if pi == self.plen:
            if ti == tlen:
                self.is_match = True
            return
        
        if self.pattern[pi] == '*':
            for j in range(tlen-ti+1):
                self.rmatch(text, tlen, ti+j, pi+1)
        elif self.pattern[pi] == '?':
            self.rmatch(text, tlen, ti, pi+1)
            self.rmatch(text, tlen, ti+1, pi+1)
        elif ti < tlen and text[ti] == self.pattern[pi]:
            self.rmatch(text, tlen, ti+1, pi+1)


texts = ['asd', 'aaaasd', 'aaaasdddd', 'aaaaasd', 'aaaaadddd']
pattern = Pattern('a*s?d*')
for text in texts:
    print(pattern.match(text))