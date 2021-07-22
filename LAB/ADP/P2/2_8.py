class VE():
    def __init__(self, vector):
        self.vector = vector
    def __str__(self):
        return str(self.vector)

    def __repr__(self):
        return self.__str__()
    def __add__(self, other):
        if(len(self.vector)!=len(other.vector)):
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
            for k in range(len(other.vector)):
                if other.vector[k] != 0:
                    return [self.vector[i] / other.vector[i] for i in range(len(self.vector))]
                else:
                    raise ZeroDivisionError

v1 = VE([1,2,3,4])
v2 = VE([5,3,2,1])
v3 = VE([2,3,1])
v4 = VE([7,0,2,1])

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
try:
    print(v3 / v4)
except ValueError:
    print('błąd wartości')
except ZeroDivisionError:
    print('dzielenie przez zero')

try:
    print(v1 + v3)
except ValueError:
    print('błąd wartości')
except ZeroDivisionError:
    print('dzielenie przez zero')

try:
    print(v1 / v4)
except ValueError:
    print('błąd wartości')
except ZeroDivisionError:
    print('dzielenie przez zero')

