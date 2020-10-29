#!/usr/bin/python3

stars= ["*", "* *", "* * *", "* * * *", "* * * * *", "* * * *", "* * *", "* *", "*"]

for x in stars:
    print(x)

for star in range(1,6):
    print(star * "* ")
for star in range(4,0,-1):
    print(star * "* ")

