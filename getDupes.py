#!/usr/bin/env python3


from collections import Counter
import sys
import os


os.system('clear')
getFile = input("Enter File Name: ")

try:
   with open(getFile, 'r') as f:
      c=Counter(c.strip().lower() for c in f)
      print("\nDuplicates Found")
      print("=======================")

      for line in c:
         if c[line] > 1:
            print(line + " : Dup#: " + str(int(c[line])))
   f.close

except FileNotFoundError:
   progName = os.path.basename(__file__)
   print("File:\'{}\' does NOT exist!".format(getFile))
   print("Program:\'{}\' is exiting ...".format(progName))
   sys.exit(1)

else:
   print("\nThanks for playing -- Good Bye!")
