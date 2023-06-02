# Stack
list = []
while True:
    n = int(input("""
    1. Push
    2. Pop
    3. Peek
    4. Display
    5. Exit
    """))
    if n == 1:
        ele = input("Enter the element to push")
        list.append(ele)
        print("Updated list is: ", list)
    elif n == 2:
        if len(list) == 0:
            print("List is empty")
        else:
            print(list[-1], " Poped")
            del list[-1]
            print("Updated list is: ", list)
    elif n == 3:
        if len(list) == 0:
            print("List is empty")
        else:
            print(list[-1], " Picked")
            print("Updated list is: ", list)
    elif n == 4:
        print("List is: ", list)
    elif n == 5:
        break
    else:
        print("Invalid Input")
