# Remove multiple elements from a list in Python
list = [9, 5, 7, 6, 9, 5, 4, 9, 1, 9, 6, 6]
for x in range(3):
    a = int(input("Enter a number to remove"))
    list.remove(a)
    print(list)
print("Final List",list)