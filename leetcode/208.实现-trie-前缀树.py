#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Node:
    def __init__(self, c):
        self.c = c
        self.is_end = False
        self.childs = [None] * 26

class Trie:
    def __init__(self):
        self.root = Node('/')

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.childs[idx] is None:
                cur.childs[idx] = Node(c)
            cur = cur.childs[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.childs[idx] is None:
                return False
            cur = cur.childs[idx]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c)-ord('a')
            if cur.childs[idx] is None:
                return False
            cur = cur.childs[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))      # True