# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:03:54 2025

@author: aeriksen
"""
#Program for å beregne antall pizza som må kjøpes og krive ut svar på skjerm
# Be om antall elever fra bruker
antall_elever = int(input("Skriv inn antall elever: "))

#Beregner antall pizza (hver erlev spiser 1/4 pizz = 0,25 Pizza)
#antall_pizzaer = antall_elever * 0.25
antall_pizzaer = (antall_elever + 3) // 4  # Runder opp svaret fro å få heltall 

# Skriver ut antall pizza til skjerm
print("Det må kjøpes inn", antall_pizzaer, "pizzaer til klassefesten.")