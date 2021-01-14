num = int(input("Please enter a number: "))
list = []

for i in range(1, 999999):
    if(i > num):
        print("Loop broke")
        break
    elif(num % i == 0):
        list.append(i)
        
print("Divisors which are divisible to " + str(num) + " is " + str(list))
