#!/usr/bin/env python3
#! python3
import os
import sys
# vyrvořil: Jan Buchmaier V2A
file = sys.argv[0]
are = False
for i in file:
    if i in "01234567890":
        are = True

if not are:
    number = "1"
    name = file
else:
    number = ""
    number2 = ""
    for i in file:
        if i in "0123456789":
            number2 += i
    number = str(int(number2) + 1)
    name = file
    for ii in range(10):
        name = name.replace(str(ii), "")
if sys.platform == "linux":
    dir = os.getcwd() + "/"
    name = name.replace("./", "")
    name = name.replace(dir, "")
    old = name

    name = name.replace(".py", "")
    name = name + number + ".py"
    print(name)

    os.system("cp " + dir + old +" "+ dir + name)
    os.system("chmod +x " + dir + name)
    if number != "10":
        os.system(dir + "./" + name)
else:
    dir = os.getcwd() + '\\'
    name = name.replace(dir, "")
    old = name

    name = name.replace(".py", "")
    name = name + number + ".py"
    print(name)

    os.system("copy " + dir + old + " " + dir + name)
    if number != "10":
        os.system(name)