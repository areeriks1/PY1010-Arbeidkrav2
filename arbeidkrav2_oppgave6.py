# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:53:09 2025

@author: aeriksen
"""

import numpy as np
import matplotlib.pyplot as plt

# Definer x og funksjonen f(x)
x = np.linspace(-10, 10, 200)  # 200 punkter jevnt fordelt mellom -10 og 10
y = -x**2 - 5  # Funksjonen f(x) = -x^2 - 5

# Plot funksjonen
plt.plot(x, y, label=r"$f(x) = -x^2 - 5$", color="blue")  # Tegn funksjonen med etikett og farge

# Legg til tittel og aksebeskrivelser
plt.title("Graf")
plt.xlabel("x")
plt.ylabel("f(x)")

# Vis grafen
plt.show()
