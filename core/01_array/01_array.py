class Array:
    def __init__(self, cap):
        self.cap = cap
        self.len = 0
        self.data = [None] * cap

    def insert(self, idx, val):
        if self.len == self.cap:
            return False
        if idx > self.len:
            return False
        if idx < self.len:
            for i in range(self.len, idx, -1):
                self.data[i] = self.data[i-1]
        self.data[idx] = val
        self.len += 1
        return True

    def delete(self, idx):
        if self.len == 0:
            return False
        last = self.len-1
        if idx > last:
            return False
        if idx < last:
            for i in range(idx, last):
                self.data[i] = self.data[i+1]
        self.len -= 1
        return True

    def get(self, idx):
        if idx < self.len:
            return self.data[idx]

    def find(self, val):
        for i in range(self.len):
            if self.data[i] == val:
                return i
        return -1

    def __repr__(self):
        return str(self.data[:self.len])


arr = Array(2)
arr.insert(1, 'x')
arr.insert(0, 'a')
arr.insert(1, 'b')
arr.insert(2, 'c')
print(arr)

arr.delete(2)
print(arr)

arr.delete(1)
print(arr)

arr.insert(0, 'b')
print(arr)
