# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:37:58 2025

@author: aeriksen
"""

#Program som bruker Dictionary for oversikt over Land, Hovedstad og innbyggere.

#Dictionary med oversikt over land, hovedstad og innbyggere i millioner.

land_innbygger ={
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
    }

#Ber bruker om input på det landet bruker ønsker info om
land = input("Skriv inn et land du ønsker å vite mer om:")

#skriver ut svaret
hovedstad, antallinnbyggere = land_innbygger[land] #Gir verdiene i Dictionary et navn for bedre oversikt
print(hovedstad + " er hovedstaden i " + land + " og det er " + str(antallinnbyggere) + " mill. innbyggere i " + hovedstad + ".")

