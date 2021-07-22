print("co tu robić?\n 1. dodawanie\n 2. potęgowanie")
y = input()
y = int(y)
if y == 1:
    x = 2 + 33
    print("wynik dodawania ", x)
elif y == 2:
    z = 1
    print("podaj potęgę")
    a = input()
    a = int(a)
    for i in range(a):
        if i < a:
            z = z * 10
    print("wynik 2 ^",a,"to:",z)
