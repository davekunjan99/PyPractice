import random

randrange = int(input("Enter the range of Set Values: "))

def usingList():
    count = 0
    dupList, newList = [], []
    listLen = int(input("Enter the length of the list: "))
    
    for i in range(listLen):
##        listItem = int(input("Enter the value [" + str(i) + "]: "))
        listItem = random.randrange(randrange)
        
        dupList.append(listItem)

##        print(listItem)

        for i in range(len(dupList)):
            if dupList[i] not in newList:
                newList.append(dupList[i])
            else:
                continue
        
##        if listItem not in dupList:
##            dupList.append(listItem)

    print(dupList)
    return newList

print(usingList())


def usingSet():
    dupList, newlist = [], []
    listLen = int(input("Enter the length of the list: "))
    
    for i in range(listLen):
        listItem = int(input("Enter the value [" + str(i) + "]: "))
        
        dupList.append(listItem)
##        dupList.append(random.randrange(randrange))

    newList = set(dupList)
    newList = list(newList)

    return newList

print(usingSet())

def usingSetsEx5():
    newSet = set()
    set1 = set()
    set2 = set()
    lenSet1 = int(input("Enter length of Set 1: "))
    lenSet2 = int(input("Enter length of Set 2: "))

    for i in range(lenSet1):
        set1.add(random.randrange(randrange))
        
    print(set1)
    
    for i in range(lenSet2):
        set2.add(random.randrange(randrange))
        
    print(set2)

    newSet = set1.intersection(set2)
    
    return newSet

print(usingSetsEx5())
