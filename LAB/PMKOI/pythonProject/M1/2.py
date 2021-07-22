class Power:
    def __init__(self, a, n):
        self.n = n
        self.a = a
        self.i = 0
        self.pow = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i = self.i + 1
        self.pow = self.pow * self.a
        return self.pow

print([a for a in Power(10,1000)])