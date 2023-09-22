class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

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
            minParent = cur
            minCur = cur.right
            while minCur.left:
                minParent = minCur
                minCur = minCur.left
            cur.val = minCur.val
            parent = minParent
            cur = minCur
        
        child = cur.left if cur.left else cur.right

        if parent == None:
            self.root = child
        elif parent.left == cur:
            parent.left = child
        else:
            parent.right = child    

    def min(self):
        cur = self.root
        if not cur:
            return
        while cur.left:
            cur = cur.left
        return cur.val

    def max(self):
        cur = self.root
        if not cur:
            return
        while cur.right:
            cur = cur.right
        return cur.val

    def depth(self):
        def _depth(cur):
            if not cur:
                return 0
            elif not cur.left and not cur.right:
                return 0
            else:
                return max(_depth(cur.left), _depth(cur.right)) + 1

        return _depth(self.root)

    def in_order(self):
        def _in_order(cur):
            if cur:
                _in_order(cur.left)
                ret.append(cur.val)
                _in_order(cur.right)
        
        ret = []
        _in_order(self.root)
        print(ret)
    
    def bfs(self):
        if not self.root:
            return

        ret = []
        level = self.depth() + 1
        for i in range(level):
            ret.append([None]*2**i)

        level = 1
        queue = [(1, self.root)]
        while queue:
            i, node = queue.pop(0)
            if i >= 2**level:
                print(str(ret[level-1])[1:-1])
                level += 1
            if node:
                ret[level-1][i%2**(level-1)] = node.val
                queue.append((i*2, node.left))
                queue.append((i*2+1, node.right))

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