class Stack:
    def __init__(self, cap):
        self.data = []
        self.cap = cap
        self.len = 0
    
    def push(self, val):
        if self.len == self.cap:
            return False
        self.data.append(val)
        self.len += 1
        return True

    def pop(self):
        if self.len > 0:
            val = self.data.pop()
            self.len -= 1
            return val

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