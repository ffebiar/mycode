#!/usr/bin/python3
import time
def mainmenu():
    confirm= " "
    gamemode= " "
    while True:
        print("*****WELCOME*****")
        print("This is the 20 Question Game!!")
        time.sleep(0.5)
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
                time.sleep(0.5)
                print("----------------------")
                exit()
            else:
                print("*****Returning to game*****")
                time.sleep(0.5)
                print("----------------------")
                continue
        elif gamemode == "menu":
            print("You will lose all progress! Are you sure you want to exit to the Main Menu?")
            confirm= input("Type (Y(Yes) to confirm!: ").lower()
            print("----------------------")
            if confirm == "yes" or confirm == "y":
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
                continue
        else:
            print("Enter (Hard) (Normal) (Easy) only!!")
            print("You can always Exit by typing (Exit) (Q(Quit)")
            print("You may also move to the Main Menu with (Menu)")
            time.sleep(0.5)
            print("----------------------")
def hard():
    confirm= " "
    answer= " "
    def rules():
        print("Enter (Y(Yes) (N(No) only!!")
        print("You can always Exit by typing (Exit) (Q(Quit)")
        print("You may also move to the Main Menu with (Menu)")
        time.sleep(0.5)
        print("----------------------")
    def menu():
        print("You will lose all progress! Are you sure you want to exit to the Main Menu?")
        confirm= input("Type (Y(Yes) to confirm!: ").lower()
        print("----------------------")
        if confirm == "yes" or confirm == "y":
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
        confirm= input("Type (Y(Yes) to confirm!: ").lower()
        print("----------------------")
        if confirm == "yes" or confirm == "y":
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
        hard()
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
        hard()
    while True:
        print("Welcome!! This is Hard mode 20 Questions game!")
        time.sleep(0.5)
        print("----------------------")
        print("Choose between a Lion, Tiger, or Bear!")
        print("Choose one and I will try and guess what you chose!")
        time.sleep(0.5)
        print("----------------------")
        while True:         
            answer = input("Are you ready to play?: ").lower()
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
            answer= input("Are you a cat?: ").lower()
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
                answer= input("Enter (Y(Yes) to restart Hard mode and (Menu) to exit to the Main Menu!: ").lower()
                print("----------------------")
                if answer == "yes" or answer == "y":
                    restart()
                elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                    quit()
                elif answer == "menu":
                    menu()
                else:
                    troll()
            elif answer == "exit" or answer == "q" or answer == "quit":
                quit()
            elif answer == "menu":
                menu()
            else:
                rules()
        while True:
            print("Question 2")
            answer= input("Do I have stripes?: ").lower()
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
                answer= input("Enter (Y(Yes) to restart Hard mode and (Menu) to exit to the Main Menu!: ").lower()
                print("----------------------")
                if answer == "yes" or answer == "y":
                    restart()
                elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                    quit()
                elif answer == "menu":
                    menu()
                else:
                    troll()
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
                answer= input("Enter (Y(Yes) to restart Hard mode and (Menu) to exit to the Main Menu!: ").lower()
                print("----------------------")
                if answer == "yes" or answer == "y":
                    restart()
                elif answer == "exit" or answer == "q" or answer == "quit" or answer == "no" or answer == "n":
                    quit()
                elif answer == "menu":
                    menu()
                else:
                    troll()
            elif answer == "exit" or answer == "q" or answer == "quit":
                quit()
            elif answer == "menu":
                menu()
            else:
                rules()
def normal():
    print("*****Coming Soon*****")
    print("This game mode is currently unavailable!!")
    time.sleep(0.5)
    print("----------------------")
def easy():
    print("*****Coming Soon*****")
    print("This game mode is currently unavailable!!")
    time.sleep(0.5)
    print("----------------------")
         
def main():
    mainmenu()

if __name__ == "__main__":
    main()
