class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = 0
        self.data = [None] * cap
        
    def push(self, val):
        if self.top == self.cap:
            return False
        self.data[self.top] = val
        self.top += 1
        return True

    def pop(self):
        if self.top == 0:
            return None
        val = self.data[self.top-1]
        self.top -= 1
        return val

    def __repr__(self):
        return str(self.data[:self.top])

stack = Stack(2)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)

stack.pop()
stack.pop()
stack.pop()
print(stack)

stack.push(2)
stack.push(1)
print(stack)

stack.pop()
print(stack)