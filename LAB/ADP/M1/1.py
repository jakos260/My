class Sum:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.sum = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:

            raise StopIteration

        self.i = self.i + 1
        self.sum = self.sum * self.i
        return self.sum

print([a for a in Sum(100)])