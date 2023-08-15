class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Queue:
    def __init__(self, cap):
        self.cap, self.len = cap, 0
        self.head = Node()
        self.tail = self.head

    def enqueue(self, val):
        if self.len == self.cap:
            return False
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.len += 1
        return True

    def dequeue(self):
        if self.len == 0:
            return None
        val = self.head.next.val
        self.head.next = self.head.next.next
        self.len -= 1
        if self.len == 0:
            self.tail = self.head
        return val

    def __repr__(self) -> str:
        vals = []
        cur = self.head.next
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return str(vals)


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

q.dequeue()
print(q)
