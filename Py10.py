import random

listRange = 100
list1, list2 = [random.randrange(listRange) for i in range(10)], [random.randrange(100) for i in range(15)]
##list1 = [92, 58, 22, 79, 32, 69, 31, 27, 32, 50]
##list2 = [13, 45, 70, 31, 3, 41, 77, 18, 13, 88, 28, 2, 32, 60, 50]
comWithDupli = [i for i in list1 if i in list2]
comItem = [i for i in range(listRange) if i in comWithDupli]

print(str(list1) + "\n"+ str(list2) + "\n" + str(comWithDupli))    
print(comItem)
