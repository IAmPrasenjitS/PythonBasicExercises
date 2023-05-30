# Exercise 022 Python | merge two list into one list using zip function
list1 = ["One", "Two", "Three", "Four", "Five"]
list2 = [1, 2, 3, 4, 5]
listMerged = []
for x, y in zip(list1, list2):
    listMerged.append(x)
    listMerged.append(y)
print(listMerged)