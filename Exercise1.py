# Exercise 1: Write a program in Python to display the Factorial of a number.
a=int(input("Enter a number to find factorial"))
fact=1
for x in range(1,a+1):
    fact=fact*x
print("Factorial is:",fact)