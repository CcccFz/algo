class Node:
    def __init__(self, c):
        self.c = c
        self.childs = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, s):
        cur = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if cur.childs[idx] is None:
                cur.childs[idx] = Node(c)
            cur = cur.childs[idx]
        cur.is_end =True

    def start_with(self, s):
        cur = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if cur.childs[idx] is None:
                return False
            cur = cur.childs[idx]
        return True

    def find(self, s):
        cur = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if cur.childs[idx] is None:
                return False
            cur = cur.childs[idx]
        return cur.is_end

if __name__ == '__main__':
    ss = ["how", "hi", "her", "hello", "so", "see"]
    trie = Trie()

    for s in ss:
        trie.insert(s)

    print(trie.find("hell"))
    print(trie.find("se"))
    print(trie.start_with("hell"))
    print(trie.start_with("se"))
    print(trie.find("hello"))
    print(trie.find("see"))
    print(trie.find("swift"))