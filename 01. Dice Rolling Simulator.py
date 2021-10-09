#This is Dice Rolling Simulator
#Asks user minimum and maximum value of the dice
#Throws up a random number within the minimum and the maximum number

import random

gameon = 'yes'  #The game repeat controller


print("Hello There! Welcome to an all new Dice Rolling Simulator!\n")  #Welcome statement. Does not add value to the code

#try-except block is used to make the workable all the time
try:
    while gameon == 'yes':
        print("What is going to be the minimum value of your dice?")
        dice_min_val = int(input())
        print("What is going to be the minimum value of your dice?")
        dice_max_val = int(input())
        dice_output = random.randint(dice_min_val,dice_max_val)
        print("And here goes the result. The dice has rolled out to",dice_output)
        print("Do you want to roll another dice?(y/n)")
        user_input = input()
        while user_input != 'y' and user_input != 'n':     #Check for valid input and ask for till a valid input is provided
            print("Input not recognized. Please provie y/n as valid input.")
            user_input = input()
        if user_input == 'n':
            gameon = "no"
            
    print("It was nice playing with you. Bye!")

except:
    print("Oops! Something went wrong. Try Again!")
    






