#!/usr/bin/python3

#Write a for loop that returns all the animals from the NE Farm
#Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm#Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

def main():
    test()

def easy():
    print("Here is everything on the NE Farm")
    for x in farms[0]["agriculture"]:
        print(x)

def mid():
    answer=" "
    while True:
        print("I'll tell you everything in the farms")
        answer= input("Which farm would you like to inspect?(NE Farm) (W Farm) (SE Farm): ").lower()
        if answer == "ne farm":
            for x in farms[0]["agriculture"]:
                print(x)
        elif answer == "w farm":
            for x in farms[1]["agriculture"]:
                print(x)
        elif answer == "se farm":
            for x in farms[2]["agriculture"]:
                print(x)
        elif answer == "exit":
            break
        else:
            print("Your only options are (NE Farm) (W Farm) (SE Farm) (Exit)!") 

def hard():
    answer=" "
    while True:
        print("I'll tell you only the animals on the farms")
        answer= input("Which farm would you like to inspect?(NE Farm) (W Farm) (SE Farm): ").lower()
        if answer == "ne farm":
            for x in farms[0]["agriculture"]:
                print(x)
        elif answer == "w farm":
            for x in farms[1]["agriculture"]:
                print(x)
        elif answer == "se farm":
            for x in farms[2]["agriculture"]:
                print(x)
                break
        elif answer == "exit":
            break
        else:
            print("Your only options are (NE Farm) (W Farm) (SE Farm) (Exit)!") 

def test():
    answer= input("choose").lower()
    choice = 0
    if answer == "ne farm":
        choice= 0
    elif answer == "w farm":
        choice= 1
    elif answer == "se farm":
        choice= 2
    for x in farms[choice]["agriculture"]:
        if x in animals:
            print(x)

if __name__ == "__main__":
    main()

