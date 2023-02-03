#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack = []
        self.push_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            while self.push_stack:
                self.stack.append(self.push_stack.pop())
        return self.stack.pop()

    def peek(self) -> int:
        if not self.stack:
            while self.push_stack:
                self.stack.append(self.push_stack.pop())                
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.push_stack and not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
myQueue = MyQueue()
print(myQueue.push(1))  # queue is: [1]
print(myQueue.push(2))  # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())   # return 1
print(myQueue.pop())    # return 1, queue is [2]
print(myQueue.empty())  # return false
