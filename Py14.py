import random

def usingSet():
    dupList, newlist = [], []
    listLen = int(input("Enter the length of the list: "))
    
    for i in range(listLen):
        listItem = int(input("Enter the value [" + str(i) + "]: "))
        dupList.append(listItem)

    newList = set(dupList)
    newList = list(newList)

    return newList

print(usingSet())

def usingSetsEx5():
    newSet = set()
    set1 = set()
    set2 = set()
    randrange = int(input("Enter the range of Set Values: "))
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
