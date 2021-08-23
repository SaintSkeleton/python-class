# grav_force.py
# Manuel Luciano Reyes Constantino
# Gravitational force between bodies

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
z1 = float(input("Enter z1: "))
m1 = float(input("Enter m1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
z2 = float(input("Enter z2: "))
m2 = float(input("Enter m2: "))
r = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
G = 6.67408*(10**-11)
F = G*(m1 * m2 / r**2)
print("Gravitational force", F, "N")
