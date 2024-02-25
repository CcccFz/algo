from linked_node import Node

class Linkedlist:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.len = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, idx, val):
        if idx < 0 or idx > self.len:
            return False
        node = Node(val)
        cur = self.head.next
        while idx:
            cur = cur.next
            idx -= 1
        node.next = cur
        node.prev = cur.prev
        cur.prev.next = node
        cur.prev = node
        self.len += 1
        return True

    def delete(self, idx):
        if idx < 0 or idx >= self.len:
            return False
        cur = self.head.next
        while idx:
            cur = cur.next
            idx -= 1
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.len -= 1
        return True

    def __repr__(self):
        cur = self.head.next
        ret = []
        while cur != self.tail:
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
