#     A
#   /   \
#  B     C
# / \   / \
# D  E  F  G
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
root = Node('A')
b, c = Node('B'), Node('C')
root.left, root.right = b, c
d, e, f, g = Node('D'), Node('E'), Node('F'), Node('G')
b.left, b.right = d, e
c.left, c.right = f, g

def pre_order(cur):
    if cur:
        print(cur.val, end=',')
        pre_order(cur.left)
        pre_order(cur.right)

def in_order(cur):
    if cur:
        in_order(cur.left)
        print(cur.val, end=',')
        in_order(cur.right)

def post_order(cur):
    if cur:
        post_order(cur.left)
        post_order(cur.right)
        print(cur.val, end=',')

pre_order(root)  # A,B,D,E,C,F,G
print()
in_order(root)   # D,B,E,A,F,C,G
print()
post_order(root) # D,E,B,F,G,C,A