#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.pop_from(node)
            self.insert_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.pop_from(node)
            self.insert_to_head(node)
        else:
            if len(self.dic) == self.cap:
                node = self.pop_from_tail()
                self.dic.pop(node.key)
            node = Node(key, value)
            self.insert_to_head(node)
            self.dic[key] = node

    def insert_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def pop_from(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def pop_from_tail(self):
        return self.pop_from(self.tail.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))
print(lru.get(2))
lru.put(3,3)
print(lru.get(3))
print(lru.get(1))
lru.put(4,4)
print(lru.get(4))
print(lru.get(2))
