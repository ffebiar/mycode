#!/usr/bin/python3


# My (eyes)! The (goggles) do (nothing)!


def main():
    challenge()
    trial()

def challenge():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!") 
  
def trial():
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    print(f"My {trial[2]['goggles']}! The {trial[2]['eyes']} do {trial[3]}!")

# Did not have enought time to finish :(
def nightmare():
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


if __name__ == "__main__":
    main()
