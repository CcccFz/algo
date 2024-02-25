class Array:
    def __init__(self, cap):
        self.cap = cap
        self.len = 0
        self.data = [None] * cap
    
    def append(self, val):
        if self.len == self.cap:
            return False
        self.data[self.len] = val
        i = self.len
        while i > 0 and self.data[i] < self.data[i-1]:
            self.data[i], self.data[i-1] = self.data[i-1], self.data[i]
            i -= 1
        self.len += 1
        return True

    def delete(self, idx):
        if idx < 0 or idx >= self.len:
            return False
        if self.len == 0:
            return False
        for i in range(idx, self.len-1):
            self.data[i] = self.data[i+1]
        self.len -= 1
        return True

    def __repr__(self):
        return str(self.data[:self.len])
    
arr = Array(5)
arr.append(4)
arr.append(2)
arr.append(5)
arr.append(3)
arr.append(1)
print(arr)
arr.delete(3)
print(arr)