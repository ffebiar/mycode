#!/usr/bin/env python3

trash= ["cigarette butts", "cigarette butts", "cigarette butts",]
butt= 0

print("For every cigarette butt I find in the trash, I'm going to make you smoke a pack!")
for cig in trash:
    butt += 1
    print(f"I found {butt} {cig}! Go smoke {butt} pack!")


words= ["s***", "f***", "b****"]
count= 32
smack= 0
print("For every bad word that you say, I'm going to slap a tooth out of your mouth")
for curse in words:
    count -= 1
    smack += 1
    print(f"You said {curse}! I'm gonna smack you {smack} time! you only have {count} teeth left!")
    
floor= []
money= 0
legos= 0

print("For every lego I find on the floor, your dad will put another dollar in my money jar")
while legos <= 11:
    legos += 1
    floor.append("1")
    for lego in floor:
        money += 1
        print(f"I found {money} piece on the floor! That's {money} dollar in my money jar")
