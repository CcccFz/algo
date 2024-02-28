class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashMap:
    def __init__(self, cap):
        self.new, self.old = [None] * cap, []
        self.len = 0

    def add(self, key, val):
        if self.len / len(self.new) >= 2:
            self.old, self.new = self.new, [None] * (len(self.new)* 2)

        idx = self.hash_new(key)

        if not self.new[idx]:
            self.new[idx] = Node(key, val)
        else:
            cur = self.new[idx]
            while cur.next:
                cur = cur.next
            cur.next = Node(key, val)
        self.len += 1

    def get(self, key):
        for i, node in enumerate(self.old):
            if not node:
                continue
            prev = node
            while node.next:
                prev = node
                node = node.next
            if prev == node:
                self.old[i] = None
            else:
                prev.next = None
            self.len -= 1
            self.add(node.key, node.val)
            break
                
        idx = self.hash_new(key)
        if self.new[idx]:
            cur = self.new[idx]
            while cur:
                if cur.key == key:
                    return cur.val
                cur = cur.next

        idx = self.hash_old(key)
        if self.old[idx]:
            cur = self.old[idx]
            while cur:
                if cur.key == key:
                    return cur.val
                cur = cur.next

        return None

    def hash_new(self, key):
        return key % len(self.new)
    
    def hash_old(self, key):
        return key % len(self.old)

# hash
# 冲突链
# 扩容

h = HashMap(2)
h.add(0, 'a')
h.add(1, 'b')
h.add(2, 'c')
h.add(3, 'd')

h.add(4, 'e')
h.add(5, 'f')
h.add(6, 'g')
h.add(7, 'h')

for i in range(8):
    print(h.get(i), end=', ')

print(h.old)