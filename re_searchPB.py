try:
   import os
   import re
   import sys

   os.system('clear')
   progName = os.path.basename(__file__)

except Exception as e:
   print("Error: {}".format(e))
   print("{} is terminating ...".format(progName))
   sys.exit(1)

else:
   print("All modules imported successfully ...")
   try:
      with open('phonebook.txt', 'r') as f:

         content = f.read()
         pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

         matches = pattern.finditer(content)
         for match in matches:
            print(match)

   except Exception as e2:
      print("Error: {} ...".format(e2))
      print("{} terminating ...".format(progName))
      sys.exit(1)

   else:
      print("\n----------------------------------------------------------------")
      print("Final Results -- Thanks!")
