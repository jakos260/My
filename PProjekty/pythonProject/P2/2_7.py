def try_except_ex(s, x):
    for i in range(len(x)):
        a = 0
        if x[i] in s:
            a = a + 1

    if a == 0:
        print('false')
    else:
        print('ok')

dict = {'a': 5, 'b': 7, 'c': 4}
list1 = ['a', 'b', 'c']
list2 = ['a', 'b', 'd']
list3 = ['b', 'c', 'a']

try_except_ex(dict, list1)
try_except_ex(dict, list2)
try_except_ex(dict, list3)