#!/usr/bin/env python3



try:
   import os
   import sys
   from collections import Counter
   from time import sleep

   os.system('clear')
   print("\nModule Importation successful ...\n")

except Exception as e:
   print("Module failure with {} ...".format(e))

else:
   while True:

      print("Will now look for duplicates ...")
      getFile = input("Enter File: ")

      try:
         with open(getFile, 'r') as f:
            c = Counter(c.strip().lower() for c in f if c.strip().lower())
            print("\nDuplicates Found")
            print("=====================\n")

            count = 0
            for line in c:
               if c[line] > 1:
                  print(line + " --> : Dup#: " + str(int(c[line])))
                  count+=1

         f.close()
         if count == 0:
            print("0 Duplicates Found ...")
            break

      except FileNotFoundError:
         print("\n{} does NOT exist ...".format(getFile))
         print("Try again ...")
         sleep(1)
         os.system('clear')
      else:
         print("\nThanks for playing!")
         break
