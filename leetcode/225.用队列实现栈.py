#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
# 法一： 两个队列
class MyStack:
    def __init__(self):
       self.queue = deque()
       self.push_queue = deque()

    def push(self, x: int) -> None:
        self.push_queue.append(x)
        while self.queue:
            self.push_queue.append(self.queue.popleft())
        self.queue, self.push_queue = self.push_queue, self.queue

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

# 法二： 一个队列
class MyStack2:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        size = len(self.queue)
        while size > 1:
            self.queue.append(self.queue.popleft())
            size -= 1

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())  # 返回 2
print(myStack.pop())  # 返回 2
print(myStack.empty()) # 返回 False