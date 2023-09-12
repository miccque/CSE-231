# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 19:15:07 2023

@author: Conner O'Sullivan
"""
def open_file():
    fp = open('scores.txt')
    return fp

def student_info(line):
    grade = []
    name = [line[:20].strip()]
    grade_str = line[20:].strip().split()
    for i in grade_str: grade.append(int(i))
    mean_grade = [sum(grade)/4]
    return tuple(name + grade + mean_grade)

def display(student_list):
    print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format(
        "Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
    for index in student_list:
        print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(*index))
    grade_one_avg = sum(grade[1] for grade in student_list)/5
    grade_two_avg = sum(grade[2] for grade in student_list)/5
    grade_three_avg = sum(grade[3] for grade in student_list)/5
    grade_four_avg = sum(grade[4] for grade in student_list)/5
    print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean",
        grade_one_avg, grade_two_avg, grade_three_avg, grade_four_avg))

def main ():
    fp = open_file()
    student_list = []
    for line in fp:
        info = student_info(line)
        student_list.append(info)
    student_list.sort()
    display(student_list)
    
main()