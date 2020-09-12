print("This program is calculates the area of a triangle using base and height.")
base = float(input("What is the base of your triangle? Please enter here and no letters: "))
height = float(input("What is the height of your triangle. Please enter here and no letters: "))
unit = input("What unit do you want to use for the area of your triangle? Please enter here: ")
A = base * height / 2
A_rounded = "%.2f" % A
print(f"The area of your triangle using the numbers you entered is {A_rounded} sq. {unit}")