import math

# 大顶堆
class Heap:
    def __init__(self, cap, vals=None):
        self.cap, self.len = cap, 0
        self.vals = [None] * (cap+1)
        for val in vals:
            self.insert(val)

    def insert(self, val):
       if self.len == self.cap:
           return False
       self.len += 1
       self.vals[self.len] = val
       i = self.len
       while i//2 and self.vals[i] > self.vals[i//2]:
           self.vals[i], self.vals[i//2] = self.vals[i//2], self.vals[i]
           i //= 2
       return True
    
    def remove_top(self):
        if self.len == 0:
            return False
        self.vals[1] = self.vals[self.len]
        self.len -= 1
        self.heapify(1)
        return True
    
    def heapify(self, i):
        while True:
            max_i = i
            if i*2 <= self.len and self.vals[max_i] < self.vals[i*2]:
                max_i = i*2
            if i*2+1 <= self.len and self.vals[max_i] < self.vals[i*2+1]:
                max_i = i*2+1
            if max_i == i:
                break
            self.vals[i], self.vals[max_i] = self.vals[max_i], self.vals[i]
            i = max_i

    def draw(self):
        if self.len == 0:
            return
        ret = []
        level = math.ceil((self.len+1)/2)
        for i in range(level):
            ret.append([None]*2**i)
        queue = [(1, self.vals[1])]
        level = 1
        while queue:
            i, val = queue.pop(0)
            if i >= 2**level:
                print(ret[level-1])
                level += 1
            if val is not None:
                if i <= self.len:
                    ret[level-1][i%2**(level-1)] = val
                queue.append((i*2, self.vals[i*2]))
                queue.append((i*2+1, self.vals[i*2+1]))

    def __repr__(self) -> str:
        print(self.len)
        print(self.vals[1:self.len+1])
        self.draw()
        return ''
            
heap = Heap(100, [7,17,5,13,15,1,8,6,16,21,2,9,33])
print(heap)

heap.insert(18)
print(heap)

heap.remove_top()
print(heap)

heap.insert(19)
print(heap)

heap.remove_top()
print(heap)

heap.remove_top()
print(heap)