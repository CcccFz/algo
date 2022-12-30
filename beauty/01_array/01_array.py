class Array:
    def __init__(self, cap):
        self.data = []
        self.cap = cap
        self.len = 0

    def insert(self, idx, val):
        if idx >= self.cap:
            return
        self.data.insert(idx, val)
        self.len += 1

    def pop(self, idx):
        if idx >= self.len:
            return
        self.data.pop(idx)
        self.len -= 1

    def get(self, idx):
        if idx >= self.len:
            return None
        return self.data[idx]

    def find(self, val):
        for i, v in enumerate(self.data):
            if v == val:
                return i
        return None

    def print(self):
        print(self.data)

arr = Array(2)
arr.insert(1, 'b')
arr.insert(0, 'a')
arr.print()
print(arr.get(1))
arr.pop(1)
arr.print()
arr.pop(0)
arr.print()
arr.insert(0, 'c')
arr.insert(1, 'd')
arr.pop(0)
arr.print()

arr.insert(2, 'e')
# l.get(2)
# l.pop(2)