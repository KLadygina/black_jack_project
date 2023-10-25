import random
import os 
os.system('cls')


    

def greet():
    print("ᗷ ᒪ ᗩ ᑕ ᛕ  ᒎ ᗩ ᑕ ᛕ\n")
    print("Welcome to Black Jack terminal game!")
    

def players_amount():
    amount = int(input('How many players will play? Choose 1 to 3 \n'))
    if amount == 1:
        user_1 = input('How can we call you?\n')
    else:
        print("Oops, looks like this amount is not available at the moment")
        return players_amount()

def rules():
    answer = input("Would you like to see the roles of the game? Answer Yes or No \n")
    if answer == "Yes":
        print('Roles of the game')
    elif answer == "No":
        print("Okay, then let's start!")
    else:
        return rules()

    



greet() 
players_amount()
rules()
