#!/usr/bin/python3

import os
import sys

os.chdir("/home/student/mycode/")

ask= 0
answer= " "

def R():    # This is to restart the game
    print("Restarting game...")
    os.system("python3 test.py")
    sys.exit()
    sys.exit()
    sys.exit()
    sys.exit()
    sys.exit()
    sys.exit()
    sys.exit()
    sys.exit()
    sys.exit()
    sys.exit()
    
def win():  # Command to run when the script wins
    print("Thanks for playing!!")
    print("I hope you had fun!!")
    answer= input("Do you want to play again? ").lower()
    if answer == "yes":
        R()
    elif answer == "no":
        bye()
    else:
        yon2()
    
def bye():  # Command to run when player does't want to play again after script winning
    print("Come back again!!")
    while True:
        sys.exit()

def Q():    # Made for counting the questions
    print(f"Question {ask}")

def end():  # Used when player doesn't want to play before the script wins
    print("Shame, come again next time!!")
    while True:
        sys.exit()

def yon():  # Used when player types anythong other than yes or no
    print("Sorry, you can only answer Yes or No!")

def yon2(): # Used after script wins and player still types anything other than yes or no
    print("This late in the game and you still can\'t follow the rules!!")
    print("Looks like you\'ll just have to play again!! :D")
    R()

while True:
    print("Welcome!! This is the 20 Questions game!")
    answer= input("Would you like to play? ").lower()
    if answer == "yes":
        print("Great!! Choose between a Lion, Tiger, or Bear!")
        print("Choose one and I will try and guess what you chose!")
        break
    elif answer == "no":
        end()
    else:
        yon()

while True:
    answer = input("Are you ready to play? ").lower()
    if answer == "yes":
        print("Awesome, let\'s get started!!")
        break
    elif answer == "no":
        end()
    else:
        yon()

while ask < 20:
    ask += 1
    Q()
    answer= input("Are you a cat? ").lower()
    if answer == "yes":
        print("Great!!")
        break
    elif answer == "no":
        print("Welp, looks like I\'m a Bear!!")
        win()
    else:
        ask -= 1
        yon()

while ask < 20:
    ask += 1
    Q()
    answer= input("Do I have stripes? ").lower()
    if answer == "yes":
        print("Welp, looks like I\'m a Tiger!!")
        win()
    elif answer == "no":
        print("Welp, looks like I\'m a Lion!!")
        win()
    else:
        ask -= 1
        yon()
