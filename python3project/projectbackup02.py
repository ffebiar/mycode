#!/usr/bin/python3

import time

def main():
    gamemode= " "
    while True:
        print("Welcome to the 20 Question Game!!")
        gamemode= input("Play Hard or Normal mode?: ").lower()
        print("----------------------")
        if gamemode == "hard":
            hard()
        elif gamemode == "normal":
            normal()
        elif gamemode == "exit" or gamemode == "q" or gamemode == "quit":
            print("Goodbye")
            print("----------------------")
            exit()
        else:
            print("Enter (Hard) or (Normal) only!!")
            print("You can always Exit by typing (Exit) (Q) (Quit)")
            print("----------------------")

def normal():
    print("Coming Soon!!")
    print("----------------------")

def hard():
    ask= 0
    answer= " "
    while True:
        print("Welcome!! This is Hard mode 20 Questions game!")
        print("----------------------")
        time.sleep(0.5)
        print("Choose between a Lion, Tiger, or Bear!")
        print("Choose one and I will try and guess what you chose!")
        print("----------------------")
        while True:         
            answer = input("Are you ready to play? ").lower()
            if answer == "yes":
                print("Awesome, let\'s get started!!")
                break
            elif answer == "no":
                print("Shame, come again next time!!")
                exit()
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
            answer= input("Are you a cat? ").lower()
            if answer == "yes":
                print("Great!!")
                break
            elif answer == "no":
                print("Welp, looks like I\'m a Bear!!")
                print("Thanks for playing!!")
                print("I hope you had fun!!")
                answer= input("Do you want to play again? ").lower()
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
            answer= input("Do I have stripes? ").lower()
            if answer == "yes":
                print("Welp, looks like I\'m a Tiger!!")
                print("Thanks for playing!!")
                print("I hope you had fun!!")
                answer= input("Do you want to play again? ").lower()
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
                answer= input("Do you want to play again? ").lower()
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
           
if __name__ == "__main__":
    main()
