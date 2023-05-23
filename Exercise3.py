# Exercise 3: Write a Python program to reverse a number.
number=int(input("Enter a number to reverse"))
rev=0
while number!=0:
    rem=number%10
    rev=rev*10+rem
    number=number//10
print(rev)

