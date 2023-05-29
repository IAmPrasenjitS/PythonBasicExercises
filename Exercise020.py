# Python Program to find sum and average of List in Python
list = [9, 5, 7, 6, 9, 5, 4, 9, 1, 9, 6, 6]
total = 0
len = len(list)

for x in list:
    total = total + x
ave = total / len
print("Total:", total,"\nAverage:", ave)