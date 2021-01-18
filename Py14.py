newList = []

def usingSet():
    dupList = []
    listLen = int(input("Enter the length of the list: "))
    
    for i in range(listLen):
        listItem = int(input("Enter the value [" + str(i) + "]: "))
        dupList.append(listItem)

    newList = set(dupList)
    newList = list(newList)

    return newList

print(usingSet())    
