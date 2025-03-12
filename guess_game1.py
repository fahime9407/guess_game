''' This is a simple number guessing game where
the computer randomly selects a number between 1 and 100 
and the user tries to guess the number. '''

import random

number_com = random.randint(1,100) # computer guess a number from 1 to 100
number_guess = int (input("enter your guess : ")) # user guess computer's number

while number_com != number_guess : # if the two numbers were equal we exit the loop
    if number_guess > number_com :
        print ("no , my number is less than your guess!! ")
    else : # if computer number is bigger than users's guess
        print ("no , my number is more than your guess!! ")
    number_guess = int (input("enter your guess : ")) # get next guess
else :
    print (f"congratulations , you won!!! ")


