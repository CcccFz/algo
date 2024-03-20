class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BinarySearchTree():
    def __init__(self, vals):
        self.root = None
        for val in vals:
            self.insert(val)
    
    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        cur = self.root
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = node
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = node
                    return
                cur = cur.right

    def search(self, val):
        parents, nodes = [], []
        parent, cur = None, self.root
        while cur:
            if val < cur.val:
                parent, cur = cur, cur.left
            else:
                if val == cur.val:
                    parents.append(parent)
                    nodes.append(cur)
                parent, cur = cur, cur.right
        return parents, nodes

    def delete(self, val):
        parents, nodes = self.search(val)
        while nodes:
            self.delete_node(parents[0], nodes[0])
            parents, nodes = self.search(val)

    def delete_node(self, parent, cur):
        if cur.left and cur.right:
            min_parent, min_node = cur, cur.right
            while min_node.left:
                min_parent, min_node = min_node, min_node.left
            cur.val = min_node.val
            parent, cur = min_parent, min_node
        
        child = cur.left if cur.left else cur.right

        if not parent:
            self.root = child
        elif parent.left == cur:
            parent.left = child
        else:
            parent.right = child

    def min(self):
        if not self.root:
            return
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val

    def max(self):
        if not self.root:
            return
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.val

    def depth(self):
        def dfs(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 0
            else:
                return max(dfs(root.left), dfs(root.right)) + 1
        return dfs(self.root)

    def in_order(self):
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ret.append(root.val)
            dfs(root.right)
        ret = []
        dfs(self.root)
        print(ret)
    
    def bfs(self):
        ret = []
        queue = []
        if self.root:
            queue.append(self.root)
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                ret.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print(ret)

    def __repr__(self):
        self.in_order()
        self.bfs()
        return ''

if __name__ == '__main__':
    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)

    bst.insert(1)
    bst.insert(4)
    print(bst)

    parents, nodes = bst.search(2)
    for i in range(len(nodes)):
        print(parents[i].val, nodes[i].val)

    bst.insert(6)
    bst.insert(7)
    print(bst)

    bst.delete(7)
    print(bst)

    bst.delete(6)
    print(bst)

    bst.delete(4)
    print(bst)

    print(bst.max())
    print(bst.min())



"""
[1, 2, 3, 4, 5, 6, 7]
4
2, 5
1, 3, None, 6
None, None, None, None, None, None, None, 7

[1, 1, 2, 3, 4, 4, 5, 6, 7]
4
2, 5
1, 3, 4, 6
None, 1, None, None, None, None, None, 7

4 2
[1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7]
4
2, 5
1, 3, 4, 6
None, 1, None, None, None, None, None, 7
None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6, 7

[1, 1, 2, 3, 4, 4, 5, 6, 6]
4
2, 5
1, 3, 4, 6
None, 1, None, None, None, None, None, 6

[1, 1, 2, 3, 4, 4, 5]
4
2, 5
1, 3, 4, None
None, 1, None, None, None, None, None, None

[1, 1, 2, 3, 5]
5
2, None
1, 3, None, None
None, 1, None, None, None, None, None, None

5
1
"""