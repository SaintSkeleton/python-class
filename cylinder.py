# cylinder.py
# Manuel
# Solution to a cylender's area and volume

import math

r = float(input("Enter the cylinder's radius: "))
h = float(input("Enter the cylinder's height: "))
a = 2 * math.pi * r**2 + h * 2 * math.pi * r 
v = h * math.pi * r**2
print("Cylinder's area:", a, "u^2")
print("Cylinder's volume", v, "u^3")
