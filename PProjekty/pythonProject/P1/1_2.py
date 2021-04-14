
def multiply_lists(list1, list2):
    a = []
    for i in range(len(list1)):
        a.append(list1[i] * list2[i])
    return a
list1 = [i for i in range(0, 10, 2)]
list2 = [i for i in range(1, 11, 2)]
list3 = multiply_lists(list1, list2)
print(list3)