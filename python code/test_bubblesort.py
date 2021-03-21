#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter an integer value"))
    if n%2 !=0:
        print("Weird")
    elif (n%2 == 0) and n>20:
        print("Not Weird")
    elif (n%2==0)and(n<=20 or n>=6):
         print("Weird")
    elif (n%2==0) and (n>=2 or n<=5):
          print("Not Weird")
