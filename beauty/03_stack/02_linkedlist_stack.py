class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack():
    def __init__(self, cap):
        self.cap = cap
        self.len = 0
        self.top = None

    def push(self, val):
        if self.len == self.cap:
            return False
        node = Node(val)
        node.next = self.top
        self.top = node
        self.len += 1
        return True
    
    def pop(self):
        if self.top is None:
            return 
        val = self.top.val
        self.top = self.top.next
        self.len -= 1
        return True

    def __repr__(self):
        cur = self.top
        vals = []
        while cur:
            vals.insert(0, cur.val)
            cur = cur.next
        return str(vals)

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