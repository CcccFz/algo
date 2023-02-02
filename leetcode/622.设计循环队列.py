#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue:
    def __init__(self, k: int):
        self.cap = k + 1
        self.vals = [None] * self.cap
        self.head, self.tail = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.vals[self.tail] = value
        self.tail = (self.tail+1) % self.cap
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head+1) % self.cap
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.vals[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.vals[(self.tail-1+self.cap)%self.cap]
   
    def isEmpty(self) -> bool:
        return self.head == self.tail
   
    def isFull(self) -> bool:
        return (self.tail+1) % self.cap == self.head

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
circularQueue = MyCircularQueue(3)
print(circularQueue.enQueue(1))  # 返回 true
print(circularQueue.enQueue(2))  # 返回 true
print(circularQueue.enQueue(3))  # 返回 true
print(circularQueue.enQueue(4))  # 返回 false，队列已满
print(circularQueue.Rear())      # 返回 3
print(circularQueue.isFull())    # 返回 true
print(circularQueue.deQueue())   # 返回 true
print(circularQueue.enQueue(4))  # 返回 true
print(circularQueue.Rear())      # 返回4 