# diagonal.py
# Manuel
# Solution to the lenght of a rectangle diagonal

import math

w = float(input("Enter the rectangle's width: "))
h = float(input("Enter the rectangle's height: "))
d = math.sqrt(h**2 + w**2)
print("rectangle's diagonal:", d, "u")
