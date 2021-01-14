import random

exit = 0
userIn = 0

while(exit != 1):
    
    count = 0
    num = random.randrange(1, 9)
    print("---------------------New Game (type 'exit' to exit)-------------------------")
    while(True):
        
        userIn = input("Guess the number generated between 1 and 9: ")
##        print(userIn == num)
        if (str(userIn) == "exit" or str(userIn) == "Exit" or str(userIn) == "EXIT"):
            exit += 1
            break    

        elif (int(userIn) == num):
            count += 1
            print("Congratulations, Your guess is correct and it took you " + str(count) + " tries. ")
            break
            
        else:
            print("Try again!")
            count += 1
##            print(num)
