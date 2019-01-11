

import os


 mycompre = ['Fizz-Buzz' if (x % 5 == 0 and x % 3 == 0) else 'Fizz' if (x % 5 == 0) else 'Buzz' if (x % 3 == 0) else x for x in range(1,100)]
 for items in mycompre:
    print(items)
