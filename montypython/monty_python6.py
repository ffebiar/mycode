#!/usr/bin/env python3
round= 0
answer= " "

while round < 3 and answer != "brian" and answer != "shrubbery":
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of _____": ').lower()
    if answer == "shrubbery":
        print("You gave the super secret answer!")
        if True:        # can also just use print()
            print("Congrats!!")
    elif answer == "brian":
        print("Correct!")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry. Try again!")
