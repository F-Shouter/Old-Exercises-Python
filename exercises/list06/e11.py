import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if 1 <= n <= 20:
    if n % 2 != 0:
        print ("Weird")
    elif (2 <= n) or (n <= 5):
        print("Not Weird")
    elif (6 <= n) or (n <=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Not Weird")