#!/usr/bin/python3

import time
import random
## This is the dictionary for Normal Mode
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

answer= " "
## Used when player does not enter the correct input
def rules():
    print("Enter (Y(Yes) (N(No) only!!")
    print("You can always Exit by typing (Exit) (Q(Quit)")
    print("You may also move to the Main Menu with (Menu)")
    time.sleep(0.5)
    print("----------------------")
## Navigate to the Main Menu
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
## Used to confirm exit()
def quit():
    print("You will lose all progress! Are you sure you want to exit?")
    print("Type (Y(Yes) to confirm!")
    answer= input(">> ").lower()
    print("----------------------")
    if answer == "yes" or answer == "y":
        print("*****GOODBYE*****")
        print(""" 
     ██████╗ ██████╗ ███╗   ███╗███████╗    ██████╗  █████╗  ██████╗██╗  ██╗     █████╗  ██████╗  █████╗ ██╗███╗   ██╗██╗██╗
    ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔════╝ ██╔══██╗██║████╗  ██║██║██║
    ██║     ██║   ██║██╔████╔██║█████╗      ██████╔╝███████║██║     █████╔╝     ███████║██║  ███╗███████║██║██╔██╗ ██║██║██║
    ██║     ██║   ██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔══██║██║     ██╔═██╗     ██╔══██║██║   ██║██╔══██║██║██║╚██╗██║╚═╝╚═╝
    ╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    ██████╔╝██║  ██║╚██████╗██║  ██╗    ██║  ██║╚██████╔╝██║  ██║██║██║ ╚████║██╗██╗
     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═╝
                                                                                                                            """)
        time.sleep(0.5)
        print("----------------------")
        exit()
    else:
        print("*****Returning to game*****")
        time.sleep(0.5)
        print("----------------------")
## Used to restart the game from the begining 
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
## Used on players who don't listen 
def troll():
    print("This late in the game and you still can\'t follow the rules!!")
    time.sleep(0.5)
    print("----------------------")
    print("Looks like you\'ll just have to play again!! :D")
    time.sleep(0.5)
    print("----------------------")
    input(">>")
    print("----------------------")
    restart()
## Main Menu of the game
def mainmenu():
    print("*****WELCOME*****")
    print("""
    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗                 
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗                
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║                
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║                
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝                
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝                 
                                                                                                        
    ██████╗  ██████╗      ██████╗ ██╗   ██╗███████╗███████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗██╗██╗
    ╚════██╗██╔═████╗    ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝██║██║
     █████╔╝██║██╔██║    ██║   ██║██║   ██║█████╗  ███████╗   ██║   ██║██║   ██║██╔██╗ ██║███████╗██║██║
    ██╔═══╝ ████╔╝██║    ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║╚═╝╚═╝
    ███████╗╚██████╔╝    ╚██████╔╝╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚████║███████║██╗██╗
    ╚══════╝ ╚═════╝      ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝
                                                                                                        """)
    print("This is the 20 Question Game!!")
    time.sleep(0.5)
    print("----------------------")
    while True:
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
## Hard Mode of the game
def hard():
    print("*****WELCOME*****") 
    print("""
    ██╗  ██╗ █████╗ ██████╗ ██████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗██╗
    ██║  ██║██╔══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║██║
    ███████║███████║██████╔╝██║  ██║    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║██║
    ██╔══██║██╔══██║██╔══██╗██║  ██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ╚═╝╚═╝
    ██║  ██║██║  ██║██║  ██║██████╔╝    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗██╗██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═╝
                                                                                  """)
    print("This is Hard mode 20 Questions game!")
    time.sleep(0.5)
    print("----------------------")
    print("Choose between a Lion, Tiger, or Bear!")
    print("Choose and I will try and guess which one you chose!")
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
    while True:
        print("*****Beginning Hard mode*****")
        print("Question 1")
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
            print("""             (()__(()
             /       \ 
            ( /    \  \ 
             \ o o    /
             (_()_)__/ \             
            / _,==.____ \ 
           (   |--|      )
           /\_.|__|'-.__/\_
          / (        /     \ 
          \  \      (      /
           )  '._____)    /    
         (((____.--(((____/""")
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
                hard()
            elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                quit()
            elif answer == "menu":
                menu()
            else:
                troll()
                hard()
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
            print("""                             __,,,,_
               _ __..-;''`--/'/ /.',-`-.
           (`/' ` |  \ \ \/\ / / / / .-'/`,_
          /'`\ \   |  \ | \| // // / -.,/_,'-,
         /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
        /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\.'
        `-`  f/ ;      / __/ \__ `/ |__/ |
             `-'      |  -| =|\_  \  |-' |
                   __/   /_..-' `  ),'  //
                  ((__.-'((___..-'' \__.'""")
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
                hard()
            elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                quit()
            elif answer == "menu":
                menu()
            else:
                troll()
                hard()
        elif answer == "no" or answer == "n":
            print("Welp, looks like you\'re a Lion!!")
            print("""                           ,   __, ,
           _.._         )\/(,-' (-' `.__
          /_   `-.      )'_      ` _  (_    _.---._
         // \     `-. ,'   `-.    _\`.  `.,'   ,--.\ 
        // -.\       `        `.  \`.   `/   ,'   ||
        || _ `\_         ___    )  )     \  /,-'  ||
        ||  `---\      ,'__ \   `,' ,--.  \/---. //
         \   .---`.   / /  | |      |,-.\ |`-._ //
          `..___.'|   \ |,-| |      |_  )||\___//
            `.____/    \ \O| |      \o)// |____/
                 /      `---/        \-'  \ 
                 |        ,'|,--._.--')    \ 
                 \       /   `n     n'\    /
                  `.   `<   .::`-,-'::.) ,'    
                    `.   \-.____,^.   /,'
                      `. ;`.,-V-.-.`v'
                        \| \     ` \|\ 
                         ;  `-^---^-'/
                          `-.______,'""")
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
                hard()
            elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                quit()
            elif answer == "menu":
                menu()
            else:
                troll()
                hard()
        elif answer == "exit" or answer == "q" or answer == "quit":
            quit()
        elif answer == "menu":
            menu()
        else:
            rules()            
## Normal Mode of the game
def normal():
    count= 0 
    print("*****WELCOME*****") 
    print("""
    ███╗   ██╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ██╗         ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗██╗
    ████╗  ██║██╔═══██╗██╔══██╗████╗ ████║██╔══██╗██║         ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║██║
    ██╔██╗ ██║██║   ██║██████╔╝██╔████╔██║███████║██║         ██╔████╔██║██║   ██║██║  ██║█████╗  ██║██║
    ██║╚██╗██║██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║██║         ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ╚═╝╚═╝
    ██║ ╚████║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║███████╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗██╗██╗
    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═╝
                                                                                                        """)
    print("This is Normal mode 20 Questions game!")
    time.sleep(0.5)
    print("----------------------")
    print("Choose a US State!")
    print("Choose and I will try and guess which one you chose!")
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
    print("*****Beginning Normal mode*****")
    while count < 20:
        count += 1
        zone= random.choice(list(usa))
        x= zone
        print(f"Question {count}!")
        print(f"Is your state in the {x} zone?")
        answer= input(">> ").lower()
        print("----------------------")
        if answer == "yes" or answer == "y":
            print("Great!!")
            time.sleep(0.5)
            print("----------------------")
            break
        elif answer == "no" or answer == "n":
            print("Welp!!")
            time.sleep(0.5)
            print("----------------------")
        elif answer == "exit" or answer == "q" or answer == "quit":
            quit()
            count -= 1
        elif answer == "menu":
            menu()
            count -= 1
        else:
            rules()
            count -= 1
    while count < 20:
        count += 1
        state= random.choice(list(usa[x]))
        print(f"Question {count}!")
        print(f"Is the state you choose {state}?")
        answer= input(">> ").lower()
        print("----------------------")
        if answer == "yes" or answer == "y":
            print("Looks like I WIN!!")
            print("""
    ██╗      ██████╗ ███████╗███████╗██████╗ ██╗██╗
    ██║     ██╔═══██╗██╔════╝██╔════╝██╔══██╗██║██║
    ██║     ██║   ██║███████╗█████╗  ██████╔╝██║██║
    ██║     ██║   ██║╚════██║██╔══╝  ██╔══██╗╚═╝╚═╝
    ███████╗╚██████╔╝███████║███████╗██║  ██║██╗██╗
    ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝
                                                   """)
            print("You lost!!")
            time.sleep(0.5)
            print("----------------------")
            print("Thanks for playing!!")
            print("I hope you had fun!!")
            time.sleep(0.5)
            print("----------------------")
            print("Do you want to play again?")
            print("Enter (Y(Yes) to restart Normal mode and (Menu) to exit to the Main Menu!")
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
            print("Welp!!")
            time.sleep(0.5)
            print("----------------------")
        elif answer == "exit" or answer == "q" or answer == "quit":
            quit()
            count -= 1
        elif answer == "menu":
            menu()
            count -= 1
        else:
            rules()
            count -= 1
    print("Looks like I LOST!!")
    print("""
    ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ ██╗██╗
    ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗██║██║
    ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝██║██║
    ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗╚═╝╚═╝
    ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║██╗██╗
     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝
                                                           """)
    print("You won!!")
    time.sleep(0.5)
    print("----------------------")
    print("Thanks for playing!!")
    print("I hope you had fun!!")
    time.sleep(0.5)
    print("----------------------")
    print("Do you want to play again?")
    print("Enter (Y(Yes) to restart Normal mode and (Menu) to exit to the Main Menu!")
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
## Easy Mode of the game (not really)
def easy():
    print("*****Coming Soon*****")
    print("""
    ███████╗ █████╗ ███████╗██╗   ██╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗██╗
    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║██║
    █████╗  ███████║███████╗ ╚████╔╝     ██╔████╔██║██║   ██║██║  ██║█████╗  ██║██║
    ██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ╚═╝╚═╝
    ███████╗██║  ██║███████║   ██║       ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗██╗██╗
    ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═╝
                                                                                   """)
    print("This game mode is currently unavailable!!")
    time.sleep(0.5)
    print("----------------------")
    input(">>")
    print("----------------------")
    print("*****Moving to Selection*****")
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
## Main fuction of the script
def main():
    mainmenu()
## Used to keep the script from running if imported
if __name__ == "__main__":
    main()
