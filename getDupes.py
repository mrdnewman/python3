#!/usr/bin/env python3

from collections import Counter
import sys
import os


os.system('clear')
getFile = input("Enter File Name: ")


try:
   with open(getFile, 'r') as f:

          #expression for items in function if conditional
      c = Counter(c.strip().lower() for c in f if c.strip().lower())

      count = 0
      print("\nDuplicate List")
      print("========================\n")

      for line in c:
         if c[line] > 1:
            print(line + " --> Dup#: " + str(int(c[line])))
            count +=1
   f.close
   if count == 0:
      print("ZERO Duplicates Found ...")

except FileNotFoundError:
   progName = os.path.basename(__file__)
   print("File: \'{}\' does NOT exist!".format(getFile))
   print("Program: \'{}\' is terminating ...".format(progName))
   sys.exit(1)

else:
   print("\nThanks for playing -- Good Bye!")

