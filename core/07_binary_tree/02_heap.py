# 小顶堆

class Heap:
    def __init__(self, cap, vals=None):
        self.cap, self.len = cap, 0
        self.vals = [None] * (cap+1)
        for val in vals:
            self.push(val)

    def push(self, val):
       if self.len == self.cap:
           return
       self.len += 1
       self.vals[self.len] = val
       i = self.len
       while i//2 and self.vals[i] < self.vals[i//2]:
           self.vals[i], self.vals[i//2] = self.vals[i//2], self.vals[i]
           i //= 2

    def pop(self):
        if self.len == 0:
            return
        self.vals[1] = self.vals[self.len]
        self.len -= 1
        self.heapify(1)
        return self.vals[self.len+1]
    
    def heapify(self, i):
        while True:
            min_i = i
            if i*2 <= self.len and self.vals[min_i] > self.vals[i*2]:
                min_i = i*2
            if i*2+1 <= self.len and self.vals[min_i] > self.vals[i*2+1]:
                min_i = i*2+1
            if min_i == i: break
            self.vals[min_i], self.vals[i] = self.vals[i], self.vals[min_i]
            i = min_i

    def __repr__(self):
        print(self.len)
        print(self.vals[1:self.len+1])
        return ''


heap = Heap(100, [7,17,5,13,15,1,8,6,16,21,2,9,33])
print(heap)

heap.push(18)
print(heap)

heap.pop()
print(heap)

heap.push(19)
print(heap)

heap.pop()
print(heap)

heap.pop()
print(heap)
