num = int(input("Please enter a number: "))
check = int(input("Please enter another number to check if num1 is divisible: "))

if(num % check == 0):
    print(str(num) + " is divisible by " + str(check))
else:
    print(str(num) + " is not divisible by " + str(check))
