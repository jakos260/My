def my_multiply(tab):
    def fun(a):
        tab_new = []
        for i in range(len(tab)):
            tab_new.append(tab[i] * a)
        return tab_new
    return fun

ex_list = [1, 2, 3, 4, 5]
ex_func = my_multiply(ex_list)
print(ex_list)
print(ex_func(5.5))
print(ex_list)