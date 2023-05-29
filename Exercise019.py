# Python | Count occurrences of an element in a list
list = [9, 5, 7, 6, 9, 5, 4, 9, 1, 9, 6, 6]
n = int(input("Enter a number to check"))
count = 0
for x in list:
    if x == n:
        count += 1
print("Occurrence of", n,"is",count, "times")