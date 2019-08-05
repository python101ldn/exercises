# How would you check if the first and last elements of a list are the same?

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

if list1[0] == list1[-1]:
    print("list1 has the same first and last elements")
else:
    print("list1 has different first and last elements")

if list2[0] == list2[-1]:
    print("list2 has the same first and last elements")
else:
    print("list2 has different first and last elements")
