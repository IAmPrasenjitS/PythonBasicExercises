# Exercise 7: WAP to separate positive and negative number from a list.
list = [1, -1, 2, -2, -3, 4, 3, -4, -5, 5]

print("Negative numbers are: ")
for x in range(len(list)):
    if list[x] < 0:
        print(list[x], ", ", end="")

print("\nPositive numbers are: ")
for x in range(len(list)):
    if list[x] > 0:
        print(list[x], ", ", end="")