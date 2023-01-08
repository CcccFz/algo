class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self, cap):
        self.cap = cap
        self.len = 0
        self.head = Node(None)
        self.tail = self.head

    def enqueue(self, val):
        if self.len == self.cap:
            return
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.len += 1

    def dequeue(self):
        if self.len == 0:
            return
        self.head.next = self.head.next.next
        self.len -= 1
        if self.len == 0:
            self.tail = self.head
    
    def __repr__(self) -> str:
        ret = []
        cur = self.head.next
        while cur:
            ret.append(str(cur.val))
            cur = cur.next
        return '->'.join(ret)


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
q.dequeue()
q.dequeue()
q.dequeue()
print(q)
q.enqueue(1)
q.enqueue(2)
print(q)