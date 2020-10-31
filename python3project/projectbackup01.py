#!/usr/bin/python3

import time

def main():
    confirm= " "
    gamemode= " "
    while True:
        print("*****WELCOME*****")
        print("This is the 20 Question Game!!")
        time.sleep(1)
        print("----------------------")
        gamemode= input("Play Hard, Normal, or Easy mode?: ").lower()
        print("----------------------")
        if gamemode == "hard":
            hard()
        elif gamemode == "normal":
            normal()
        elif gamemode == "easy":
            easy()
        elif gamemode == "exit" or gamemode == "q" or gamemode == "quit":
            print("You will lose all progress! Are you sure you want to exit?")
            confirm= input("Type (Y(Yes) to confirm!: ").lower()
            print("----------------------")
            if confirm == "yes" or confirm == "y":
                print("*****GOODBYE*****")
                time.sleep(1)
                print("----------------------")
                exit()
            else:
                print("*****Returning to game*****")
                time.sleep(1)
                print("----------------------")
                continue
        elif gamemode == "menu":
            print("You will lose all progress! Are you sure you want to exit?")
            confirm= input("Type (Y(Yes) to confirm!: ").lower()
            print("----------------------")
            if confirm == "yes" or confirm == "y":
                print("*****Moving to Starting Screen*****")
                time.sleep(1)
                print("----------------------")
                main()
            else:
                print("*****Returning to game*****")
                time.sleep(1)
                print("----------------------")
                continue
        else:
            print("Enter (Hard) (Normal) (Easy) only!!")
            print("You can always Exit by typing (Exit) (Q(Quit)")
            print("You may also go back to the Starting Screen with (Menu)")
            time.sleep(2)
            print("----------------------")

def hard():
    ask= 0
    answer= " "
    while True:
        print("Welcome!! This is Hard mode 20 Questions game!")
        time.sleep(1)
        print("----------------------")
        print("Choose between a Lion, Tiger, or Bear!")
        print("Choose one and I will try and guess what you chose!")
        time.sleep(1)
        print("----------------------")
        while True:         
            answer = input("Are you ready to play?: ").lower()
            if answer == "yes":
                print("Awesome, let\'s get started!!")
                break
            elif answer == "no":
                print("Shame, come again next time!!")
                exit()
            elif answer == "exit" or answer == "q" or answer == "quit":
                print("Goodbye")
                print("----------------------")
                exit()       
            else:
                print("Enter (Yes) or (No) only!!")
                print("You can always Exit by typing (Exit) (Q) (Quit)")
                print("----------------------")
        while ask < 20:
            ask += 1
            print(f"Question {ask}")
            answer= input("Are you a cat?: ").lower()
            if answer == "yes":
                print("Great!!")
                break
            elif answer == "no":
                print("Welp, looks like I\'m a Bear!!")
                print("Thanks for playing!!")
                print("I hope you had fun!!")
                answer= input("Do you want to play again?: ").lower()
                if answer == "yes":
                    print("Restarting game")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    main()
                elif answer == "no":
                    print("Come back again!!")
                    exit()
                elif gamemode == "exit" or gamemode == "q" or gamemode == "quit":
                    print("Goodbye")
                    print("----------------------")
                    exit()       
                else:
                    print("This late in the game and you still can\'t follow the rules!!")
                    print("Looks like you\'ll just have to play again!! :D")
                    print("Restarting game")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    main()
            elif gamemode == "exit" or gamemode == "q" or gamemode == "quit":
                print("Goodbye")
                print("----------------------")
                exit()       
            else:
                print("Enter (Yes) or (No) only!!")
                print("You can always Exit by typing (Exit) (Q) (Quit)")
                print("----------------------")
        while ask < 20:
            ask += 1
            print(f"Question {ask}")
            answer= input("Do I have stripes?: ").lower()
            if answer == "yes":
                print("Welp, looks like I\'m a Tiger!!")
                print("Thanks for playing!!")
                print("I hope you had fun!!")
                answer= input("Do you want to play again?: ").lower()
                if answer == "yes":
                    print("Restarting game")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    main()
                elif answer == "no":
                    print("Come back again!!")
                    exit()
                elif gamemode == "exit" or gamemode == "q" or gamemode == "quit":
                    print("Goodbye")
                    print("----------------------")
                    exit()       
                else:
                    print("This late in the game and you still can\'t follow the rules!!")
                    print("Looks like you\'ll just have to play again!! :D")
                    print("Restarting game")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    main()
            elif answer == "no":
                print("Welp, looks like I\'m a Lion!!")
                print("Thanks for playing!!")
                print("I hope you had fun!!")
                answer= input("Do you want to play again?: ").lower()
                if answer == "yes":
                    print("Restarting game")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    main()
                elif answer == "no":
                    print("Come back again!!")
                    exit()
                elif gamemode == "exit" or gamemode == "q" or gamemode == "quit":
                    print("Goodbye")
                    print("----------------------")
                    exit()       
                else:
                    print("This late in the game and you still can\'t follow the rules!!")
                    print("Looks like you\'ll just have to play again!! :D")
                    print("Restarting game")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    print(".")
                    main()
            elif gamemode == "exit" or gamemode == "q" or gamemode == "quit":
                print("Goodbye")
                print("----------------------")
                exit()       
            else:
                print("Enter (Yes) or (No) only!!")
                print("You can always Exit by typing (Exit) (Q) (Quit)")
                print("----------------------")

def normal():
    print("Coming Soon!!")
    print("----------------------")
  
def easy():
    print("*****Coming Soon*****")
    print("This game mode is currently unavailable!!")
    time.sleep(2)
    print("----------------------")
         
if __name__ == "__main__":
    main()
