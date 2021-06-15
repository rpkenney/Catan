# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 10:58:08 2021

@author: kenn5
"""

import numpy as np

def roll_dice():
    return (np.random.randint(1, 7), np.random.randint(1, 7))

def roll_to_start(players):
    tie = True
    while tie:
        vals =  np.random.randint(1, 7, 2)
        tie = np.count_nonzero(vals == max(vals)) > 1
        
    return dict(zip(players, vals))