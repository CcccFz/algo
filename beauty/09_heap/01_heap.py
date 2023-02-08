import math

# 大顶堆
class Heap:
    def __init__(self, cap, vals=None):
        self.cap = cap
        self.vals = [None] * (cap+1)
        self.len = 0
        for val in vals:
            self.insert(val)

    def insert(self, val):
        if self.len == self.cap:
            return False

        self.len += 1
        self.vals[self.len] = val

        # 从下到上堆化
        i = self.len
        while i//2 and self.vals[i] > self.vals[i//2]:
            self.vals[i], self.vals[i//2] = self.vals[i//2], self.vals[i]
            i = i//2

        return True
    
    def remove_max(self):
        if self.len == 0:
            return False
        
        self.vals[1] = self.vals[self.len]
        self.len -= 1

        # 从上到下堆化
        self.heapify(1)
        return True
    
    def heapify(self, i):
        while True:
            max_i = i
            if i*2 <= self.len and self.vals[i*2] > self.vals[i]:
                max_i = i*2
            if i*2+1 <= self.len and self.vals[i*2+1] > self.vals[max_i]:
                max_i = i*2+1
            if max_i == i:
                break
            self.vals[i], self.vals[max_i] = self.vals[max_i], self.vals[i]
            i = max_i

    def draw(self):
        def split_level(s):
            cnt = 0
            for i, c in enumerate(s):
                if c == ',': cnt += 1
                if cnt == 2**(level-2):
                    s = s[0:i]+' ;'+s[i+1:]
                    break
            return s

        if self.len == 0:
            return
        level = math.ceil(math.log(self.len+1, 2))
        ret = []
        for i in range(level):
            ret.append([None]*2**i)
        
        level = 1
        queue = [(1,self.vals[1])]
        while queue:
            i, val = queue.pop(0)
            if i >= 2**level:     
                print(split_level(str(ret[level-1])[1:-1]))
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

heap.remove_max()
print(heap)

heap.insert(19)
print(heap)

heap.remove_max()
print(heap)

heap.remove_max()
print(heap)