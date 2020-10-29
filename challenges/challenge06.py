#!/usr/bin/python3

import time

def calc():
    while True:
        print("Would you like to add(+), subtract(-), multiply(*), or divide(/)?")
        answer= input("You can always type Exit to QUIT!: ").lower()
        if answer == "+":
            x = input("First number: ").lower()
            if x == "exit":
                print("Calculator powering down!")
                exit()
            y = input("Second number: ").lower()
            if y == "exit":
                print("Calculator powering down!")
                exit()
            elif x.isnumeric() and y.isnumeric():
                x = float(x)
                y = float(y)
                print("Your answer is:", x+y)
                continue
            else:
                print("You can only add numbers!")
                time.sleep(1.5)
                continue

        if answer == "-":
            x = input("First number: ").lower()
            if x == "exit":
                print("Calculator powering down!")
                exit()
            y = input("Second number: ").lower()
            if y == "exit":
                print("Calculator powering down!")
                exit()
            elif x.isnumeric() and y.isnumeric():
                x = float(x)
                y = float(y)
                print("Your answer is:", x-y)
                continue
            else:
                print("You can only subtract numbers!")
                time.sleep(1.5)
                continue

        if answer == "*":
            x = input("First number: ").lower()
            if x == "exit":
                print("Calculator powering down!")
                exit()
            y = input("Second number: ").lower()
            if y == "exit":
                print("Calculator powering down!")
                exit()
            elif x.isnumeric() and y.isnumeric():
                x = float(x)
                y = float(y)
                print("Your answer is:", x*y)
                continue
            else:
                print("You can only multiply numbers!")
                time.sleep(1.5)
                continue

        if answer == "/":
            x = input("First number: ").lower()
            if x == "exit":
                print("Calculator powering down!")
                exit()
            y = input("Second number: ").lower()
            if y == "exit":
                print("Calculator powering down!")
                exit()
            elif x.isnumeric() and y.isnumeric():
                x = float(x)
                y = float(y)
                print("Your answer is:", x/y)
                continue
            else:
                print("You can only divide numbers!")
                time.sleep(1.5)
                continue

        elif answer == "exit":
            print("Calculator powering down!")
            exit()

        else:
            print("You can only enter these characters (+), (-), (*), (/), or (Exit) to QUIT!")
            time.sleep(1)

calc()
