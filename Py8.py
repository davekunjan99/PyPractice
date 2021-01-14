import random

computer = random.randrange(0, 2)

##print(computer)
while(True):
    winLose = 0
    choice = int(input("Enter 1 = New Game or 2 = Exit: "))
    
    if(choice == 1):
        while(winLose != 1):
            print("0 = You vs. Computer, 9 = You vs. Friend")
            newGame = int(input("Enter your choice: "))
            
            if(newGame == 0):
                while(True):
                    print("0 = Rock, 1 = Paper, 2 = Scissor")
                    opponent = int(input("Enter your choice: "))
                    
                    if(computer == 0 and opponent == 0):
                        print("Your game is tied, please try again." + str(computer))

                    elif(computer == 0 and opponent == 1):
                        print("Sorry, you Lost, better luck next time." + str(computer))
                        break

                    elif(computer == 0 and opponent == 2):
                        print("Congratulations, you Won!" + str(computer))
                        winLose += 1
                        break

                    elif(computer == 1 and opponent == 0):
                        print("Sorry, you Lost, better luck next time." + str(computer))
                        break

                    elif(computer == 1 and opponent == 1):
                        print("Your game is tied, please try again." + str(computer))

                    elif(computer == 1 and opponent == 2):
                        print("Congratulations, you Won!" + str(computer))
                        winLose += 1
                        break

                    elif(computer == 2 and opponent == 0):
                        print("Congratulations, you Won!" + str(computer))
                        winLose += 1
                        break

                    elif(computer == 2 and opponent == 1):
                        print("Sorry, you Lost, better luck next time." + str(computer))
                        break

                    elif(computer == 2 and opponent == 2):
                        print("Your game is tied, please try again." + str(computer))

                    else:
                        print("Opps! Enter your number again." + str(computer))
                        continue
                    
            elif(newGame == 9):
                while(True):
                    print("0 = Rock, 1 = Paper, 2 = Scissor")
                    you = int(input("Enter your choice: "))
                    opponent = int(input("Enter your opponents choice: "))

                    if(you == 0 and opponent == 0):
                        print("Your game is tied, please try again.")

                    elif(you == 0 and opponent == 1):
                        print("Sorry, you Lost and your friend Won, better luck next time.")
                        winLose += 1
                        break

                    elif(you == 0 and opponent == 2):
                        print("Congratulations, you Won!")
                        winLose += 1
                        break

                    elif(you == 1 and opponent == 0):
                        print("Sorry, you Lost and your friend Won, better luck next time.")
                        winLose += 1
                        break

                    elif(you == 1 and opponent == 1):
                        print("Your game is tied, please try again.")

                    elif(you == 1 and opponent == 2):
                        print("Congratulations, you Won!")
                        winLose += 1
                        break

                    elif(you == 2 and opponent == 0):
                        print("Congratulations, you Won!")
                        winLose += 1
                        break

                    elif(you == 2 and opponent == 1):
                        print("Sorry, you Lost and your friend Won, better luck next time.")
                        winLose += 1
                        break 

                    elif(you == 2 and opponent == 2):
                        print("Your game is tied, please try again.")

                    else:
                        print("Opps! Enter your number again.")
                        continue

            else:
                print("Opps! Enter your number again.")
                continue

    else:
        print("Thank you for playing this game.")
        break
