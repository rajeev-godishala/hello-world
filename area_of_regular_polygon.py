import math
from math import tan, pi
print("""This program calculates the area of a regular polygon using the length of one 
side of a polygon and the number of sides on a polygon.""")
n = int(input("How many sides does your polygon have? No decimal numbers or letters: "))
s = float(input("What is the length of one of your polygon sides? Please enter here and no letters: "))
unit = input("What is the measurement of one of your polygon sides? Please enter here: ")
A = (n * s ** 2) / (4 * tan(pi / n))
A_rounded = "%.2f" % A
print(f"The area of the regular polygon using the numbers you entered is {A_rounded} sq {unit}")