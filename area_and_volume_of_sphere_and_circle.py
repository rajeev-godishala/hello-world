import math
from math import pi
r = float(input("What is the radius of your circle and sphere? Please type here and no letters: "))
area_of_circle = pi * r ** 2
area_of_circle_formatted = "%.2f" % area_of_circle
print(f"The area of a circle using the radius you entered is: {area_of_circle_formatted}")
volume_of_sphere = 4/3 * pi * r ** 3
volume_of_sphere_formatted = "%.2f" % volume_of_sphere
print(f"The volume of a sphere using the radius you entered is: {volume_of_sphere_formatted}")