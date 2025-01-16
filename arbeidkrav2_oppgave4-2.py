# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 07:03:47 2025

@author: aeriksen
"""

#Program som bruker Dictionary for oversikt over Land, Hovedstad og innbyggere.
#Og ber bruker 

#Dictionary med oversikt over land, hovedstad og innbyggere i millioner.
land_innbygger = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

# Funksjon for at bruker skal kunne legge til nytt land
nytt_land = input("Skriv inn navnet landet: ")
hovedstad = input("Skriv inn hovedstaden i " + nytt_land +": " )
innbyggere = float(input("Skriv inn antall innbyggere i " + hovedstad + " (i millioneFinlandr): "))

# Oppdaterer dictionaryen med den nye informasjonen
land_innbygger[nytt_land] = [hovedstad, innbyggere]

# Skriver ut den oppdaterte dictionaryen
print("Oppdatert dictionary:")
print(land_innbygger)
