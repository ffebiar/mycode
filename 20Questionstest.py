#!/usr/bin/env python3
 
import os

os.chdir("/home/student/mycode/")
 
ask= 0
answer= " "
answer2= " "

def R():
    os.system("python3 20Questionstest.py")
    print("Restarting game")

def win():
    print("Thanks for playing!!")
    print("I hope you had fun!!")
    print("Come back again!!")       
    exit()

def Q():
    print(f"Question {ask}")

def end():
    print("Shame, come again next time!!")
    exit()

def yon():
    print("Sorry, you can only answer Yes or No!")

while True:
    answer= input("Restart? ").lower()
    if answer == "yes":
        R()

while True:
    print("Hello, this is the 20 Questions game!")
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
    ask += + 1
    Q()
    answer= input("Are you a cat? ").lower()
    if answer == "yes":
        print("Great!!")
        break
    elif answer == "no":
        print("Welp, looks like I\'m a bear!!")
        win()
    else:
        ask += - 1
        yon()
while ask < 20:
    ask += + 1
    Q()
    answer= input("Do I have stripes? ").lower()
    if answer == "yes":
        print("Welp, looks like I\'m a tiger!!")
        win()
    elif answer == "no":
        print("Welp, looks like I\'m a lion!!")
        win()
    else:
        ask += - 1
        yon()
