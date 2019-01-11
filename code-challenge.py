

# FizzBuzz - Comprehension style

mycompre = ['Fizz-Buzz' if (x % 5 == 0 and x % 3 == 0) else 'Fizz' if (x % 5 == 0) else 'Buzz' if (x % 3 == 0) else x for x in range(1,100)]
for items in mycompre:
   print(items)


# Walk Directory, find all files ending in ".py"
  
for root, dirs, files in os.walk(myPath):
   for file in files:
      if file.endswith(".py"):
         print(os.path.join(root, file))
