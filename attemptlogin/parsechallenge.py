#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginsucces = 0 # counter for fails

# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# loop over the file
for line in keystone_file:

    # if this 'fail pattern' appears in the line...
    if "GET" or "POST" in line:
        loginsucces += 1 # this is the same as loginfail = loginfail + 1

print("The number of successful login attempts is", loginsucces)
keystone_file.close() # close the open file

## This is no complete. The class started again and I will probably forget about this challenge.
## Also I don't know what a successful login attempt looks like.
