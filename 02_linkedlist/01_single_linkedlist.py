from linked_node import Node

class Linkedlist:
    def __init__(self):
        self.head = Node()
        self.len = 0

    def insert(self, idx, val):
        if idx < 0 or idx > self.len:
            return False
        node = Node(val)
        cur = self.head
        while idx:
            cur = cur.next
            idx -= 1
        node.next = cur.next
        cur.next = node
        self.len += 1
        return True

    def delete(self, idx):
        if idx < 0 or idx >= self.len:
            return False
        cur = self.head
        while idx:
            cur = cur.next
            idx -= 1
        cur.next = cur.next.next
        self.len -= 1
        return True

    def __repr__(self):
        cur = self.head.next
        ret = []
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return ','.join(ret)


l = Linkedlist()
l.insert(0, 'a')
l.insert(1, 'c')
l.insert(1, 'b')
print(l)
l.delete(1)
print(l)
