# initial_velocity.py
# Manuel Luciano Reyes Constantino
# Initial velocity of a projectile

import math

x = float(input("Enter x: "))
y = float(input("Enter y: "))
T = math.radians(float(input("Enter angle in degrees: ")))
g = 9.81
xsin = x * math.sin(2 * T)
ycos = 2 * y * math.cos(T)**2
v0 = math.sqrt((x**2 * g) / (xsin - ycos))
print("Initial Velocity is:", v0, "m/s")

