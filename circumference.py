import math
from math import pi
print("This program finds the circumference of a circle using radius.")
unit = input("What is the unit of your circumference? Enter here: ")
r = float(input("What is the radius of your circle? Enter here: "))
c = 2 * pi * r
c_rounded = "%.2f" % c
print(f"The circumference of your circle using radius is {c_rounded} {unit}")