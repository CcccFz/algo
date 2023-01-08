#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.input, self.output = [], []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        return self.output[-1] if self.output else self.input[0]

    def empty(self) -> bool:
        return not self.input and not self.output


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
