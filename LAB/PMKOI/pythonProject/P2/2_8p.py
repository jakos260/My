class VectorExample():
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return str(self.vector)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if (len(self.vector) != len(other.vector)):
            raise ValueError
        else:
            return [self.vector[i] + other.vector[i] for i in range(len(self.vector))]

    def __sub__(self, other):
        if (len(self.vector) != len(other.vector)):
            raise ValueError
        else:
            return [self.vector[i] - other.vector[i] for i in range(len(self.vector))]

    def __mul__(self, other):
        if (len(self.vector) != len(other.vector)):
            raise ValueError
        else:
            return [self.vector[i] * other.vector[i] for i in range(len(self.vector))]

    def __truediv__(self, other):

        if (len(self.vector) != len(other.vector)):
            raise ValueError
        else:
            for k in range(len(self.vector)):
                if self.vector[k] == 0 or other.vector[k] == 0:
                    raise ZeroDivisionError

            return [self.vector[i] / other.vector[i] for i in range(len(self.vector))]


v1 = VectorExample([1, 2, 3, 4])
v2 = VectorExample([5, 3, 2, 1])
v3 = VectorExample([2, 3, 1])
v4 = VectorExample([7, 0, 4, 2])

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
try:
    print(v1 + v2)
    print("Ok")
except ValueError:
    print("Rozne dlugosci wektorow!")
try:
    print(v1 + v3)
    print("Ok")
except ValueError:
    print("Rozne dlugosci wektorow!")

try:
    print(v1 / v2)
    print("Ok")
except ZeroDivisionError:
    print("Dzielenie przez zero")

try:
    print(v1 / v4)
    print("Ok")
except ZeroDivisionError:
    print("Dzielenie przez zero")
