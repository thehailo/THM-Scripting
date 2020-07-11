# TryHackMe's "Scripting" room (https://tryhackme.com/room/scripting).
# Learn basic scripting by solving some challenges!

# Task 1 - Base64
#
# This file has been base64 encoded 50 times - write a script to retrieve the
# flag. Here is the general process to do this:
#
# 1. Read input from the file.
# 2. Use function to decode the file.
# 3. Do process in a loop.

import base64

# Prompt user for challenge filename.
userfile = input("Enter your challenge filename: ")

# Open challenge file.
with open(userfile) as challengefile:
	flag = challengefile.read()

# Decode challenge file 50 times.
for i in range(50):
	flag = base64.b64decode(flag)

# Present final decoded flag.
print("The flag is: " + (flag.decode("utf-8")))