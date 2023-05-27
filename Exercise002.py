#Exercise 2: Write a program in Python to reverse a word.
word = input("Enter a word")
for x in range(len(word)-1, -1, -1):
    print(word[x], end="")
