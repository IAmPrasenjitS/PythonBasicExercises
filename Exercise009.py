# Exercise 9: Write a program to filter even and odd number from a list.
list = [10, 15, 12, 18, 19, 21, 52, 25, 30, 65, 66, 92, 29, 41, 40, 72, 27, 78, 87]
print("Even numbers are:")
for x in range(len(list)):
    if list[x]%2==0:
        print(list[x], end=", ")

print("\nOdd numbers are:")
for x in range(len(list)):
    if list[x]%2!=0:
        print(list[x], end=", ")
