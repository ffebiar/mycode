#!/usr/bin/python3

import time
import random

usa = {

            'Alaska Standard Time' : 
                            ['Alaska'],

            'Hawaii Standard Time' : 
                            ['Hawaii'],

            'Pacific Standard Time' : 
                            ['Washington',
                             'Oragan',
          		     'Nevada',
          		     'California',
              		     'Idaho'],

            'Arizona Mountain Standard Time' : 
                            ['Arizona'],

            'Mountain Standard Time' :  
                            ['Montana',
			     'Idaho',
			     'Wyoming',
			     'Utah',
			     'Colorado',
			     'Arizona',
			     'New Mexico',
			     'Texas',
			     'North Dakota',
			     'South Dakota',
			     'Nebraska',
			     'Kansas'],

            'Central Standard Time' :  
                            ['North Dakota',
			     'South Dakota',
			     'Nebraska',
			     'Kansas',
			     'Oklahoma',
			     'Texas',
			     'Minnesota',
			     'Iowa',
		             'Missouri',
			     'Arkansas',
			     'Louisiana',
			     'Michigan',
			     'Wisconsin',
			     'Illinois',
			     'Indiana',
			     'Kentucky',
			     'Tennessee',
			     'Mississippi',
			     'Alabama',
			     'Florida'],

            'Eastern Standard Time' : 
                            ['Michigan',
			     'Indiana',
			     'Kentucky',
			     'Tennessee',
			     'Georgia',
			     'Florida',
			     'Ohio',
			     'West Virginia',
			     'Virginia',
			     'North Carolina',
			     'South Carolina',
			     'Pennsylvania',
			     'Maryland',
			     'Delaware',
			     'New Jersey',
			     'New York',
			     'Connecticut',
			     'Rhode Island',
			     'Massachusetts',
			     'Vermont',
			     'New Hampshire',
			     'Maine',
			     'District of Columbia']
            
         }

zone= random.choice(list(usa))
state= random.choice(list(usa['Eastern Standard Time']))
answer= " "
count= 0

def rules():
    print("Enter (Y(Yes) (N(No) only!!")
    print("You can always Exit by typing (Exit) (Q(Quit)")
    print("You may also move to the Main Menu with (Menu)")
    time.sleep(0.5)
    print("----------------------")
def menu():
    print("You will lose all progress! Are you sure you want to exit to the Main Menu?")
    print("Type (Y(Yes) to confirm!")
    answer= input(">> ").lower()
    print("----------------------")
    if answer == "yes" or answer == "y":
        print("*****Moving to Main Menu*****")
        time.sleep(0.1)
        print("       +8-=-=-=-=-=-8+")
        time.sleep(0.1)
        print("        | ,.-'''-., |")
        time.sleep(0.1)
        print("        |/         \|")
        time.sleep(0.1)
        print("        |\:.     .:/|")
        time.sleep(0.1)
        print("        | \:::::::/ |")
        time.sleep(0.1)
        print("        |  \:::::/  |")
        time.sleep(0.1)
        print("        |   \:::/   |")
        time.sleep(0.1)
        print("        |    ):(    |")
        time.sleep(0.1)
        print("        |   / . \   |")
        time.sleep(0.1)
        print("        |  /  .  \  |")
        time.sleep(0.1)
        print("        | /   .   \ |")
        time.sleep(0.1)
        print("        |/   .:.   \|")
        time.sleep(0.1)
        print("        |\.:::::::./|")
        time.sleep(0.1)
        print("        | '--___--' |")
        time.sleep(0.1)
        print("       +8-=-=-=-=-=-8+")
        time.sleep(0.1)
        print("----------------------")
        mainmenu()
    else:
        print("*****Returning to game*****")
        time.sleep(0.5)
        print("----------------------")
def quit():
    print("You will lose all progress! Are you sure you want to exit?")
    print("Type (Y(Yes) to confirm!")
    answer= input(">> ").lower()
    print("----------------------")
    if answer == "yes" or answer == "y":
        print("*****GOODBYE*****")
        time.sleep(0.5)
        print("----------------------")
        exit()
    else:
        print("*****Returning to game*****")
        time.sleep(0.5)
        print("----------------------")
def restart():
    print("*****Restarting game*****")
    time.sleep(0.1)
    print("     +8-=-=-=-=-=-8+")
    time.sleep(0.1)
    print("      | ,.-'''-., |")
    time.sleep(0.1)
    print("      |/         \|")
    time.sleep(0.1)
    print("      |\:.     .:/|")
    time.sleep(0.1)
    print("      | \:::::::/ |")
    time.sleep(0.1)
    print("      |  \:::::/  |")
    time.sleep(0.1)
    print("      |   \:::/   |")
    time.sleep(0.1)
    print("      |    ):(    |")
    time.sleep(0.1)
    print("      |   / . \   |")
    time.sleep(0.1)
    print("      |  /  .  \  |")
    time.sleep(0.1)
    print("      | /   .   \ |")
    time.sleep(0.1)
    print("      |/   .:.   \|")
    time.sleep(0.1)
    print("      |\.:::::::./|")
    time.sleep(0.1)
    print("      | '--___--' |")
    time.sleep(0.1)
    print("     +8-=-=-=-=-=-8+")
    time.sleep(0.1)
    print("----------------------")
def troll():
    print("This late in the game and you still can\'t follow the rules!!")
    time.sleep(0.5)
    print("----------------------")
    print("Looks like you\'ll just have to play again!! :D")
    time.sleep(0.5)
    print("----------------------")
    print("*****Restarting game*****")
    time.sleep(0.1)
    print("     +8-=-=-=-=-=-8+")
    time.sleep(0.1)
    print("      | ,.-'''-., |")
    time.sleep(0.1)
    print("      |/         \|")
    time.sleep(0.1)
    print("      |\:.     .:/|")
    time.sleep(0.1)
    print("      | \:::::::/ |")
    time.sleep(0.1)
    print("      |  \:::::/  |")
    time.sleep(0.1)
    print("      |   \:::/   |")
    time.sleep(0.1)
    print("      |    ):(    |")
    time.sleep(0.1)
    print("      |   / . \   |")
    time.sleep(0.1)
    print("      |  /  .  \  |")
    time.sleep(0.1)
    print("      | /   .   \ |")
    time.sleep(0.1)
    print("      |/   .:.   \|")
    time.sleep(0.1)
    print("      |\.:::::::./|")
    time.sleep(0.1)
    print("      | '--___--' |")
    time.sleep(0.1)
    print("     +8-=-=-=-=-=-8+")
    time.sleep(0.1)
    print("----------------------")
def mainmenu():
    while True:
        print("*****WELCOME*****")
        print("This is the 20 Question Game!!")
        time.sleep(0.5)
        print("----------------------")
        print("Play Hard, Normal, or Easy mode?")
        answer= input(">> ").lower()
        print("----------------------")
        if answer == "hard":
            hard()
        elif answer == "normal":
            normal()
        elif answer == "easy":
            easy()
        elif answer == "exit" or answer == "q" or answer == "quit":
            quit()
        elif answer == "menu":
            menu()
        else:
            print("Enter (Hard) (Normal) (Easy) only!!")
            print("You can always Exit by typing (Exit) (Q(Quit)")
            print("You may also move to the Main Menu with (Menu)")
            time.sleep(0.5)
            print("----------------------")
def normal():
    print("Welcome!! This is Normal mode 20 Questions game!")
    time.sleep(0.5)
    print("----------------------")
    print("Choose between a US State!")
    print("Choose one and I will try and guess what you chose!")
    time.sleep(0.5)
    print("----------------------")
    while True:
        print("Are you ready to play?")
        answer= input(">> ").lower()
        print("----------------------")
        if answer == "yes" or answer == "y":
            print("Awesome, let\'s get started!!")
            time.sleep(0.5)
            print("----------------------")
            break
        elif answer == "no" or answer == "n":
            print("Okay! I'll be waiting!!")
            time.sleep(0.5)
            print("----------------------")
            continue
        elif answer == "exit" or answer == "q" or answer == "quit":
            quit()
        elif answer == "menu":
            menu()
        else:
            rules()
    while count == 20:
        print("*****Beginning Normal mode*****")
        print(f"Question {count}!")
        print("Are you a cat?")
        answer= input(">> ").lower()
        print("----------------------")
        if answer == "yes" or answer == "y":
            print("Great!!")
            time.sleep(0.5)
            print("----------------------")
            break
        elif answer == "no" or answer == "n":
            print("Welp, looks like you\'re a Bear!!")
            time.sleep(0.5)
            print("----------------------")
            print("Thanks for playing!!")
            print("I hope you had fun!!")
            time.sleep(0.5)
            print("----------------------")
            print("Do you want to play again?")
            print("Enter (Y(Yes) to restart Hard mode and (Menu) to exit to the Main Menu!")
            answer= input(">> ").lower()
            print("----------------------")
            if answer == "yes" or answer == "y":
                restart()
                normal()
            elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                quit()
            elif answer == "menu":
                menu()
            else:
                troll()
                normal()
        elif answer == "exit" or answer == "q" or answer == "quit":
            quit()
        elif answer == "menu":
            menu()
        else:
            rules()
    while True:
        print("Question 2")
        print("Do I have stripes?")
        answer= input(">> ").lower()
        print("----------------------")
        if answer == "yes" or answer == "y":
            print("Welp, looks like you\'re a Tiger!!")
            time.sleep(0.5)
            print("----------------------")
            print("Thanks for playing!!")
            print("I hope you had fun!!")
            time.sleep(0.5)
            print("----------------------")
            print("Do you want to play again?")
            print("Enter (Y(Yes) to restart Hard mode and (Menu) to exit to the Main Menu!")
            answer= input(">> ").lower()
            print("----------------------")
            if answer == "yes" or answer == "y":
                restart()
                normal()
            elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                quit()
            elif answer == "menu":
                menu()
            else:
                troll()
                normal()
        elif answer == "no" or answer == "n":
            print("Welp, looks like you\'re a Lion!!")
            time.sleep(0.5)
            print("----------------------")
            print("Thanks for playing!!")
            print("I hope you had fun!!")
            time.sleep(0.5)
            print("----------------------")
            print("Do you want to play again?")
            print("Enter (Y(Yes) to restart Hard mode and (Menu) to exit to the Main Menu!")
            answer= input(">> ").lower()
            print("----------------------")
            if answer == "yes" or answer == "y":
                restart()
                normal()
            elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                quit()
            elif answer == "menu":
                menu()
            else:
                troll()
                normal()
        elif answer == "exit" or answer == "q" or answer == "quit":
            quit()
        elif answer == "menu":
            menu()
        else:
            rules()            


def test():
    x= zone
    print(x)
    print(state)
    print(x)
    print(x)
                                                  
def main():
    normal()

if __name__ == "__main__":
    main()
