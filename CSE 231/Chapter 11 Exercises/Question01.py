# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:47:05 2023

@author: Conner O'Sullivan
"""

class Student(object):
    def __init__( self, score = 10 ):
        self.score = score
    def add_score(self):
        self.score += 10
    def decrease_score(self):
        self.score -= 10
    def __str__(self):
        return str(self.score)
        

