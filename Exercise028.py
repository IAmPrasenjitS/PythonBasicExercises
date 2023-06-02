# Exercise 028 Write a Python script to check whether a given key already exists in a dictionary.
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
n = input("Enter a key to check availablity")
flag = False
for x in d.keys():
    if x == n:
        print("Key is already available")
        flag = True
        break
if flag == False:
    print("Key is not already available")