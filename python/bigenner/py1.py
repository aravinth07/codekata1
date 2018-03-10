#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rgcet
#
# Created:     10/03/2018
# Copyright:   (c) rgcet 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
number=raw_input()
if(number.isnumeric()):
    print("u entered a number")
    number=int(number)
    if number%2 ==0 and number !=0:
        print("even")
    else:
        print("odd")
else:
    print("invalid")
