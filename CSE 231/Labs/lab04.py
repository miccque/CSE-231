# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:24:49 2023

@author: Conner O'Sullivan
"""

def leap_year(y):
    year = int(y)
    return True if (year%4 == 0 and year%100 != 0) or year%400 == 0 else False

def rotate(s,n):
    return (s[-n:]+s[:len(s)-n])
    
def digit_count(num):
    x = str(num)
    even_count, odd_count, zero_count = 0,0,0
    for index,number in enumerate(x):
        if number.isdigit():
            if int(number) == 0:
                zero_count += 1
            elif int(number)%2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            break
    return (even_count,odd_count,zero_count)

def float_check(flt):
    return True if (flt.replace(".","",1).isdigit()) else False
