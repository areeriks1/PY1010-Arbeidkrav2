# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:10:47 2025

@author: aeriksen
"""
# program for omregning fra grader til Radianer

#importerer modulen numpy
import numpy as np

# Bruker må skrive inn gradetallet:
v_grad = float(input('Skriv inn gradtallet: '))

# Regn om fra grader til radianer
v_rad = v_grad * np.pi / 180 #formel for utregning av radiantall

# Skriver resultatet til skjerm
print('Vinkelen', v_grad, 'grader er det samme som', round(v_rad, 4), 'radianer.')