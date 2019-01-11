

# FizzBuzz - Comprehension style

mycompre = ['Fizz-Buzz' if (x % 5 == 0 and x % 3 == 0) else 'Fizz' if (x % 5 == 0) else 'Buzz' if (x % 3 == 0) else x for x in range(1,100)]
for items in mycompre:
   print(items)


# Walk Directory, find all files ending in ".py"
  
for root, dirs, files in os.walk(myPath):
   for file in files:
      if file.endswith(".py"):
         print(os.path.join(root, file))
         
         
# Get Dupes in File ...
import os
from collections import Counter

os.system('clear')
getFile = input("\nEnter File: ")


with open(getFile, 'r') as f:
    c = Counter(c.strip().lower() for c in f if c.strip().lower())
    print("____________________\n")

    for item in c:
        if c[item]>1:
            print(item + " -->  " + str(int(c[item])) + " Dupes ...")

print("____________________\n")
f.close()

