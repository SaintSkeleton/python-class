# sphere.py
# Manuel
# Solution to a sphere's area and volume
 
import math

r = float(input("Enter sphere's radius: "))
a = 4 * math.pi * r**2
v = 4 * math.pi * r**3 / 3
print("Sphere's area:", a, "u^2")
print("Volume:", v, "u^3")
