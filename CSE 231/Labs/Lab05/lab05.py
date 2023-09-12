# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:09:01 2023

@author: Conner O'Sullivan
"""

#################################
## CSE 231
## Lab 5
#################################
fp = open('data.txt')  # open the file
outfile = open("output.txt","w") # open another file in write mode

total_lines = 0
total_height = 0
max_height = 0
min_height = 10**6

total_weight = 0
max_weight = 0
min_weight= 10**6

total_bmi = 0
max_bmi = 0
min_bmi = 10**6

for line in fp:
    name = line[:12]
    height = line[12:24]
    weight = line[24:36]
    if total_lines == 0:
        header = '{:<12s}{:<12s}{:<12s}{:<12s}'
        print(header.format(name, height, weight, 'BMI'), file = outfile)
    total_lines += 1
    try:
        weight = float(weight.strip())
        height = float(height.strip())
        bmi = weight/(height**2)
        
        if weight > max_weight:
            max_weight = weight
            
        if weight < min_weight:
            min_weight = weight
            
        if height > max_height:
            max_height = height
            
        if height < min_height:
            min_height = height
        
        if bmi > max_bmi:
            max_bmi = bmi
        
        if bmi < min_bmi:
            min_bmi = bmi
            
        total_height += height
        total_weight += weight
        total_bmi += bmi
        
        avg_height = total_height/(total_lines-1) # -1 to ignore the header
        avg_weight = total_weight/(total_lines-1) # -1 to ignore the header
        avg_bmi = total_bmi/(total_lines-1) # -1 to ignore the header
        
        body = "{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}"
        print(body.format(name,height,weight,bmi), file = outfile)
        
    except ValueError:
        continue
fp.close()
avg_str = "\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}"
print(avg_str.format('Average',avg_height,avg_weight,avg_bmi), file = outfile)
print(body.format('Max',max_height,max_weight,max_bmi), file = outfile)
print(body.format('Min',min_height,min_weight,min_bmi), file = outfile)
outfile.close() 


