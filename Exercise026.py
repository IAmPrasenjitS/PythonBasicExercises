# Write a Python program to sum all the items in a dictionary.
d = {
    'One' : 1,
    'Two' : 2,
    'Three' : 3,
    'Four' : 4,
    'Five' : 5,
    'Six' : 6,
    'Seven' : 7,
    'Eight' : 8,
    'Nine' : 9,
    'Ten' : 10,
}
print("Dictionary is: ", d)
sum = 0
for x in d.values():
    sum += x
print("Sum of Dictionary's value is: ",sum)
