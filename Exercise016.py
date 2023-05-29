# Different ways to clear a list in Python
list = [9, 5, 7, 6, 2, 3, 4, 5, 1, 0, 10, 11]
# list.clear()
# list = []
len = len(list)
if len != 0:
    print(list, "Element exist")
else:
    print(list, "Element not exist")