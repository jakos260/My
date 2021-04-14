import time

a = int(input('podaj liczbę\n'))

t1 = time.time()
silnia = 1
for i in range(1, a):
    silnia *= i
t2 = time.time()

print(a, '! =', silnia)
print('time =>', t2 - t1)