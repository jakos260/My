class Counter():
    def __init__(self, start, stop, step):
        self.stop = stop
        self.step = step
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start = self.start + self.step
            return x
        else:
            raise StopIteration


print[a for a in Counter(start = 10, stop = 20, step = 2)]
