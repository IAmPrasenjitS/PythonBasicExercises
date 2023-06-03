# Rock Paper Scissor Game
import sys
import random
comCount = 0
userCount = 0
# list = ['rock', 'paper', 'scissor']
start = int(input("""
1. Start The Game
2. Exit
"""))
if start == 2:
    sys.exit("Program Exit")
for x in range(5):
    computer = random.randint(1,3)
    user = int(input("""
    Enter your choise
    1. Rock
    2. Paper 
    3. Scissor
    """))
    # To show user
    if computer == 1:
        c = 'Rock'
    elif computer == 2:
        c = 'Paper'
    elif computer == 3:
        c = 'Scissor'
    # Game Win Logic
    if computer == user:
        print("Computer choose", c)
        print("Tie")
    # Rock (1) vs Paper (2)
    elif computer == 1 and user == 2:
        userCount+=1
        print("Computer choose", c)
        print("User won")
    elif computer == 2 and user == 1:
        comCount+=1
        print("Computer choose", c)
        print("Computer won")
    # Rock (1) vs Scissor (3)
    elif computer == 3 and user == 1:
        userCount+=1
        print("Computer choose", c)
        print("User won")
    elif computer == 1 and user == 3:
        comCount+=1
        print("Computer choose", c)
        print("Computer won")
    # Rock (2) vs Scissor (3)
    elif computer == 2 and user == 3:
        userCount+=1
        print("Computer choose", c)
        print("User won")
    elif computer == 3 and user == 2:
        comCount+=1
        print("Computer choose", c)
        print("Computer won")
if comCount < userCount:
    print("""
    **********************************
    **********************************
    Congratulations!!! You won the game
    **********************************
    **********************************""")
elif comCount > userCount:
    print("""
    **********************************
    Sorry!!! You lose the game
    **********************************""")
elif comCount == userCount:
    print("""
    **********************************
    You have a tie
    **********************************""")