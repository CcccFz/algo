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
            return
        node = Node(val)
        node.next = self.top
        self.top = node
        self.len += 1
    
    def pop(self):
        if self.len == 0:
            return
        self.top = self.top.next
        self.len -= 1
    
    def print(self):
        cur = self.top
        items = []
        while cur:
            items.append(str(cur.val))
            cur = cur.next
        print('[' + ' -> '.join(items) + ']')

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