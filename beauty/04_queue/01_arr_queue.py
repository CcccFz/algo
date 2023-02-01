class Queue:
    def __init__(self, cap):
        self.cap = cap
        self.head = 0
        self.tail = 0
        self.data = [None] * cap

    def enqueue(self, val):
        if self.tail == self.cap:
            if self.head == 0:
                return False
            else:
                for i in range(self.head, self.tail):
                    self.data[i-self.head] = self.data[i]
                self.tail -= self.head
                self.head = 0
        self.data[self.tail] = val
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return False
        val = self.data[self.head]
        self.head += 1
        return val

    def __repr__(self):
        return '->'.join([str(self.data[i]) for i in range(self.head, self.tail)])

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
q.dequeue()
q.dequeue()
print(q)
q.enqueue(1)
q.enqueue(2)
print(q)