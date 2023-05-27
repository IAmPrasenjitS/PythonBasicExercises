# Exercise 8: Write a program that appends the type of elements from a list.
list1 = [1, 1.2, 1.3j, 'Hello']
list2 = []
for x in range(len(list1)):
    list2.append(type(list1[x]))
print(list2)
