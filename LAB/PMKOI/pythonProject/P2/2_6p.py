def my_multiply(l):
    def in_func(number):
        for i in range(len(l)):
            l[i]=l[i]*number
        return l
    return in_func


example_list = [1,2,3,4,5]
a = my_multiply(example_list)
print(example_list)
a(5.5)
print(example_list)

