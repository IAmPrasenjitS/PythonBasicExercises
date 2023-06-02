# Exercise 030 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#             Sample Dictionary ( n = 5) :
#             Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
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
d1 = {}
n = int(input("Enter nth term"))
for x,y in d.items():
    if y <= n:
        d1.update({x:y*y})
print(d1)