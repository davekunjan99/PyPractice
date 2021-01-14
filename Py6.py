string = str(input("Enter a string: "))
revString = string[::-1]

if(string == revString):
    print("Your string " + string + " is palindrome.")
else:
    print("Your string " + string + " is not palindrome.")
