class Array:
    def __init__(self, cap):
        self.cap = cap
        self.len = 0
        self.data = [None] * cap
    
    def add(self, val):
        if self.len == self.cap:
            self.cap *= 2
            data = [None] * self.cap
            for i in range(self.len):
                data[i] = self.data[i]
            self.data = data
        self.data[self.len] = val
        self.len += 1

    def __repr__(self):
        return str(self.data)

arr = Array(3)
arr.add('a')
arr.add('b')
print(arr)
arr.add('c')
print(arr)
arr.add('d')
print(arr)