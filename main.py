import os
import sys
from time import sleep

PREFIX = ">> "

os.system("title= Hacker Program Master - By Korte007")

print("\nTo hack a database type name\n\n")

target = input(PREFIX)

print("\nHacking progress started")
sleep(2)
print("\nSearching all known addresses for " + target )
sleep(2)
print("\nSearching all Databases for " + target)
sleep(2)
print("\nSearching all Servers for " + target)
sleep(2)
print("\nOne match found [", target, "]")
sleep(2)
print("\nProceed?")

reply = input("ENTER")

print("\nProceeding ...")
sleep(4)
print("\nStart attack  ")

reply = input()



def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "₪"*x, "×"*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


import time

for i in progressbar(range(35), "Get all password and permission to Your PC: ", 40):
    time.sleep(0.1)

print("\nDone!")
sleep(2)
print("\nFirewall detected!")

reply = input("\nATTACK!")

def progressbar(it, prefix="", size=100, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "₪"*x, "×"*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

for i in progressbar(range(35), "Attacking: ", 40):
    time.sleep(0.1)

print("\nDone!")
sleep(2)
print("\nSaving files.......")
sleep(2)
print("\nFiles saved to Your PC!")

reply = input("\nPress ENTER to exit!")

