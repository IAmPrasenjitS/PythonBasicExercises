# C - Create
# R - Read
# U - Update
# D - Delete
import sys
list = []
def create():
    i=input("Enter data to create")
    list.append(i)
def read():
    print(list)
def update():
    print(list)
    i = int(input("Enter position number to update"))
    j = input("Enter data to update")
    list[i-1] = j
def delete():
    print(list)
    i = int(input("Enter position number to delete"))
    del list[i-1]

while True:
    n=int(input("""
    1. Create
    2. Read
    3. Update
    4. Delete
    5. Exit
    """))
    if n==1:
        create()
    elif n==2:
        read()
    elif n==3:
        update()
    elif n==4:
        delete()
    elif n==5:
        sys.exit()
    else:
        print("Invalid Input")