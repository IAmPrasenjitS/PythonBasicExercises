# Python | Remove empty tuples from a list
list = [(1,3),5,(2,5,8),(),()]
for x in range(len(list)-1):
    print(list[x])
    if type(list[x]) == tuple and len(list[x]) == 0:
        list.remove(list[x])
        print("Tuple is empty. Removed..")
# print(list)