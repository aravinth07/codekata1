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
number=int(input())
if(number>0):   
    if number%2 ==0 and number !=0:
        print("even")
    else:
        print("odd")
else:
    print("invalid")
