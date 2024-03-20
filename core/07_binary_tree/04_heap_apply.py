import random

class Item:
    def __init__(self, priority, val):
        self.priority = priority
        self.val = val

class PriorityQueue:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items)-1
    
    def enqueue(self, priority, val):
        self.items.append(Item(priority, val))
        i = len(self)
        while i//2 and priority < self.items[i//2].priority:
            self.items[i], self.items[i//2] = self.items[i//2], self.items[i]
            i //= 2

    def dequeue(self):
        if len(self) == 0:
            return
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        item = self.items.pop()
        i, n = 1, len(self)
        while True:
            min_i = i
            if i*2 <= n and self.items[min_i].priority > self.items[i*2].priority:
                min_i = i*2
            if i*2+1 <= n and self.items[min_i].priority > self.items[i*2+1].priority:
                min_i = i*2+1
            if min_i == i: break
            self.items[min_i], self.items[i] = self.items[i], self.items[min_i]
            i = min_i
        return item

    def dequeue_all(self):
        for _ in range(len(self)):
            item = self.dequeue()
            print(item.priority, item.val)

def top_k(nums, k):
    heap = [None]
    n = lambda: len(heap)-1
    for num in nums:
        if n() < k:
            heap.append(num)
            i = n()
            while i//2 and num < heap[i//2]:
                heap[i], heap[i//2] = heap[i//2], heap[i]
                i //= 2
        else:
            if num > heap[1]:
                heap[1] = num
                i = 1
                while True:
                    min_i = i
                    if i*2 <= k and heap[min_i] > heap[i*2]:
                        min_i = i*2
                    if i*2+1 <= k and heap[min_i] > heap[i*2+1]:
                        min_i = i*2+1
                    if min_i == i: break
                    heap[min_i], heap[i] = heap[i], heap[min_i]
                    i = min_i
    return heap[1:]


pq = PriorityQueue()
pq.enqueue(5, 'Watch TV')
pq.enqueue(2, 'Learning')
pq.enqueue(10, 'Go Sleep')
pq.enqueue(0, 'Go Home')
pq.enqueue(7, 'Mobile Games')
pq.dequeue_all()

nums = [i for i in range(1, 101)]
random.shuffle(nums)
print(top_k(nums, 3))