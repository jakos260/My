class FB:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.n:
            raise StopIteration

        self.i += 1
        if not self.i % 3:
            return 'Fizz'
        elif not self.i % 5:
            return 'Buzz'
        else:
            return self.i

x = input()
x = int(x)
print([a for a in FB(x)])
