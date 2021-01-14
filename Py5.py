import random
list, list1, list2, list3 = [], [], [], []

for i in range(15):
    list1.append(random.randrange(25))
for i in range(10):
    list2.append(random.randrange(25))

print(str(list1) + "\n" + str(list2))

for i in range(len(list1)):
    for j in range(len(list2)):
        if(list1[i] == list2[j]):
            num = list1[i]
            list.append(num)


for k in range(len(list)):
    if(list3.count(list[k])<1):
        list3.append(list[k])
##    print(list)
        
print(list3)
