#!/usr/bin/env python3
round= 0
answer= " "

while round < 3 and answer.lower() != "brian" and answer.lower() != "shrubbery":
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of _____": ')
    if answer.lower() == "shrubbery":
        print("You gave the super secret answer!")
        if True:        # can also just use print()
            print("Congrats!!")
    elif answer.lower() == "brian":
        print("Correct!")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry. Try again!")
