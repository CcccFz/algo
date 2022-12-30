#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(None, -1)
        self.tail = Node(None, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.move_to_first(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            self.move_to_first(node)
            node.value = value 
        else:
            if len(self.hash) == self.capacity:
                end = self.tail.prev
                self.pop_node(end)
                self.hash.pop(end.key)
            node = Node(key, value)
            self.insert_to_first(node)
            self.hash[key] = node

    def move_to_first(self, node):
        self.pop_node(node)
        self.insert_to_first(node)

    def pop_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_to_first(self, node):
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node        

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
