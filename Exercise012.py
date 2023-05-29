# Python program to swap two elements in a list
list = ['One', 'Two', 'Three', 'Four']
print("Original List: ", list)
temp = list[0]
list[0] = list[3]
list[3] = temp
print("Changed List: ", list)