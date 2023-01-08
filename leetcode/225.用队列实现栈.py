#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)
        size = len(self.items)
        while size > 1:
            self.items.append(self.items.pop(0))
            size -= 1

    def pop(self) -> int:
        if self.empty():
            return
        return self.items.pop(0)

    def top(self) -> int:
        if self.empty():
            return
        return self.items[0]

    def empty(self) -> bool:
        return not self.items



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