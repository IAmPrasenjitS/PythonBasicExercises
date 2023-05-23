# Exercise 10: Write a program to fetch only even values from a dictionary.
dict = {
    'user1': 1,
    'user2': 2,
    'user3': 3,
    'user4': 4,
    'user5': 5,
    'user6': 6,
    'user7': 7,

}
# print(len(dict))
for x in dict.values():
    if x%2==0:
        print(x)