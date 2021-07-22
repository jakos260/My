ep = 1.0
a = 1.0
print(type(a))

while a != a + ep:
    ep = ep/10

#mg - rząd wielkości ep
#dec - z taką dokładnością metoda wyznaczy ep
dec = 100
mg = ep/dec

while a == a + ep:
    b = a + ep
    ep += (mg)

print("a = ", a)
print("a + ep = ", b)
print("ep = ", ep)
