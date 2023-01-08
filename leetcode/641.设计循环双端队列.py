#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int): 
        self.cap = k+1
        self.data = [None] * self.cap
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head + self.cap - 1) % self.cap
        self.data[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.cap
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.cap
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail + self.cap - 1) % self.cap
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.tail+self.cap-1) % self.cap]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return (self.tail + 1) % self.cap == self.head



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

circularDeque = MyCircularDeque(3)
print(circularDeque.insertLast(1))         # true   
print(circularDeque.insertLast(2))         # true
print(circularDeque.insertFront(3))         # true
print(circularDeque.insertFront(4))         # false
print(circularDeque.getRear())      # 2
print(circularDeque.isFull())       # true
print(circularDeque.deleteLast())   # true
print(circularDeque.insertFront(4)) # true
print(circularDeque.getFront())     # 4