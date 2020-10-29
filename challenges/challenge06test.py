#!/usr/bin/python3

import time

def calc():
    while True:
        
        answer= input("Would you like to add(+), subtract(-), multiply(*), or divide(/)? ").lower()
        if answer == "+":
            x = input("First number: ")
            y = input("Second number: ")
            if x.isnumeric() and y.isnumeric():  # or y == float or int:
                print("Your answer is:", x+y)
            else:
                print("You can only add numbers!")
                time.sleep(1)
    
        elif answer == "-":
            x = input("First number: ")
            y = input("Second number: ")
            if x.isnumeric() and y.isnumeric():  # or y == float or int:
                print("Your answer is:", x-y)
            else:
                print("You can only subtract numbers!")
                time.sleep(1)

        elif answer == "*":
            x = input("First number: ")
            y = input("Second number: ")
            if x.isnumeric() and y.isnumeric():  # or y == float or int:
                print("Your answer is:", x*y)
            else:
                print("You can only multiply numbers!")
                time.sleep(1)

        elif answer == "/":
            x = input("First number: ")
            y = input("Second number: ")
            if x.isnumeric() and y.isnumeric():  # or y == float or int:
                print("Your answer is:", x/y)
            else:
                print("You can only divide numbers!")
                time.sleep(1)

        elif answer == "exit":
            print("Calculator powering down!")
            exit()

        else:
            print("You can only enter these characters (+), (-), (*), (/), or (exit) to quit!")
            time.sleep(1)

calc()
