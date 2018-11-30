try:

   import subprocess
   import json
   import sys
   import os
   import boo

   os.system('clear')
   print("All modules installed successfully")

except Exception as e:

   os.system('clear')
   prog_n = os.path.basename(__file__)
   print("ERROR: {}!".format(e))
   print("{} is terminating ...".format(prog_n))
   sys.tracbacklimit = 0
   sys.exit(1)
