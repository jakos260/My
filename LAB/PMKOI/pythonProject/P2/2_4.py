def my_generator(start, stop, step):
    n = start
    while n <= stop - step:
        n = n + step
        yield n #przerwanie funkcji i zwrócenie wartości n

my_gen = my_generator(start=10, stop=20, step=2)
for value in my_gen:
    print(value)
