# Write a Python script to add a key to a dictionary.
#             Sample Dictionary : {0: 10, 1: 20}
#             Expected Result : {0: 10, 1: 20, 2: 30}
d = {0: 10, 1: 20}
print("Dictionary: ", d)
d[2] = 30
print("Updated using direct method",d)
d.update({3:40})
print("Updated using update method",d)