#!/usr/bin/python3

# I found some spaghetti code online and wanted to see if I could make it not spaghetti

# Original spaghetti code

#for i in [1,2,3]:
#    def printMa():
#        print ('Ma')
#    x = True
#    if x == True:
#     printMa()
#    y = False
#    if y == True:
#     printMa()
#    else:
#     print("Ma")
#    y = True
#    if x and y == True:
#        if i == 3:
#            print('Mia let me GO !')
#        else:
#           print ('Mia')

# OUTPUT:
# Ma Ma mia Ma Ma mia Ma Ma mia let me GO !

# This was my sulotion
for i in [1,2,3]:
    print("Ma")
    print("Ma")
    if i == 3:
        print('Mia let me GO !')
    else:
        print ('Mia')
