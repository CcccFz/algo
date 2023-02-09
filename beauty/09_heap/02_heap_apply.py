import random

class Item:
    def __init__(self, priority, val):
        self.priority = priority
        self.val = val

class PriorityQueue:
    def __init__(self):
        self.len = 0
        self.items = [None]
    
    def enqueue(self, priority, val):
        self.len += 1
        self.items.append(Item(priority, val))
        i = self.len
        while i//2 and self.items[i//2].priority > self.items[i].priority:
            self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
            i = i//2
        return True

    def dequeue(self):
        def heapify(i):
            while True:
                min_i = i
                if i*2 <= self.len and self.items[i*2].priority < self.items[min_i].priority :
                    min_i = i*2
                if i*2+1 <= self.len and self.items[i*2+1].priority  < self.items[min_i].priority :
                    min_i = i*2+1
                if min_i == i:
                    break
                self.items[min_i], self.items[i] = self.items[i], self.items[min_i]
                i = min_i
        
        if self.len == 0:
            return
        
        self.items[1], self.items[self.len] = self.items[self.len], self.items[1]
        item = self.items.pop()
        self.len -= 1
        heapify(1)
        return item
        

def top_k(nums, k):
    if len(nums) <= k:
        return nums

    ans = [None]
    length = 0
    for num in nums:
        if length == k:
            if num <= ans[1]:
                continue
            ans[1] = num
            i = 1
            while True:
                min_i = i
                if i*2 <= k and ans[i*2] < ans[i]:
                    min_i = i*2
                if i*2+1 <= k and ans[i*2+1] < ans[i]:
                    min_i = i*2+1
                if min_i == i:
                    break
                ans[min_i], ans[i] = ans[i], ans[min_i]
                i = min_i
        else:
            ans.append(num)
            length += 1
            i = length
            while i//2 and ans[i//2] > ans[i]:
                ans[i], ans[i//2] = ans[i//2], ans[i]
                i = i//2

    return ans[1:]


pq = PriorityQueue()
pq.enqueue(5, 'Watch TV')
pq.enqueue(2, 'Learning')
pq.enqueue(10, 'Go Sleep')
pq.enqueue(0, 'Go Home')
pq.enqueue(7, 'Mobile Games')

while True:
    item = pq.dequeue()
    if not item:
        break
    print(item.priority, item.val)


nums = [i for i in range(1, 101)]
random.shuffle(nums)
print(nums)
print(top_k(nums, 3))