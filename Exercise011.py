# Python program to interchange first and last elements in a list
l = [5, 10, 4, 28, 62, 11, 35, 91, 99, 27]
print("Before Changing value", l)
temp = l[0]
l[0] = l[len(l)-1]
l[len(l)-1] = temp
print("Before Changing value", l)