# Exercise 6: Write a program that appends the square of each number upto n to a new list.
n = int(input("Enter the nth term"))
list = []
for x in range(1, n+1):
    list.append(x*x)
print(list)
