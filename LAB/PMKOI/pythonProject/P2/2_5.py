def my_multiply(x):
    def fun(tab):
        for i in range(len(tab)):
            tab[i] = tab[i] * x
        return tab
    return fun

ex_func = my_multiply(5.5)
ex_list = [1, 2, 3, 4, 5]
print(ex_list)
ex_func(ex_list)
print(ex_list)