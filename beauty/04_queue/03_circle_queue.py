class CircleQueue:
    def __init__(self, cap):
        self.cap = cap + 1
        self.data = [None] * self.cap
        self.head, self.tail = 0, 0

    def enqueue(self, val):
        if (self.tail + 1) % self.cap == self.head:
            return False
        self.data[self.tail] = val
        self.tail = (self.tail+1) % self.cap
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        val = self.data[self.head]
        self.head = (self.head+1) % self.cap
        return val

    def __repr__(self) -> str:
        ret = []
        cur = self.head
        while cur != self.tail:
            ret.append(str(self.data[cur]))
            cur = (cur + 1) % self.cap
        return '->'.join(ret)


q = CircleQueue(3)
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