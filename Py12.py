i = 0
listLength = int(input("Enter the length of the list: "))
list = []
newList = []

while i < listLength:
    list.append(input("Enter a list of numbers [" + str(i) + "]: "))
    i += 1
print(list)

def flElements(list, newList):
    newList = [list[0], list[len(list) - 1]]
    return print(newList)

flElements(list, newList)
