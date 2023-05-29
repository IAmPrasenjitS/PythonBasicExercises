# Python | Reversing a List
list = [9, 5, 7, 6, 2, 3, 4, 5, 1, 0, 10, 11]
revList = []
for x in range(len(list)-1, -1, -1):
    revList.append(list[x])
print(revList)