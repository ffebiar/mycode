#!/usr/bin/python3

import time

def quit():
    ans= " "
    print("Are you sure you want to exit?")
    ans= input("Type (Y(Yes) to confirm!: ").lower()
    print("----------------------")
    if ans == "yes" or ans == "y":
        print("*****GOODBYE*****")
        time.sleep(0.5)
        print("----------------------")
        exit()
    else:
        print("*****Returning to Flowchart*****")
        time.sleep(0.5)
        print("----------------------")
        q1()

def q1():
    ans= " "
    print("Should you eat that bacon?")
    print("Do you wnat to feel like angels are frolicking on your taste buds?")
    ans= input(":").lower()
    print("----------------------")
    if ans == "yes" or ans == "y":
        print("EAT IT")
        print("----------------------")
    elif ans == "no" or ans == "n":
        print("You've clearly never tasted bacon!")
        print("EAT IT")
        print("----------------------")
    elif ans == "maybe" or ans == "m":
        q2()
    elif ans == "quit" or ans == "q":
        quit()
    else:
        print("You can only answer (Y(Yes) (N(No) (M(Maybe) (Q(Quit)")
        time.sleep(0.5)
        print("----------------------")
        q1()

def q2():
    ans= " "
    print("Maybe?!?!")
    print("You're afraid bacon will kill you?")
    print("Are you a coward?")
    ans= input(":").lower()
    print("----------------------")
    if ans == "yes" or ans == "y":
        print("YES, you're a coward!")
        print("Bacon will turn you into a true warrior")
        print("EAT IT!")
        print("----------------------")
    elif ans == "no" or ans == "n":
        print("You're not?")
        print("Then EAT IT!")
        print("----------------------")
    elif ans == "quit" or ans == "q":
        quit()
    else:
        print("You can only answer (Y(Yes) (N(No) (Q(Quit)")
        time.sleep(0.5)
        print("----------------------")
        q2()

def main():
    print("*****SHOULD YOU EAT THAT BACON?*****")
    print("*****         FLOWCHART        *****")
    print("""          __      _.._
       .-'__`-._.'.--.'.__.,
      /--'  '-._.'    '-._./
     /__.--._.--._.'``-.__/
     '._.-'-._.-._.-''-..'""")
    time.sleep(0.5)
    print("----------------------")
    q1()

if __name__ == "__main__":
    main()
