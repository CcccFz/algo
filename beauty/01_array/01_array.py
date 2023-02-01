class Array:
    def __init__(self, cap):
        self.data = []
        self.cap = cap
        self.len = 0

    def insert(self, idx, val):
        if self.len == self.cap:
            return False
        self.data.insert(idx, val)
        self.len += 1
        return True

    def delete(self, idx):
        if idx >= self.len:
            return False
        self.data.pop(idx)
        self.len -= 1
        return True

    def get(self, idx):
        if idx < self.len:
            return self.data[idx]

    def find(self, val):
        for i, v in enumerate(self.data):
            if val == v:
                return i
        return -1

    def print(self):
        print(self.data)

arr = Array(2)
arr.insert(1, 'b')
arr.insert(0, 'a')
arr.print()
print(arr.get(1))
arr.delete(1)
arr.print()
arr.delete(0)
arr.print()
arr.insert(0, 'c')
arr.insert(1, 'd')
arr.delete(0)
arr.print()

arr.insert(2, 'e')