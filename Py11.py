num = int(input("Please enter a number: "))

def checkPrime(num):
    isPrime = ""
    if num == 1 or num == 2:
        isPrime = "This number is prime."
    else:
        for i in range(2, num):
            if num % i == 0:
                isPrime = "This number is not prime."
                break
            else:
                isPrime = "This number is prime."
    return isPrime

##while(num != 0):
checkPrime = checkPrime(num)
print(checkPrime)
