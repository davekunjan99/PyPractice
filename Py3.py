list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Enter a number: "))
list1 = []

##for i in range(0, len(list)):
##    print(i)
##    if(list[i] < num):
##        item = list[i]
##        print("Item: " + str(item))
##        list1.append(item)

for i in list:
    if(i < num):
        list1.append(i)

print(list1)
