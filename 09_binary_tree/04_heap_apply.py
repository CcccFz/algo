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
        while i//2 and self.items[i].priority < self.items[i//2].priority:
            self.items[i], self.items[i//2] = self.items[i//2], self.items[i]
            i //= 2
        return True

    def dequeue(self):
        if self.len == 0:
            return None
        self.items[1], self.items[self.len] = self.items[self.len], self.items[1]
        item = self.items.pop()
        self.len -= 1
        i = 1
        while True:
            min_i = i
            if i*2 <= self.len and self.items[min_i].priority > self.items[i*2].priority:
                min_i = i*2
            if i*2+1 <= self.len and self.items[min_i].priority > self.items[i*2+1].priority:
                min_i = i*2+1
            if min_i == i:
                break
            self.items[i], self.items[min_i] = self.items[min_i], self.items[i]
            i = min_i
        return item

    def dequeue_all(self):
        while True:
            item = self.dequeue()
            if item is None:
                break
            print(item.priority, item.val)

def top_k(nums, k):
    if len(nums) == 0:
        return []
    length = 0
    ans = [None]
    for num in nums:
        if length < k:
            ans.append(num)
            length += 1
            i = length
            while i//2 and ans[i] < ans[i//2]:
                ans[i], ans[i//2] = ans[i//2], ans[i]
                i //= 2
        else:
            if num <= ans[1]:
                continue
            ans[1] = num
            i = 1
            while True:
                min_i = i
                if i*2 <= k and ans[min_i] > ans[i*2]:
                    min_i = i*2
                if i*2+1 <= k and ans[min_i] > ans[i*2+1]:
                    min_i = i*2+1
                if min_i == i:
                    break
                ans[min_i], ans[i] = ans[i], ans[min_i]
                i = min_i
    return ans[1:]


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