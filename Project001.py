# Number guessing game
import random
a = int(input("Enter a number"))
b = random.randint(0,a*2)
print("Your Number",a,"\nComputer generated is",b)
comHigh = a+a*1/10
comLow = a-a*1/10
if b < comLow:
    print("Number is too high")
elif b > comLow and b < comHigh:
    print("Number is near to your number")
elif b > comHigh:
    print("Number is too low")
elif b == comHigh:
    print("Number is equal")