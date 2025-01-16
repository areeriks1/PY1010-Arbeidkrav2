# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 08:39:22 2025

@author: aeriksen
"""

import math

# Brukerinput for a og b
a = float(input("Skriv inn lengden på a: "))
b = float(input("Skriv inn lengden på b: "))

# Beregn hypotenusen og radiusen til halvsirkelen
hypotenus = math.sqrt(a**2 + b**2)
radius = hypotenus / 2

# Beregn arealet (trekanten + halvsirkelen)
areal_trekant = (a * b) / 2
areal_halvsirkel = (math.pi * radius**2) / 2
areal = areal_trekant + areal_halvsirkel

# Beregn ytre omkrets (katetene + halvsirkelens bue)
omkrets = a + b + (math.pi * radius)

# Skriver ut resultatene
print("Arealet er: " + str(areal))
print("Omkretsen av figuren er: " + str(omkrets))
