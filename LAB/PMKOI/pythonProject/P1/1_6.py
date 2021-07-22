def func6(*arg):
    list_to_check = [*arg]
    a = len(list_to_check)
    if(a % 2) == 0:
        dict = {}
        for i in range(len(arg)):
            dict[i] = arg[i]
        print(dict)
    else:
        for i in range(2, a):
            if (a % i) == 0:
                print(a, "is not a prime number")
                break
        else:
            print(a, "is a prime number")
print(func6(5, 7, 4, "Temperatura", 5, "Natezenie"))
print(func6(2, 3, 5))
print(func6(2, 9, 11, 5, 7, 2, 1, 4, 6))