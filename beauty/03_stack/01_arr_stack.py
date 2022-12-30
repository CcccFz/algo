class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.data = []
        self.len = 0
    
    def push(self, val):
        if self.len == self.cap:
            return
        self.data.append(val)
        self.len += 1
    
    def pop(self):
        if self.len == 0:
            return
        self.data.pop()
        self.len -= 1

    def print(self):
        print(self.data)

stack = Stack(2)
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
stack.pop()
stack.pop()
stack.pop()
stack.print()
stack.push(2)
stack.push(1)
stack.print()