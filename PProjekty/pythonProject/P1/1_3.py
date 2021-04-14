list1 = [i for i in range(0, 10, 2)]
list2 = [i for i in range(1, 11, 2)]
cos = lambda list1, list2: [a * b for a, b in zip(list1, list2)]
print(cos(list1, list2))